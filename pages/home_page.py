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

from selenium.webdriver.common.by import By
from .base_page import BasePage


class HomePage(BasePage):
    # סלקטורים כלליים
    SEARCH_BAR = (By.NAME, "q")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    FIRST_PRODUCT = (By.CSS_SELECTOR, ".product-item-info")
    ADD_TO_CART_BTN = (By.ID, "product-addtocart-button")

    # סלקטורים לטופס צור קשר
    CONTACT_US_LINK = (By.LINK_TEXT, "צור קשר")
    SEND_BUTTON = (By.CSS_SELECTOR, "button.submit")
    ERROR_FIELD = (By.CSS_SELECTOR, ".mage-error")

    # סלקטורים לסל הקניות
    CART_ICON = (By.CLASS_NAME, "showcart")
    REMOVE_ITEM_BTN = (By.CSS_SELECTOR, ".action-delete")
    CONFIRM_REMOVE = (By.CSS_SELECTOR, ".action-primary.accept")
    EMPTY_CART_MSG = (By.CSS_SELECTOR, ".cart-empty")

    def search_and_add(self, product_name):
        self.type(self.SEARCH_BAR, product_name)
        self.click(self.SEARCH_BUTTON)
        self.click(self.FIRST_PRODUCT)
        self.click(self.ADD_TO_CART_BTN)
def search_and_add(self, product_name):
    self.type(self.SEARCH_BAR, product_name)
    self.click(self.SEARCH_BUTTON)
    # לחיצה על המוצר הראשון ברשימה
    self.click((By.CSS_SELECTOR, ".product-item-info"))
    # לחיצה על הוספה לסל בדף המוצר
    self.click((By.ID, "product-addtocart-button"))
