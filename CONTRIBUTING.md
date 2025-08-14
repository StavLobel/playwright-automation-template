# Contributing to Playwright Automation Template

Thank you for your interest in contributing! This document provides guidelines for contributing to this project.

## Getting Started

### Prerequisites
- Python 3.11+
- Node.js 18+ (for Playwright)
- Git

### Setup Development Environment

1. Fork and clone the repository:
```bash
git clone https://github.com/YOUR_USERNAME/playwright-automation-template.git
cd playwright-automation-template
```

2. Create a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # Unix/Mac
# or
.venv\Scripts\activate  # Windows
```

3. Install dependencies:
```bash
make install-dev
```

## Development Workflow

### Code Quality
Before submitting any changes, ensure your code meets our quality standards:

```bash
# Format code
make fmt

# Run linting
make lint

# Run type checking
make type

# Run all quality checks
make ci
```

### Testing
Run tests to ensure your changes don't break existing functionality:

```bash
# Run all tests
make test-all

# Run specific test types
make test-ui
make test-api
make test-smoke
```

### Pre-commit Hooks
We use pre-commit hooks to ensure code quality. They are automatically installed with `make install-dev`.

To run hooks manually:
```bash
pre-commit run --all-files
```

## Contribution Guidelines

### Code Standards
- Follow PEP 8 style guidelines
- Use type hints for all public functions and methods
- Write comprehensive docstrings (Google style)
- Maintain line length of 88 characters
- Use meaningful variable and function names

### Testing Standards
- Write tests for all new features
- Maintain or improve test coverage
- Use descriptive test names
- Group related tests in classes
- Use appropriate pytest markers

### Documentation
- Update relevant documentation
- Add docstrings to new functions and classes
- Update README if adding new features
- Include examples when helpful

### Commit Messages
Use conventional commit format:
```
type(scope): description

[optional body]

[optional footer]
```

Types:
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes
- `refactor`: Code refactoring
- `test`: Test changes
- `chore`: Maintenance tasks

Examples:
```
feat(pages): add login page object
fix(api): handle timeout errors in API client
docs(readme): update installation instructions
```

## Pull Request Process

1. Create a feature branch:
```bash
git checkout -b feature/your-feature-name
```

2. Make your changes and commit:
```bash
git add .
git commit -m "feat: add your feature"
```

3. Run quality checks:
```bash
make ci
make test-all
```

4. Push to your fork:
```bash
git push origin feature/your-feature-name
```

5. Create a pull request with:
   - Clear description of changes
   - Link to related issues
   - Screenshots (for UI changes)
   - Test results

### Pull Request Checklist
- [ ] Code follows style guidelines
- [ ] Self-review completed
- [ ] Tests added/updated
- [ ] Documentation updated
- [ ] No breaking changes (or clearly documented)
- [ ] All CI checks pass

## Reporting Issues

When reporting issues, please include:
- Clear description of the problem
- Steps to reproduce
- Expected vs actual behavior
- Environment details (OS, Python version, etc.)
- Relevant logs or error messages
- Screenshots (if applicable)

## Feature Requests

For feature requests:
- Describe the feature and its benefits
- Provide use cases
- Consider implementation approach
- Check for existing similar requests

## Code of Conduct

This project follows a Code of Conduct. By participating, you agree to uphold this code. Please report unacceptable behavior to the project maintainers.

## Questions?

If you have questions about contributing:
- Check existing documentation
- Search closed issues
- Create a new issue with the question label
- Contact maintainers

Thank you for contributing!