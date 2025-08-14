# Troubleshooting Guide

Common issues and solutions for the Playwright automation template.

## Installation Issues

### Python Dependencies

**Issue**: `ModuleNotFoundError` or import errors

**Solutions**:
```bash
# Ensure virtual environment is activated
source .venv/bin/activate  # Unix/Mac
# or
.venv\Scripts\activate  # Windows

# Upgrade pip and reinstall
pip install --upgrade pip
pip install -r requirements.txt

# Clear pip cache if needed
pip cache purge
```

### Playwright Browser Installation

**Issue**: Browser not found or installation errors

**Solutions**:
```bash
# Install all browsers with dependencies
playwright install --with-deps

# Install specific browser
playwright install chromium

# Check browser status
playwright install --dry-run
```

## Test Execution Issues

### Test Failures

**Issue**: Random test failures or timeouts

**Solutions**:
- Check screenshots in `screenshots/` directory
- Increase timeout values in settings
- Use explicit waits instead of fixed delays
- Verify test data and environment setup

**Issue**: Element not found errors

**Solutions**:
- Use data-testid attributes for stable locators
- Implement proper wait strategies
- Check for dynamic content loading
- Verify page state before interactions

### Performance Issues

**Issue**: Slow test execution

**Solutions**:
- Run tests in parallel with `-n` option
- Use headless browser mode
- Optimize locator strategies
- Cache browser contexts when possible

## Environment Issues

### Configuration Problems

**Issue**: Settings not loading correctly

**Solutions**:
- Verify `.env` file exists and has correct format
- Check environment variable names and prefixes
- Validate Pydantic settings classes
- Use absolute paths for file references

### Authentication Issues

**Issue**: API authentication failures

**Solutions**:
- Verify API keys and credentials
- Check token expiration
- Validate request headers
- Test authentication endpoints manually

## Development Issues

### Code Quality

**Issue**: Linting or formatting errors

**Solutions**:
```bash
# Auto-format code
make fmt

# Fix linting issues
flake8 src tests --show-source

# Type checking
mypy src tests
```

**Issue**: Pre-commit hooks failing

**Solutions**:
```bash
# Install pre-commit hooks
pre-commit install

# Run hooks manually
pre-commit run --all-files

# Update hook versions
pre-commit autoupdate
```

## Debug Mode

### Verbose Logging
```bash
# Enable debug logging
export LOG_LEVEL=DEBUG
pytest -s -v
```

### Playwright Debug
```bash
# Visual debugging
PWDEBUG=1 pytest tests/ui/test_example.py

# Slow motion
pytest --browser-channel=chrome --headed --slowmo=1000
```

### Screenshots and Videos
```bash
# Enable video recording
pytest --video=on

# Take screenshots on failure
pytest --screenshot=on
```

## CI/CD Issues

### GitHub Actions Failures

**Common Issues**:
- Browser installation timeouts
- Test timeouts in CI environment
- Environment variable configuration
- Artifact upload issues

**Solutions**:
- Increase timeout values for CI
- Use matrix strategy for parallel execution
- Cache dependencies properly
- Verify secrets configuration

## Getting Help

1. Check the error message and stack trace
2. Review logs and screenshots
3. Search existing issues in the repository
4. Consult Playwright documentation
5. Create a detailed issue report with:
   - Error message
   - Steps to reproduce
   - Environment details
   - Relevant logs/screenshots