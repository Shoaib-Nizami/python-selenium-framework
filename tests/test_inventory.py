"""
Test suite for Inventory / Products page functionality.
Covers product listing, add to cart, sorting, and logout.
"""

import pytest
from config.config import Config


@pytest.mark.inventory
@pytest.mark.regression
class TestInventory:
    """Test cases for the inventory page."""

    @pytest.fixture(autouse=True)
    def login_first(self, login_page):
        """Login before each inventory test."""
        login_page.login(Config.VALID_USERNAME, Config.VALID_PASSWORD)

    def test_inventory_page_loads(self, inventory_page):
        """Test that the inventory page loads successfully after login."""
        assert inventory_page.is_on_inventory_page(),             "Inventory page should be displayed after successful login"

    def test_products_are_displayed(self, inventory_page):
        """Test that products are listed on the inventory page."""
        product_count = inventory_page.get_product_count()
        assert product_count > 0,             f"Expected products to be displayed, but found {product_count}"

    def test_add_product_to_cart(self, inventory_page):
        """Test adding a product to the shopping cart."""
        inventory_page.add_product_to_cart(index=0)
        cart_count = inventory_page.get_cart_count()
        assert cart_count == 1,             f"Expected cart count to be 1, but got {cart_count}"

    def test_add_multiple_products_to_cart(self, inventory_page):
        """Test adding multiple products to the cart."""
        inventory_page.add_product_to_cart(index=0)
        inventory_page.add_product_to_cart(index=1)
        cart_count = inventory_page.get_cart_count()
        assert cart_count == 2,             f"Expected cart count to be 2, but got {cart_count}"

    def test_product_names_are_visible(self, inventory_page):
        """Test that all product names are visible and not empty."""
        product_names = inventory_page.get_all_product_names()
        assert len(product_names) > 0, "Product names should be visible"
        for name in product_names:
            assert name.strip() != "", "Each product name should not be empty"

    def test_sort_dropdown_is_visible(self, inventory_page):
        """Test that the product sort dropdown is present."""
        assert inventory_page.is_sort_dropdown_visible(),             "Product sort dropdown should be visible"

    def test_logout_from_inventory(self, login_page, inventory_page):
        """Test logout functionality from the inventory page."""
        inventory_page.open_menu()
        inventory_page.click_logout()
        assert login_page.is_on_login_page(),             "User should be redirected to login page after logout"
