"""Tests for CSV export of scan results.

Every CSV row has to carry one cell per column of the header row. Records for
detected and undetected targets are built with different key orders, so a mixed
report only stays readable when each record is serialized through the header.
"""

import csv
import io
import json
import random
import sys
import urllib.parse

import pytest
from requests.adapters import HTTPAdapter
from requests.models import Response
from requests.structures import CaseInsensitiveDict

from wafw00f.main import buildResultRecord, main as wafw00f_main


DETECTED_TARGET = 'https://waf-a.test/'
SECOND_DETECTED_TARGET = 'https://waf-c.test/'
# A comma in the path forces the writer to quote the url cell.
COMMA_PLAIN_TARGET = 'http://plain-b.test/a,b'
# Accented characters make sure cells survive the round trip unchanged. These
# targets are only exported to stdout, which is not affected by the locale
# dependent default encoding of open().
UNICODE_DETECTED_TARGET = 'https://waf-a.test/päth,ü/'
UNICODE_PLAIN_TARGET = 'http://plain-b.test/naïve,ok/'

DETECTED_HEADER = ['url', 'detected', 'trigger_url', 'firewall', 'manufacturer']
UNDETECTED_HEADER = ['url', 'trigger_url', 'detected', 'firewall', 'manufacturer']

# Both export runs of a test share this seed, so the randomized attack urls are
# comparable between the CSV output and its JSON control.
RANDOM_SEED = 20261107

CSV_OUTPUTS = [
    pytest.param(['-o', '{output}'], False, '.csv', id='csv-extension'),
    pytest.param(['-o', '-', '-f', 'csv'], True, None, id='stdout-explicit-csv'),
    pytest.param(['-o', '{output}', '-f', 'csv'], False, '.txt', id='forced-csv-other-extension'),
]


def _fake_response(request):
    """Build a real response object for one of the canned sites."""
    hostname = urllib.parse.urlsplit(request.url).hostname or ''
    headers = {'Content-Type': 'text/html'}
    if hostname.startswith('waf-'):
        headers['Server'] = 'cloudflare'
    response = Response()
    response.url = request.url
    response.status_code = 200
    response.reason = 'OK'
    response.encoding = 'utf-8'
    response.headers = CaseInsensitiveDict(headers)
    response._content = b'<html><body>ok</body></html>'
    response._content_consumed = True
    response.raw = None
    return response


@pytest.fixture
def export_transport(monkeypatch):
    """Answer the scan locally at the single HTTP transport entry point."""
    sent_urls = []

    def send(adapter, request, **kwargs):
        sent_urls.append(request.url)
        return _fake_response(request)

    monkeypatch.setattr(HTTPAdapter, 'send', send)
    return sent_urls


def _run_export(args, monkeypatch, stdout=None):
    """Run main() and always hand the global state back untouched."""
    monkeypatch.setattr(sys, 'argv', ['wafw00f'] + list(args))
    random_state = random.getstate()
    original_stdout = sys.stdout
    if stdout is not None:
        # main() redirects sys.stdout to sys.__stdout__ when writing to '-'.
        monkeypatch.setattr(sys, '__stdout__', stdout)
        monkeypatch.setattr(sys, 'stdout', stdout)
    random.seed(RANDOM_SEED)
    try:
        wafw00f_main()
    finally:
        sys.stdout = original_stdout
        random.setstate(random_state)
    assert sys.stdout is original_stdout


def _read_csv(path):
    with open(path, newline='', encoding='utf-8') as handle:
        return list(csv.DictReader(handle))


def _parse_csv_text(text):
    return list(csv.DictReader(io.StringIO(text, newline='')))


def _read_json(path):
    with open(path, encoding='utf-8') as handle:
        return json.load(handle)


def _expected_cells(record):
    """CSV writes None as an empty cell and every other value via str()."""
    return {key: '' if value is None else str(value) for key, value in record.items()}


def _header_for(control):
    return DETECTED_HEADER if control[0]['detected'] else UNDETECTED_HEADER


def _assert_matches_control(rows, control):
    """Every cell of a CSV row equals the matching field of the JSON control."""
    assert len(rows) == len(control)
    for row, record in zip(rows, control):
        assert sorted(row) == sorted(_expected_cells(record))
        for key, expected in _expected_cells(record).items():
            assert row[key] == expected


def _assert_record_semantics(rows, targets):
    """Check the meaning of each cell instead of only its existence."""
    assert len(rows) == len(targets)
    for row, target in zip(rows, targets):
        assert row['url'] == target
        assert row['detected'] in ('True', 'False')
        assert row['detected'] != row['trigger_url']
        if row['detected'] == 'True':
            assert row['firewall'] == 'Cloudflare'
            assert row['manufacturer'] == 'Cloudflare Inc.'
            assert row['trigger_url'].startswith(target.rstrip('/'))
            assert 'XSS' in row['trigger_url']
        else:
            assert row['firewall'] == 'None'
            assert row['manufacturer'] == 'None'
            assert row['trigger_url'] == ''


class TestResultRecords:
    """The two record shapes are what makes a shared header order necessary."""

    def test_detected_and_undetected_records_keep_their_orders(self):
        detected = buildResultRecord(
            DETECTED_TARGET, 'Cloudflare (Cloudflare Inc.)', DETECTED_TARGET + '?q=1'
        )
        undetected = buildResultRecord(COMMA_PLAIN_TARGET, None, None)
        assert list(detected) == DETECTED_HEADER
        assert list(undetected) == UNDETECTED_HEADER
        assert detected['detected'] is True
        assert undetected['detected'] is False


class TestCsvExport:
    """Exported CSV must be readable by a plain csv.DictReader."""

    @pytest.mark.parametrize('output_args, to_stdout, suffix', CSV_OUTPUTS)
    @pytest.mark.parametrize(
        'targets',
        [
            pytest.param([DETECTED_TARGET, COMMA_PLAIN_TARGET], id='detected-first'),
            pytest.param([COMMA_PLAIN_TARGET, DETECTED_TARGET], id='undetected-first'),
        ],
    )
    def test_mixed_records_keep_their_cells(
        self, tmp_path, monkeypatch, export_transport, output_args, to_stdout, suffix, targets
    ):
        """Detected and undetected rows may not trade column values."""
        control_path = tmp_path / 'control.json'
        _run_export(['-o', str(control_path)] + targets, monkeypatch)
        control = _read_json(control_path)
        assert len(control) == 2
        assert sorted(control[0]) == sorted(DETECTED_HEADER)

        report_path = str(tmp_path / 'report') + (suffix or '')
        stdout = io.StringIO() if to_stdout else None
        args = [arg.format(output=report_path) for arg in output_args]
        _run_export(args + targets, monkeypatch, stdout=stdout)

        if to_stdout:
            rows = _parse_csv_text(stdout.getvalue())
        else:
            rows = _read_csv(report_path)

        assert list(rows[0]) == _header_for(control)
        _assert_matches_control(rows, control)
        _assert_record_semantics(rows, targets)
        assert export_transport

    def test_same_kind_records_are_unchanged(self, tmp_path, monkeypatch, export_transport):
        """A report where every target is detected still exports as before."""
        targets = [DETECTED_TARGET, SECOND_DETECTED_TARGET]
        control_path = tmp_path / 'control.json'
        _run_export(['-o', str(control_path)] + targets, monkeypatch)
        report_path = tmp_path / 'report.csv'
        _run_export(['-o', str(report_path)] + targets, monkeypatch)

        rows = _read_csv(report_path)
        control = _read_json(control_path)
        assert list(rows[0]) == DETECTED_HEADER
        _assert_matches_control(rows, control)
        _assert_record_semantics(rows, targets)

    @pytest.mark.parametrize(
        'targets',
        [
            pytest.param([UNICODE_DETECTED_TARGET, UNICODE_PLAIN_TARGET], id='detected-first'),
            pytest.param([UNICODE_PLAIN_TARGET, UNICODE_DETECTED_TARGET], id='undetected-first'),
        ],
    )
    def test_stdout_csv_quotes_urls_and_keeps_unicode(
        self, tmp_path, monkeypatch, export_transport, targets
    ):
        """Quoted url cells keep commas and non-ASCII characters intact."""
        control_path = tmp_path / 'control.json'
        _run_export(['-o', str(control_path)] + targets, monkeypatch)
        control = _read_json(control_path)

        stdout = io.StringIO()
        _run_export(['-o', '-', '-f', 'csv'] + targets, monkeypatch, stdout=stdout)
        text = stdout.getvalue()
        rows = _parse_csv_text(text)

        assert text.splitlines()[0] == ','.join(_header_for(control))
        assert '"' + targets[0] + '"' in text
        assert list(rows[0]) == _header_for(control)
        _assert_matches_control(rows, control)
        _assert_record_semantics(rows, targets)
