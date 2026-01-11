import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()


import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def driver(request):
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()

    yield driver

    # צילום מסך במקרה של כישלון בדיקה
    item = request.node
    if item.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(),
                      name="screenshot_on_failure",
                      attachment_type=allure.attachment_type.PNG)

    driver.quit()


# פונקציית עזר לניהול סטטוס הבדיקה (חובה עבור צילום המסך)
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
