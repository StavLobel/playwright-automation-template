# Development Guide

This guide covers development practices and conventions for the Playwright automation template.

## Code Style

### Python Code Standards
- Follow PEP 8 guidelines
- Use type hints for all public functions and methods
- Line length: 88 characters (Black default)
- Use Google-style docstrings

### Testing Best Practices

#### Test Organization
- UI tests in `tests/ui/`
- API tests in `tests/api/`
- Use pytest markers: `@pytest.mark.ui`, `@pytest.mark.api`, `@pytest.mark.smoke`
- Group related tests in classes with `Test` prefix

#### Page Object Model (POM)
- All page objects inherit from `BasePage`
- Define locators as class constants in UPPER_SNAKE_CASE
- Implement abstract properties: `url_pattern` and `page_title`
- Page methods should perform single actions without assertions

#### API Clients
- All API clients inherit from `BaseAPIClient`
- One client class per endpoint group
- Use typed response models (dataclasses)
- Include proper error handling and logging

### Logging
- Use structured logging with correlation IDs
- Log method entry/exit with timing information
- Include relevant context in log messages
- Use appropriate log levels (DEBUG, INFO, WARNING, ERROR)

### Configuration
- Use Pydantic settings classes
- Environment variable prefixes for different components
- Support for multiple environments (local, CI, staging)
- Never commit secrets or API keys

## Makefile Targets

```bash
# Install dependencies
make install

# Format code
make fmt

# Run linting
make lint

# Run type checking
make type

# Run all tests
make test-all

# Run UI tests only
make test-ui

# Run API tests only
make test-api

# Run smoke tests
make test-smoke

# Run quality checks
make ci
```

## Running Tests

### Local Development
```bash
# Run all tests
pytest

# Run specific test types
pytest -m ui
pytest -m api
pytest -m smoke

# Run with specific browser
pytest tests/ui/ --browser=firefox

# Run with verbose output
pytest -v
```

### Test Data
- Store test data in `testdata/` directory
- Use YAML or JSON format
- Load data via fixtures in `conftest.py`
- Do not hardcode test data in test files

## Troubleshooting

### Common Issues

#### Import Errors
- Ensure `src/` is in Python path
- Check `pyproject.toml` pythonpath configuration
- Verify virtual environment is activated

#### Browser Issues
- Run `playwright install` to install browsers
- Check browser dependencies with `playwright install --with-deps`
- Verify headless mode settings

#### Test Failures
- Check screenshots in `screenshots/` directory
- Review logs for error messages
- Verify test data and environment variables

### Debug Mode
```bash
# Run with debug logging
PYTEST_CURRENT_TEST=1 pytest -s -v

# Run single test with debugging
pytest tests/ui/test_example.py::TestExampleUI::test_page_loads -s -v

# Run with Playwright debug mode
PWDEBUG=1 pytest tests/ui/
```