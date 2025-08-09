import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

from pages.login_page import LoginPage
from utils.config_reader import read_config


@pytest.fixture(scope="function")
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")

    # ✅ Disable browser notifications
    prefs = {"profile.default_content_setting_values.notifications": 2}
    options.add_experimental_option("prefs", prefs)

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def login(driver):
    config = read_config()
    login_page = LoginPage(driver)
    login_page.load(config["base_url"])
    # Remove debug bar right after page load
    remove_debug_bar(driver)
    login_page.login(config["username"], config["password"])
    return driver

def remove_debug_bar(driver):
    """Remove PHP Debug Bar if present on the page."""
    try:
        WebDriverWait(driver, 2).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".phpdebugbar"))
        )
        driver.execute_script("""
            let bar = document.querySelector('.phpdebugbar');
            if (bar) bar.remove();

            let resize = document.querySelector('.phpdebugbar-resize-handle');
            if (resize) resize.remove();
        """)
        print("✅ Debug bar found and removed.")
    except Exception:
        # Suppress if debug bar not found or other error
        print("⚠️ Debug bar not found or already removed.")