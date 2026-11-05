#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tests for ``--headers`` file parsing and what the product actually sends.

Covers ``wafw00f.main.getheaders()`` and the product chain

    CLI main() -> getheaders() -> WAFW00F -> waftoolsengine.Request()
    -> requests.Request.prepare() -> Session.send() -> JSON result

Only the last network boundary is replaced: ``requests.sessions.Session.send``
is patched so the real ``PreparedRequest`` built by the product can be
inspected.  A socket guard (see ``setUpModule``) makes any accidental real
connection fail loudly, so these tests never touch the network.

Runs with either ``python -m unittest tests.test_headers`` or ``pytest
tests/test_headers.py``; no extra dependencies.
"""

import io
import json
import os
import shutil
import sys
import tempfile
import unittest
from unittest import mock

import requests

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if REPO_ROOT not in sys.path:
    sys.path.insert(0, REPO_ROOT)

import wafw00f.main as main_mod  # noqa: E402

BODY = b'<html><body>Hello World</body></html>'
TARGET = 'https://example.com'


class _FakeRaw(object):
    """Minimal urllib3-response-alike so the product's streaming loop runs."""

    def __init__(self, body):
        self._body = body
        self.closed = False

    def stream(self, amt=8192, decode_content=False):
        for i in range(0, len(self._body), amt):
            yield self._body[i:i + amt]

    def read(self, amt=None, decode_content=False):
        data, self._body = self._body, b''
        return data

    def release_conn(self):
        pass


def _blocked_connect(*args, **kwargs):
    raise AssertionError(
        'network guard: a real socket connection was attempted during tests '
        '(args=%r)' % (args,))


_PATCHES = []


def setUpModule():
    """Refuse real connections for the whole module (no loopback either)."""
    for target, attr in (('socket', 'create_connection'),
                         ('socket', 'getaddrinfo')):
        p = mock.patch('%s.%s' % (target, attr), _blocked_connect)
        p.start()
        _PATCHES.append(p)
    for attr in ('connect', 'connect_ex'):
        p = mock.patch('socket.socket.%s' % attr, _blocked_connect)
        p.start()
        _PATCHES.append(p)


def tearDownModule():
    for p in reversed(_PATCHES):
        p.stop()
    del _PATCHES[:]


def _stop_session_send(captured):
    def _send(self, request, **kwargs):
        captured.append({
            'url': request.url,
            'headers': dict(request.headers),
        })
        resp = requests.models.Response()
        resp.status_code = 200
        resp.reason = 'OK'
        resp.url = request.url
        resp.request = request
        resp.headers = requests.structures.CaseInsensitiveDict({
            'Server': 'nginx',
            'Content-Type': 'text/html',
            'Content-Length': str(len(BODY)),
        })
        resp.raw = _FakeRaw(BODY)
        resp._content = BODY
        resp._content_consumed = True
        return resp
    return _send


class TestGetheaders(unittest.TestCase):
    """wafw00f.main.getheaders() on real files (real function, no stubs)."""

    def setUp(self):
        self.tmp = tempfile.mkdtemp(prefix='wafw00f-hdr-')

    def tearDown(self):
        shutil.rmtree(self.tmp, ignore_errors=True)

    def _write(self, text, name='headers.txt'):
        path = os.path.join(self.tmp, name)
        with open(path, 'w', encoding='utf-8') as fh:
            fh.write(text)
        return path

    def test_plain_headers_are_parsed(self):
        path = self._write(
            'X-Api-Key: abc123\n'
            'User-Agent: Wafw00fProbe/1.0\n')
        self.assertEqual(main_mod.getheaders(path),
                         {'X-Api-Key': 'abc123',
                          'User-Agent': 'Wafw00fProbe/1.0'})

    def test_url_value_is_kept_whole(self):
        path = self._write('Referer: https://example.com/page\n')
        parsed = main_mod.getheaders(path)
        self.assertIsNotNone(parsed)
        self.assertIn('Referer', parsed,
                      'header line with a ":" in its value was dropped: %r'
                      % (parsed,))
        self.assertEqual(parsed['Referer'], 'https://example.com/page')

    def test_multi_colon_value_is_kept_whole(self):
        path = self._write('X-Trace: req:abc:def\n')
        parsed = main_mod.getheaders(path)
        self.assertIn('X-Trace', parsed,
                      'value with several ":" was dropped: %r' % (parsed,))
        self.assertEqual(parsed['X-Trace'], 'req:abc:def')

    def test_ipv6_value_is_kept_whole(self):
        path = self._write('X-Forwarded-For: 2001:db8::1\n'
                           'X-Real-IP: [2001:db8::2]:8080\n')
        parsed = main_mod.getheaders(path)
        self.assertEqual(parsed.get('X-Forwarded-For'), '2001:db8::1')
        self.assertEqual(parsed.get('X-Real-IP'), '[2001:db8::2]:8080')

    def test_empty_value_is_kept(self):
        path = self._write('X-Empty:\nX-Blank:   \nX-Normal: v1\n')
        parsed = main_mod.getheaders(path)
        self.assertEqual(parsed.get('X-Empty'), '')
        self.assertEqual(parsed.get('X-Blank'), '')
        self.assertEqual(parsed.get('X-Normal'), 'v1')

    def test_whitespace_around_name_and_value_is_stripped(self):
        path = self._write('   X-Padded   :   spaced value   \n')
        self.assertEqual(main_mod.getheaders(path), {'X-Padded': 'spaced value'})

    def test_line_without_separator_is_skipped(self):
        path = self._write('not-a-header-line\n\nX-Ok: 1\n')
        self.assertEqual(main_mod.getheaders(path), {'X-Ok': '1'})

    def test_missing_file_returns_none(self):
        self.assertIsNone(
            main_mod.getheaders(os.path.join(self.tmp, 'does-not-exist.txt')))


class TestCliChain(unittest.TestCase):
    """CLI -> getheaders -> PreparedRequest -> -o JSON, send() replaced."""

    def setUp(self):
        self.tmp = tempfile.mkdtemp(prefix='wafw00f-cli-')

    def tearDown(self):
        shutil.rmtree(self.tmp, ignore_errors=True)

    def _write(self, text, name):
        path = os.path.join(self.tmp, name)
        with open(path, 'w', encoding='utf-8') as fh:
            fh.write(text)
        return path

    def _run_cli(self, header_path, out_name):
        out_path = os.path.join(self.tmp, out_name)
        argv = ['wafw00f', '--no-colors']
        if header_path is not None:
            argv += ['--headers', header_path]
        argv += ['-o', out_path, TARGET]

        captured = []
        buf = io.StringIO()
        old_argv, old_stdout = sys.argv, sys.stdout
        sys.argv = argv
        sys.stdout = buf
        try:
            with mock.patch.object(requests.sessions.Session, 'send',
                                   _stop_session_send(captured)):
                main_mod.main()
            code = 0
        except SystemExit as exc:
            code = exc.code if isinstance(exc.code, int) else 1
        finally:
            sys.argv, sys.stdout = old_argv, old_stdout
        return captured, code, buf.getvalue(), out_path

    def test_cli_plain_header_reaches_prepared_request(self):
        hdr = self._write('X-Api-Key: abc123\n', 'plain.txt')
        captured, code, out, _ = self._run_cli(hdr, 'plain.json')
        self.assertEqual(code, 0, out)
        self.assertTrue(captured, 'no request reached the send() boundary')
        self.assertEqual(captured[0]['headers'].get('X-Api-Key'), 'abc123')

    def test_cli_url_and_multi_colon_values_reach_prepared_request(self):
        hdr = self._write(
            'X-Api-Key: abc123\n'
            'Referer: https://example.com/page\n'
            'X-Trace: req:abc:def\n'
            'X-Forwarded-For: 2001:db8::1\n', 'values.txt')
        captured, code, out, _ = self._run_cli(hdr, 'values.json')
        self.assertEqual(code, 0, out)
        self.assertTrue(captured, 'no request reached the send() boundary')
        sent = captured[0]['headers']
        self.assertEqual(sent.get('X-Api-Key'), 'abc123')
        self.assertEqual(sent.get('Referer'), 'https://example.com/page',
                         'values containing ":" never reached the wire: %r'
                         % (sorted(sent),))
        self.assertEqual(sent.get('X-Trace'), 'req:abc:def')
        self.assertEqual(sent.get('X-Forwarded-For'), '2001:db8::1')

    def test_cli_json_result_is_written(self):
        hdr = self._write('X-Api-Key: abc123\n', 'consumer.txt')
        _, code, out, out_path = self._run_cli(hdr, 'consumer.json')
        self.assertEqual(code, 0, out)
        self.assertTrue(os.path.exists(out_path), 'no -o output file written')
        with open(out_path, encoding='utf-8') as fh:
            data = json.load(fh)
        self.assertIsInstance(data, list)
        self.assertEqual(len(data), 1)
        for key in ('url', 'detected', 'trigger_url', 'firewall',
                    'manufacturer'):
            self.assertIn(key, data[0])
        self.assertEqual(data[0]['url'], TARGET)

    def test_cli_missing_headers_file_fails_without_sending(self):
        missing = os.path.join(self.tmp, 'nope.txt')
        captured, code, _, _ = self._run_cli(missing, 'missing.json')
        self.assertNotEqual(code, 0, 'missing --headers file must fail')
        self.assertEqual(captured, [], 'no request should be sent')


if __name__ == '__main__':
    unittest.main(verbosity=2)
