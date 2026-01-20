"""Tests for the evillib module."""

import pytest
import responses
from wafw00f.lib.evillib import waftoolsengine, MAX_RESPONSE_SIZE


class TestWafToolsEngine:
    """Tests for the waftoolsengine class."""

    def test_default_timeout(self):
        """Test default timeout is set."""
        engine = waftoolsengine(target='https://example.com')
        assert engine.timeout == 7

    def test_custom_timeout(self):
        """Test custom timeout can be set."""
        engine = waftoolsengine(target='https://example.com', timeout=30)
        assert engine.timeout == 30

    def test_default_headers(self):
        """Test default headers are set."""
        engine = waftoolsengine(target='https://example.com')
        assert 'User-Agent' in engine.headers
        assert 'Accept' in engine.headers

    def test_custom_headers(self):
        """Test custom headers can be set."""
        custom = {'X-Custom': 'value'}
        engine = waftoolsengine(target='https://example.com', head=custom)
        assert engine.headers == custom

    @responses.activate
    def test_request_success(self):
        """Test successful request."""
        responses.add(
            responses.GET,
            'https://example.com',
            body='Hello World',
            status=200
        )

        engine = waftoolsengine(target='https://example.com')
        resp = engine.Request()

        assert resp is not None
        assert resp.status_code == 200
        assert engine.requestnumber == 1

    @responses.activate
    def test_request_increments_counter(self):
        """Test request counter increments."""
        responses.add(responses.GET, 'https://example.com', status=200)
        responses.add(responses.GET, 'https://example.com', status=200)

        engine = waftoolsengine(target='https://example.com')
        engine.Request()
        engine.Request()

        assert engine.requestnumber == 2

    @responses.activate
    def test_response_content_accessible(self):
        """Test response content is accessible after streaming read."""
        test_content = 'This is test content for WAF detection'
        responses.add(
            responses.GET,
            'https://example.com',
            body=test_content,
            status=200
        )

        engine = waftoolsengine(target='https://example.com')
        resp = engine.Request()

        assert resp.content == test_content.encode('utf-8')
        assert resp.text == test_content


class TestResponseSizeLimit:
    """Tests for the response size limiting feature."""

    def test_max_response_size_defined(self):
        """Test MAX_RESPONSE_SIZE is defined."""
        assert MAX_RESPONSE_SIZE > 0
        assert MAX_RESPONSE_SIZE == 100 * 1024  # 100KB

    @responses.activate
    def test_small_response_fully_read(self):
        """Test small responses are fully read."""
        small_content = 'x' * 1000  # 1KB
        responses.add(
            responses.GET,
            'https://example.com',
            body=small_content,
            status=200
        )

        engine = waftoolsengine(target='https://example.com')
        resp = engine.Request()

        assert len(resp.content) == 1000

    @responses.activate
    def test_large_response_truncated(self):
        """Test large responses are truncated to MAX_RESPONSE_SIZE."""
        large_content = 'x' * (MAX_RESPONSE_SIZE + 50000)  # 150KB
        responses.add(
            responses.GET,
            'https://example.com',
            body=large_content,
            status=200
        )

        engine = waftoolsengine(target='https://example.com')
        resp = engine.Request()

        # Should be truncated to around MAX_RESPONSE_SIZE (may be slightly over due to chunk size)
        assert len(resp.content) <= MAX_RESPONSE_SIZE + 8192
        assert len(resp.content) >= MAX_RESPONSE_SIZE


class TestTimeoutEnforcement:
    """Tests for timeout enforcement during response reading."""

    @responses.activate
    def test_timeout_attribute_used(self):
        """Test timeout is properly configured and accessible.

        Note: Testing actual timeout enforcement during slow streaming
        requires integration tests with real servers, as the responses
        mock library doesn't support time-based streaming simulation.
        The timeout enforcement logic in Request() will break out of
        the chunk reading loop if time.time() - start_time > self.timeout.
        """
        responses.add(
            responses.GET,
            'https://example.com',
            body='test',
            status=200
        )

        engine = waftoolsengine(target='https://example.com', timeout=5)
        resp = engine.Request()

        # Verify the engine has timeout configured
        assert engine.timeout == 5
        assert resp is not None
