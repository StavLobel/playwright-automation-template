"""
Pytest configuration and fixtures for the automation framework.

This module provides shared fixtures for test execution including
browser setup, test context creation, and common utilities.
"""

import uuid
import pytest
from typing import Generator

from playwright.sync_api import Page, Browser, APIRequestContext
from src.core.types import TestContext
from src.config.settings import get_settings


@pytest.fixture(scope="function")
def test_context(request: pytest.FixtureRequest) -> TestContext:
    """
    Create a test context with correlation ID and metadata.
    
    Args:
        request: Pytest request object
        
    Returns:
        TestContext: Test execution context
    """
    settings = get_settings()
    
    context = TestContext(
        correlation_id=str(uuid.uuid4())[:8],
        test_name=request.node.name,
        browser_name=getattr(request.config.option, 'browser_name', 'chromium')
    )
    
    return context


@pytest.fixture(scope="function")
def api_context(playwright) -> Generator[APIRequestContext, None, None]:
    """
    Create an API request context for API testing.
    
    Args:
        playwright: Playwright instance
        
    Yields:
        APIRequestContext: Playwright API request context
    """
    settings = get_settings()
    
    # Create API request context with base configuration
    context = playwright.request.new_context(
        base_url=settings.airportgap.base_url,
        extra_http_headers={
            "Accept": "application/json",
            "User-Agent": "Playwright-Automation-Template/1.0"
        }
    )
    
    yield context
    
    # Cleanup
    context.dispose()


# Example page object fixtures (to be customized)
@pytest.fixture(scope="function")
def example_page(page: Page, test_context: TestContext):
    """
    Example page object fixture.
    
    Replace this with your actual page objects.
    """
    from src.pages.example_page import ExamplePage  # Replace with actual import
    return ExamplePage(page, test_context)


# Example API client fixtures (to be customized)
@pytest.fixture(scope="function")
def example_api_client(api_context: APIRequestContext, test_context: TestContext):
    """
    Example API client fixture.
    
    Replace this with your actual API clients.
    """
    from src.api.example_client import ExampleClient  # Replace with actual import
    return ExampleClient(api_context, test_context)