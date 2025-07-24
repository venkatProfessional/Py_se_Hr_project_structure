import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from pages.login_page import LoginPage
from utils.config_reader import read_config


@pytest.fixture(scope="function")
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    prefs = {"profile.default_content_setting_values.notifications": 2}
    options.add_experimental_option("prefs", prefs)

    # ✅ Correct way to pass service and options
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    driver.implicitly_wait(10)
    try:
        yield driver
    finally:
        driver.quit()

@pytest.fixture(scope="function")
def login(driver):
    config = read_config()
    login_page = LoginPage(driver)
    login_page.load(config["base_url"])
    login_page.login(config["username"], config["password"])
    return driver
