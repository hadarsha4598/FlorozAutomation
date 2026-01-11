import allure
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


@allure.feature("Catalog Logic")
@allure.story("Price Sorting")
@allure.severity(allure.severity_level.MINOR)
def test_sort_price_low_to_high(driver):
    with allure.step("Open Flowers Category Page"):
        driver.get("www.floroz.co.il")

    with allure.step("Sort by price: Low to High"):
        sort_dropdown = Select(driver.find_element(By.ID, "sorter"))
        sort_dropdown.select_by_value("price")
        time.sleep(2)

    with allure.step("Extract prices of the first two products"):
        prices = driver.find_elements(By.CSS_SELECTOR, ".price-wrapper .price")
        p1 = float(prices[0].text.replace("₪", "").replace(",", "").strip())
        p2 = float(prices[1].text.replace("₪", "").replace(",", "").strip())

    with allure.step(f"Verify sorting: {p1} <= {p2}"):
        assert p1 <= p2
