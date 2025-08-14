"""
Example page object implementation.

Replace this with your actual page object classes.
"""

from src.core.base_page import BasePage
from src.core.types import TestContext
from playwright.sync_api import Page


class ExamplePage(BasePage):
    """
    Example page object.
    
    Replace this with your actual page object implementation.
    """

    # Example locators (replace with your actual locators)
    TITLE_LOCATOR = "h1"
    BUTTON_LOCATOR = "button[data-testid='example-button']"
    INPUT_LOCATOR = "input[data-testid='example-input']"
    SUCCESS_MESSAGE_LOCATOR = ".success-message"

    def __init__(self, page: Page, context: TestContext) -> None:
        """
        Initialize the example page.
        
        Args:
            page: Playwright page instance
            context: Test execution context
        """
        super().__init__(page, context)

    @property
    def url_pattern(self) -> str:
        """
        URL pattern for this page.
        
        Returns:
            str: URL pattern that identifies this page
        """
        return "/example"  # Replace with your actual URL pattern

    @property
    def page_title(self) -> str:
        """
        Expected page title.
        
        Returns:
            str: Expected page title
        """
        return "Example Page"  # Replace with your actual page title

    def click_example_button(self) -> None:
        """
        Click the example button.
        
        Replace with your actual page methods.
        """
        self.logger.info("Clicking example button")
        self.click_element(self.BUTTON_LOCATOR)

    def fill_example_input(self, text: str) -> None:
        """
        Fill the example input field.
        
        Args:
            text: Text to input
            
        Replace with your actual page methods.
        """
        self.logger.info(f"Filling example input with: {text}")
        self.fill_text(self.INPUT_LOCATOR, text)

    def get_title_text(self) -> str:
        """
        Get the page title text.
        
        Returns:
            str: Title text
            
        Replace with your actual page methods.
        """
        return self.get_text(self.TITLE_LOCATOR)

    def is_success_message_visible(self) -> bool:
        """
        Check if success message is visible.
        
        Returns:
            bool: True if success message is visible
            
        Replace with your actual page methods.
        """
        return self.is_element_visible(self.SUCCESS_MESSAGE_LOCATOR)