import allure
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


@allure.feature("Shopping Cart")
@allure.story("Add and Remove Product")
@allure.severity(allure.severity_level.CRITICAL)
def test_add_and_remove_product(driver):
    home_page = HomePage(driver)

    with allure.step("Navigate to Home Page"):
        driver.get("www.floroz.co.il")

    with allure.step("Search and add product 'ורדים'"):
        home_page.search_and_add("ורדים")
        time.sleep(3)

    with allure.step("Remove product from mini-cart"):
        home_page.click(home_page.CART_ICON)
        home_page.click(home_page.REMOVE_ITEM_BTN)
        home_page.click(home_page.CONFIRM_REMOVE)

    with allure.step("Verify cart is empty"):
        driver.get("www.floroz.co.ilcheckout/cart/")
        empty_msg = home_page.find(home_page.EMPTY_CART_MSG)
        assert "אין לך פריטים" in empty_msg.text

