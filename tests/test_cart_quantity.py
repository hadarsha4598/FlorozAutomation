import allure
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


@allure.feature("Shopping Cart")
@allure.story("Update Quantity")
@allure.severity(allure.severity_level.NORMAL)
def test_update_product_quantity(driver):
    home_page = HomePage(driver)

    with allure.step("Navigate and add product"):
        driver.get("www.floroz.co.il")
        home_page.search_and_add("ורד")
        time.sleep(3)

    with allure.step("Navigate to Cart Page"):
        driver.get("www.floroz.co.ilcheckout/cart/")

    with allure.step("Change quantity to 2 and update"):
        qty_input = driver.find_element(By.CSS_SELECTOR, "input.qty")
        qty_input.clear()
        qty_input.send_keys("2")
        driver.find_element(By.CSS_SELECTOR, "button.update").click()
        time.sleep(2)

    with allure.step("Verify quantity reflects '2'"):
        updated_qty = driver.find_element(By.CSS_SELECTOR, "input.qty").get_attribute("value")
        assert updated_qty == "2"

