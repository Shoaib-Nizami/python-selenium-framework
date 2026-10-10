"""
Inventory Page Object Model.
Contains locators and actions for the product inventory page.
"""

from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class InventoryPage(BasePage):
    """Page object for the inventory/products page."""

    # Locators
    INVENTORY_CONTAINER = (By.ID, "inventory_container")
    PRODUCT_ITEMS = (By.CLASS_NAME, "inventory_item")
    PRODUCT_NAMES = (By.CLASS_NAME, "inventory_item_name")
    ADD_TO_CART_BUTTONS = (By.XPATH, "//button[contains(text(),'Add to cart')]")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    MENU_BUTTON = (By.ID, "react-burger-menu-btn")
    LOGOUT_LINK = (By.ID, "logout_sidebar_link")
    SORT_DROPDOWN = (By.CLASS_NAME, "product_sort_container")

    def is_on_inventory_page(self) -> bool:
        """Verify that the inventory page is loaded."""
        return (
            self.is_element_visible(self.INVENTORY_CONTAINER) and
            "inventory" in self.get_current_url()
        )

    def get_product_count(self) -> int:
        """Return the number of products displayed on the page."""
        return len(self.find_elements(self.PRODUCT_ITEMS))

    def add_product_to_cart(self, index: int = 0):
        """Add a product to cart by index (default: first product)."""
        buttons = self.find_elements(self.ADD_TO_CART_BUTTONS)
        if index < len(buttons):
            buttons[index].click()

    def get_cart_count(self) -> int:
        """Return the number displayed on the cart badge."""
        if self.is_element_visible(self.CART_BADGE):
            return int(self.get_text(self.CART_BADGE))
        return 0

    def open_menu(self):
        """Click the hamburger menu button."""
        self.click(self.MENU_BUTTON)

    def click_logout(self):
        """Click the logout link from the side menu."""
        self.click(self.LOGOUT_LINK)

    def get_all_product_names(self) -> list:
        """Return a list of all product names on the page."""
        elements = self.find_elements(self.PRODUCT_NAMES)
        return [element.text for element in elements]

    def is_sort_dropdown_visible(self) -> bool:
        """Check if the product sort dropdown is visible."""
        return self.is_element_visible(self.SORT_DROPDOWN)
