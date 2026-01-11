import allure
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


@allure.feature("Contact Us")
@allure.story("Mandatory Fields Validation")
@allure.severity(allure.severity_level.NORMAL)
def test_contact_form_validation(driver):
    home_page = HomePage(driver)

    with allure.step("Navigate to Contact page"):
        driver.get("www.floroz.co.il")

    with allure.step("Click send without filling details"):
        home_page.click(home_page.SEND_BUTTON)

    with allure.step("Verify error message is displayed"):
        error = home_page.find(home_page.ERROR_FIELD)
        assert error.is_displayed()
        assert "זהו שדה חובה" in error.text
