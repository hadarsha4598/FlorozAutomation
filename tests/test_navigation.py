import pytest
import allure
from selenium.webdriver.common.by import By


@allure.feature("Navigation")
@allure.story("Main Category Navigation")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.parametrize("category", ["מארזי שי", "עציצים", "זרים לראש"])
def test_category_navigation(driver, category):
    with allure.step(f"Navigate to Home Page"):
        driver.get("www.floroz.co.il")

    with allure.step(f"Click on category: {category}"):
        driver.find_element(By.LINK_TEXT, category).click()

    with allure.step(f"Verify page header (H1) matches {category}"):
        page_h1 = driver.find_element(By.TAG_NAME, "h1").text
        assert category.lower() in page_h1.lower()


