from selenium.webdriver.common.by import By
from .base_page import BasePage

class HomePage(BasePage):
    SEARCH_BAR = (By.NAME, "q")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    FIRST_PRODUCT = (By.CSS_SELECTOR, ".product-item-info")
    ADD_TO_CART_BTN = (By.ID, "product-addtocart-button")
    CART_COUNT = (By.CLASS_NAME, "counter-number")

    def search_for_product(self, product_name):
        self.type(self.SEARCH_BAR, product_name)
        self.click(self.SEARCH_BUTTON)

    def add_first_product_to_cart(self):
        self.click(self.FIRST_PRODUCT)
        self.click(self.ADD_TO_CART_BTN)

    def get_cart_count(self):
        return self.find(self.CART_COUNT).text
