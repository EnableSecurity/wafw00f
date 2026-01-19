"""Tests for the WAFW00F matching functions."""

import pytest
from wafw00f.main import WAFW00F


class TestMatchHeader:
    """Tests for the matchHeader function."""

    def test_match_header_exact(self, wafw00f_instance, mock_response):
        """Test matching an exact header value."""
        wafw00f_instance.rq = mock_response(headers={'Server': 'cloudflare'})
        assert wafw00f_instance.matchHeader(('Server', 'cloudflare'), attack=False)

    def test_match_header_regex(self, wafw00f_instance, mock_response):
        """Test matching header with regex."""
        wafw00f_instance.rq = mock_response(headers={'Server': 'cloudflare-nginx'})
        assert wafw00f_instance.matchHeader(('Server', r'cloudflare.*'), attack=False)

    def test_match_header_case_insensitive(self, wafw00f_instance, mock_response):
        """Test that header matching is case insensitive."""
        wafw00f_instance.rq = mock_response(headers={'Server': 'CLOUDFLARE'})
        assert wafw00f_instance.matchHeader(('Server', 'cloudflare'), attack=False)

    def test_match_header_not_found(self, wafw00f_instance, mock_response):
        """Test when header doesn't match."""
        wafw00f_instance.rq = mock_response(headers={'Server': 'nginx'})
        assert not wafw00f_instance.matchHeader(('Server', 'cloudflare'), attack=False)

    def test_match_header_missing(self, wafw00f_instance, mock_response):
        """Test when header is missing."""
        wafw00f_instance.rq = mock_response(headers={})
        assert not wafw00f_instance.matchHeader(('Server', 'cloudflare'), attack=False)

    def test_match_header_none_response(self, wafw00f_instance):
        """Test when response is None."""
        wafw00f_instance.rq = None
        result = wafw00f_instance.matchHeader(('Server', 'cloudflare'), attack=False)
        assert result is None


class TestMatchContent:
    """Tests for the matchContent function."""

    def test_match_content_exact(self, wafw00f_instance, mock_response):
        """Test matching exact content."""
        wafw00f_instance.attackres = mock_response(text='Access Denied by Cloudflare')
        assert wafw00f_instance.matchContent('Access Denied')

    def test_match_content_regex(self, wafw00f_instance, mock_response):
        """Test matching content with regex."""
        wafw00f_instance.attackres = mock_response(text='Error 403: Forbidden by WAF')
        assert wafw00f_instance.matchContent(r'Error \d+:.*WAF')

    def test_match_content_case_insensitive(self, wafw00f_instance, mock_response):
        """Test that content matching is case insensitive."""
        wafw00f_instance.attackres = mock_response(text='ACCESS DENIED')
        assert wafw00f_instance.matchContent('access denied')

    def test_match_content_not_found(self, wafw00f_instance, mock_response):
        """Test when content doesn't match."""
        wafw00f_instance.attackres = mock_response(text='Welcome to our website')
        assert not wafw00f_instance.matchContent('Access Denied')

    def test_match_content_none_response(self, wafw00f_instance):
        """Test when response is None."""
        wafw00f_instance.attackres = None
        result = wafw00f_instance.matchContent('test')
        assert result is None


class TestMatchCookie:
    """Tests for the matchCookie function."""

    def test_match_cookie(self, wafw00f_instance, mock_response):
        """Test matching a cookie."""
        wafw00f_instance.rq = mock_response(
            headers={'Set-Cookie': '__cfduid=abc123; path=/'}
        )
        assert wafw00f_instance.matchCookie('__cfduid', attack=False)

    def test_match_cookie_regex(self, wafw00f_instance, mock_response):
        """Test matching cookie with regex."""
        wafw00f_instance.rq = mock_response(
            headers={'Set-Cookie': 'session_id=xyz789; path=/'}
        )
        assert wafw00f_instance.matchCookie(r'session_id=\w+', attack=False)

    def test_match_cookie_not_found(self, wafw00f_instance, mock_response):
        """Test when cookie doesn't match."""
        wafw00f_instance.rq = mock_response(
            headers={'Set-Cookie': 'other_cookie=value'}
        )
        assert not wafw00f_instance.matchCookie('__cfduid', attack=False)


class TestMatchStatus:
    """Tests for the matchStatus function."""

    def test_match_status_200(self, wafw00f_instance, mock_response):
        """Test matching 200 status code."""
        wafw00f_instance.attackres = mock_response(status_code=200)
        assert wafw00f_instance.matchStatus(200)

    def test_match_status_403(self, wafw00f_instance, mock_response):
        """Test matching 403 status code."""
        wafw00f_instance.attackres = mock_response(status_code=403)
        assert wafw00f_instance.matchStatus(403)

    def test_match_status_mismatch(self, wafw00f_instance, mock_response):
        """Test when status code doesn't match."""
        wafw00f_instance.attackres = mock_response(status_code=200)
        assert not wafw00f_instance.matchStatus(403)

    def test_match_status_none_response(self, wafw00f_instance):
        """Test when response is None."""
        wafw00f_instance.attackres = None
        result = wafw00f_instance.matchStatus(200)
        assert result is None


class TestMatchReason:
    """Tests for the matchReason function."""

    def test_match_reason_ok(self, wafw00f_instance, mock_response):
        """Test matching OK reason."""
        wafw00f_instance.attackres = mock_response(reason='OK')
        assert wafw00f_instance.matchReason('OK')

    def test_match_reason_forbidden(self, wafw00f_instance, mock_response):
        """Test matching Forbidden reason."""
        wafw00f_instance.attackres = mock_response(reason='Forbidden')
        assert wafw00f_instance.matchReason('Forbidden')

    def test_match_reason_mismatch(self, wafw00f_instance, mock_response):
        """Test when reason doesn't match."""
        wafw00f_instance.attackres = mock_response(reason='OK')
        assert not wafw00f_instance.matchReason('Forbidden')
