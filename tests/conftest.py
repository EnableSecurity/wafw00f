"""Shared pytest fixtures for wafw00f tests."""

import pytest
from unittest.mock import MagicMock


class MockResponse:
    """Mock HTTP response for testing."""

    def __init__(self, status_code=200, headers=None, text='', reason='OK'):
        self.status_code = status_code
        self.headers = headers or {}
        self.text = text
        self.reason = reason
        self._content = text.encode('utf-8') if isinstance(text, str) else text

    @property
    def content(self):
        return self._content


@pytest.fixture
def mock_response():
    """Factory fixture to create mock responses."""
    def _make_response(status_code=200, headers=None, text='', reason='OK'):
        return MockResponse(status_code, headers, text, reason)
    return _make_response


@pytest.fixture
def wafw00f_instance():
    """Create a WAFW00F instance for testing."""
    from wafw00f.main import WAFW00F
    return WAFW00F(target='https://example.com')
