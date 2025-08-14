"""
Application settings and configuration management.

This module handles environment-specific configuration using Pydantic settings,
providing typed configuration objects for different parts of the application.
"""

import os
from typing import Optional

from pydantic import Field
from pydantic_settings import BaseSettings


class SauceDemoSettings(BaseSettings):
    """
    Configuration for SauceDemo application testing.
    """

    base_url: str = Field(default="https://www.saucedemo.com", description="Base URL for SauceDemo")
    username: str = Field(default="standard_user", description="Login username")
    password: str = Field(default="secret_sauce", description="Login password")
    page_timeout: int = Field(default=30000, description="Page load timeout in milliseconds")
    element_timeout: int = Field(default=30000, description="Element wait timeout in milliseconds")

    class Config:
        env_prefix = "SAUCEDEMO_"


class AirportGapSettings(BaseSettings):
    """
    Configuration for AirportGap API testing.
    """

    base_url: str = Field(default="https://airportgap.com", description="Base URL for AirportGap API")
    api_timeout: int = Field(default=30000, description="API request timeout in milliseconds")
    api_key: Optional[str] = Field(default=None, description="API key for authentication")

    class Config:
        env_prefix = "AIRPORTGAP_"


class BrowserSettings(BaseSettings):
    """
    Configuration for browser settings.
    """

    headless: bool = Field(default=True, description="Run browser in headless mode")
    timeout: int = Field(default=30000, description="Browser timeout in milliseconds")
    viewport_width: int = Field(default=1920, description="Browser viewport width")
    viewport_height: int = Field(default=1080, description="Browser viewport height")

    class Config:
        env_prefix = "BROWSER_"


class TestSettings(BaseSettings):
    """
    Configuration for test execution settings.
    """

    timeout: int = Field(default=30000, description="Default test timeout in milliseconds")
    retries: int = Field(default=0, description="Number of test retries on failure")
    parallel_workers: int = Field(default=1, description="Number of parallel test workers")

    class Config:
        env_prefix = "TEST_"


class AppSettings(BaseSettings):
    """
    Main application settings container.
    """

    saucedemo: SauceDemoSettings = Field(default_factory=SauceDemoSettings)
    airportgap: AirportGapSettings = Field(default_factory=AirportGapSettings)
    browser: BrowserSettings = Field(default_factory=BrowserSettings)
    test: TestSettings = Field(default_factory=TestSettings)

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


# Global settings instance
_settings: Optional[AppSettings] = None


def get_settings() -> AppSettings:
    """
    Get the global settings instance.
    
    Returns:
        AppSettings: Application settings
    """
    global _settings
    if _settings is None:
        _settings = AppSettings()
    return _settings


def reload_settings() -> AppSettings:
    """
    Reload settings from environment.
    
    Returns:
        AppSettings: Fresh application settings
    """
    global _settings
    _settings = AppSettings()
    return _settings