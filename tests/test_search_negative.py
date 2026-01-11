import allure
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


@allure.feature("Search")
@allure.story("Negative Search Results")
@allure.severity(allure.severity_level.MINOR)
def test_search_non_existent_product(driver):
    home_page = HomePage(driver)

    with allure.step("Navigate to Home Page"):
        driver.get("www.floroz.co.il")

    with allure.step("Search for a non-existent item"):
        home_page.search_for_product("ZZZ123###")

    with allure.step("Verify 'No Results' message is displayed"):
        not_found_msg = driver.find_element(By.CSS_SELECTOR, ".message.notice").text
        assert "לא נמצאו מוצרים" in not_found_msg

