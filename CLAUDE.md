# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

WAFW00F is a Web Application Firewall (WAF) fingerprinting and detection tool written in Python. It identifies WAF products protecting web applications through HTTP response analysis and behavioral testing.

## Development Commands

### Testing
```bash
# Run all tests
pytest

# Run tests with verbose output
pytest -v

# Run specific test file
pytest tests/test_evillib.py

# Run specific test
pytest tests/test_evillib.py::TestWafToolsEngine::test_default_timeout

# Run tests with coverage
pytest --cov=wafw00f --cov-report=term-missing
```

### Linting
```bash
# Run linter (prospector)
prospector wafw00f --strictness veryhigh
```

### Building and Installing
```bash
# Install in development mode with dev dependencies
pip install -e .[dev,docs]

# Build distribution packages
python setup.py sdist bdist_wheel

# Clean build artifacts
make clean
```

### Publishing New Release
```bash
# 1. Update version in wafw00f/__init__.py
# 2. Update version in README.md (badge and ASCII art examples - 3 places)
# 3. Run tests
pytest

# 4. Build package
python setup.py sdist bdist_wheel

# 5. Upload to PyPI
twine upload dist/*

# 6. Create GitHub release
gh release create vX.Y.Z --title "vX.Y.Z" --notes "Release notes here"

# 7. Commit version changes
git add wafw00f/__init__.py README.md
git commit -m "Bump version to X.Y.Z"
git push
```

## Architecture

### Core Components

**main.py** - Entry point and orchestration
- `WAFW00F` class extends `waftoolsengine` and orchestrates the detection workflow
- Contains attack payload definitions (XSS, SQLi, LFI, XXE, RCE)
- Implements detection methods: `matchHeader()`, `matchStatus()`, `matchCookie()`, `matchContent()`, `matchReason()`
- Provides attack request generators: `normalRequest()`, `xssAttack()`, `sqliAttack()`, `centralAttack()`, etc.
- Two detection modes:
  - `identwaf()`: Plugin-based detection using WAF-specific signatures
  - `genericdetect()`: Behavioral detection when no plugin matches

**manager.py** - Plugin loader
- Dynamically discovers and loads all Python files from `wafw00f/plugins/`
- Uses `importlib.util` for runtime module loading
- Returns dictionary: `{plugin_name: plugin_module}`

**wafprio.py** - Detection priority
- Ordered list of 182 WAF names defining which plugins to check first
- Optimization: fast header/cookie checks before complex logic
- Plugins not in the list are still checked but after prioritized ones

**evillib.py** - HTTP request engine
- `waftoolsengine` class wraps the `requests` library
- Enforces 100KB max response size to prevent hanging on streaming responses
- Enforces timeout during response body reading (not just connection)
- Default timeout: 7 seconds (configurable)
- Disables SSL warnings for testing self-signed certificates
- Streams responses in 8KB chunks

### Detection Flow

1. **Normal request**: Baseline HTTP request to establish normal behavior
2. **Attack request**: `centralAttack()` sends combined XSS+SQLi+LFI payload
3. **Plugin detection**: Iterate through prioritized plugins, each calling `is_waf(self)`
4. **Generic detection**: If no plugin matches, analyze behavioral differences (status codes, headers, blocking)

### Plugin System

Plugins are minimal Python modules in `wafw00f/plugins/` with exactly 2 requirements:

```python
NAME = 'WAF Name (Manufacturer)'

def is_waf(self):
    # 'self' is the WAFW00F instance
    # Access: self.rq (normal response), self.attackres (attack response)
    # Available methods: matchHeader, matchCookie, matchContent, matchStatus, matchReason
    if self.matchHeader(('server', 'cloudflare')):
        return True
    return False
```

**Common detection patterns:**

1. **Simple single-check** (e.g., `cloudflare.py`):
   - Check for specific header, cookie, or content pattern

2. **Multiple checks** (e.g., `incapsula.py`):
   - Try several different signatures (OR logic)

3. **Schema-based** (e.g., `modsecurity.py`):
   - Multiple helper functions checking combinations of conditions (AND logic)
   - Example: `check_schema_02()` requires both 403 status AND "ModSecurity Action" reason

**Detection methods available to plugins:**
- `matchHeader((name, pattern), attack=False)` - Regex match on header
- `matchCookie(pattern, attack=False)` - Shortcut for Set-Cookie header
- `matchContent(regex, attack=True)` - Regex match on response body
- `matchStatus(code, attack=True)` - Match HTTP status code
- `matchReason(phrase, attack=True)` - Match HTTP reason phrase

## Adding New WAF Detection

1. Create `wafw00f/plugins/newwaf.py`
2. Define `NAME` constant with "WAF Name (Manufacturer)" format
3. Define `is_waf(self)` function returning True/False
4. Optionally add WAF name to `wafprio.py` for priority detection
5. Add test to `tests/test_detection.py`:
   ```python
   @responses.activate
   def test_detect_newwaf_by_header(self):
       responses.add(responses.GET, 'https://example.com',
                     headers={'Server': 'NewWAF'}, status=200)
       engine = WAFW00F('https://example.com')
       assert 'NewWAF' in engine.identwaf()
   ```

## Important Notes for Development

### Timeout Handling (Issue #246)
The timeout parameter must be enforced during both:
1. Connection establishment (handled by requests library)
2. Response body reading (enforced manually in `evillib.py`)

When modifying request logic, ensure timeouts are respected during streaming to prevent hangs on slow servers.

### Response Size Limiting
Always use `stream=True` with requests and enforce `MAX_RESPONSE_SIZE` (100KB) to prevent memory issues and hanging on:
- Streaming media servers (audio/video)
- Infinite response generators
- Large file downloads

### Version Updates
When bumping version, update **3 locations**:
1. `wafw00f/__init__.py` - `__version__` variable
2. `README.md` - Badge (line 18)
3. `README.md` - ASCII art examples (lines 53 and 253)

### Commit Messages
Follow conventional format:
- "Fix X" for bug fixes
- "Add X" for new features
- "Update X" for enhancements
- Include issue references: "Fix timeout enforcement (issue #246)"

### Testing WAF Plugins
When testing plugin detection:
- Use `@responses.activate` decorator
- Mock HTTP responses with specific headers/content/status
- Test both positive (WAF detected) and negative (not detected) cases
- Check against actual attack responses when possible

### Git Workflow
- Main branch: `master`
- Always run tests before committing
- Push releases to both GitHub and PyPI
- Create GitHub releases using `gh release create`
