"""Tests for the --output file handling in the command line entry point."""

import pytest

from wafw00f.main import _open_output


class TestOpenOutput:
    """Tests for _open_output."""

    def test_writes_to_an_existing_directory(self, tmp_path):
        """Verify a writable path is opened and usable."""
        outfile = _open_output(str(tmp_path / 'report.csv'))
        try:
            outfile.write('data')
        finally:
            outfile.close()
        assert (tmp_path / 'report.csv').read_text() == 'data'

    def test_missing_directory_is_an_error(self):
        """Verify a missing directory exits instead of raising a traceback."""
        with pytest.raises(SystemExit) as excinfo:
            _open_output('/nonexistent-report-dir/report.csv')
        assert excinfo.value.code == 1
