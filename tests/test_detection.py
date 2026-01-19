"""Integration tests for WAF detection."""

import pytest
import responses
from wafw00f.main import WAFW00F


class TestCloudflareDetection:
    """Tests for Cloudflare WAF detection."""

    @responses.activate
    def test_detect_cloudflare_by_header(self):
        """Test detecting Cloudflare by server header."""
        responses.add(
            responses.GET,
            'https://example.com',
            headers={'Server': 'cloudflare'},
            status=200
        )
        responses.add(
            responses.GET,
            'https://example.com',
            headers={'Server': 'cloudflare'},
            status=200
        )

        waf = WAFW00F(target='https://example.com')
        waf.rq = waf.Request()
        waf.attackres = waf.Request()

        from wafw00f.plugins import cloudflare
        assert cloudflare.is_waf(waf)

    @responses.activate
    def test_detect_cloudflare_by_cf_ray(self):
        """Test detecting Cloudflare by CF-RAY header."""
        responses.add(
            responses.GET,
            'https://example.com',
            headers={'CF-RAY': '1234567890abcdef-LAX'},
            status=200
        )
        responses.add(
            responses.GET,
            'https://example.com',
            headers={'CF-RAY': '1234567890abcdef-LAX'},
            status=200
        )

        waf = WAFW00F(target='https://example.com')
        waf.rq = waf.Request()
        waf.attackres = waf.Request()

        from wafw00f.plugins import cloudflare
        assert cloudflare.is_waf(waf)


class TestFastlyDetection:
    """Tests for Fastly detection."""

    @responses.activate
    def test_detect_fastly_by_request_id(self):
        """Test detecting Fastly by X-Fastly-Request-ID header."""
        responses.add(
            responses.GET,
            'https://example.com',
            headers={'X-Fastly-Request-ID': 'abc123def456'},
            status=200
        )
        responses.add(
            responses.GET,
            'https://example.com',
            headers={'X-Fastly-Request-ID': 'abc123def456'},
            status=200
        )

        waf = WAFW00F(target='https://example.com')
        waf.rq = waf.Request()
        waf.attackres = waf.Request()

        from wafw00f.plugins import fastly
        assert fastly.is_waf(waf)

    @responses.activate
    def test_detect_fastly_by_served_by(self):
        """Test detecting Fastly by X-Served-By header."""
        responses.add(
            responses.GET,
            'https://example.com',
            headers={'X-Served-By': 'cache-sjc10049-SJC'},
            status=200
        )
        responses.add(
            responses.GET,
            'https://example.com',
            headers={'X-Served-By': 'cache-sjc10049-SJC'},
            status=200
        )

        waf = WAFW00F(target='https://example.com')
        waf.rq = waf.Request()
        waf.attackres = waf.Request()

        from wafw00f.plugins import fastly
        assert fastly.is_waf(waf)


class TestAWSWAFDetection:
    """Tests for AWS WAF detection."""

    @responses.activate
    def test_detect_awswaf_by_header(self):
        """Test detecting AWS WAF by X-AMZ-ID header."""
        responses.add(
            responses.GET,
            'https://example.com',
            headers={'X-AMZ-ID': 'abc123xyz'},
            status=200
        )
        responses.add(
            responses.GET,
            'https://example.com',
            headers={'X-AMZ-ID': 'abc123xyz'},
            status=200
        )

        waf = WAFW00F(target='https://example.com')
        waf.rq = waf.Request()
        waf.attackres = waf.Request()

        from wafw00f.plugins import awswaf
        assert awswaf.is_waf(waf)


class TestNoWAFDetection:
    """Tests for when no WAF is detected."""

    @responses.activate
    def test_no_waf_plain_response(self):
        """Test that plain response doesn't trigger false positive."""
        responses.add(
            responses.GET,
            'https://example.com',
            headers={'Server': 'nginx'},
            body='<html><body>Hello World</body></html>',
            status=200
        )
        responses.add(
            responses.GET,
            'https://example.com',
            headers={'Server': 'nginx'},
            body='<html><body>Hello World</body></html>',
            status=200
        )

        waf = WAFW00F(target='https://example.com')
        waf.rq = waf.Request()
        waf.attackres = waf.Request()

        # Test some common WAF plugins don't trigger
        from wafw00f.plugins import cloudflare, fastly, awswaf
        assert not cloudflare.is_waf(waf)
        assert not fastly.is_waf(waf)
        assert not awswaf.is_waf(waf)


class TestAnubisDetection:
    """Tests for Anubis bot protection detection."""

    @responses.activate
    def test_detect_anubis_by_cookie(self):
        """Test detecting Anubis by cookie pattern."""
        responses.add(
            responses.GET,
            'https://example.com',
            headers={'Set-Cookie': 'site-anubis-auth=token123; path=/'},
            status=200
        )
        responses.add(
            responses.GET,
            'https://example.com',
            headers={'Set-Cookie': 'site-anubis-auth=token123; path=/'},
            status=200
        )

        waf = WAFW00F(target='https://example.com')
        waf.rq = waf.Request()
        waf.attackres = waf.Request()

        from wafw00f.plugins import anubis
        assert anubis.is_waf(waf)

    @responses.activate
    def test_detect_anubis_by_content(self):
        """Test detecting Anubis by page content."""
        anubis_page = '''
        <html>
        <head><script id="anubis_version">v1.0</script></head>
        <body>Protected by Anubis From Techaro</body>
        </html>
        '''
        responses.add(
            responses.GET,
            'https://example.com',
            body=anubis_page,
            status=200
        )
        responses.add(
            responses.GET,
            'https://example.com',
            body=anubis_page,
            status=200
        )

        waf = WAFW00F(target='https://example.com')
        waf.rq = waf.Request()
        waf.attackres = waf.Request()

        from wafw00f.plugins import anubis
        assert anubis.is_waf(waf)
