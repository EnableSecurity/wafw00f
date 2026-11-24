"""Tests for the text output helper."""

from wafw00f.main import getTextResults


def test_get_text_results_with_results():
    results = [
        {
            'url': 'http://example.com',
            'trigger_url': 'http://example.com/?x=1',
            'firewall': 'None',
            'manufacturer': 'None',
            'detected': False,
        }
    ]
    rows = getTextResults(results)
    assert len(rows) == 1
    assert 'http://example.com' in rows[0]


def test_get_text_results_without_results():
    """An empty result list must not raise (a report with no hits is valid)."""
    assert getTextResults([]) == []
