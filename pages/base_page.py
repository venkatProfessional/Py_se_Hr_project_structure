from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    # Basic click method
    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    # Input text into textbox
    def enter_text(self, locator, text):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.clear()
        element.send_keys(text)

    # Wait until element is visible
    def wait_until_visible(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def wait(seconds=2):
        print(f"Waiting for {seconds} second(s)...")
        time.sleep(seconds)

    # Wait until element is present in the DOM (not necessarily visible)
    def wait_until_present(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def wait_and_click(self, locator, timeout=10):
        try:
            # Wait until the element is present in DOM
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )

            # Scroll into view only if not displayed
            if not element.is_displayed():
                self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

            # Now wait until it's clickable
            WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(locator)
            )
            element.click()
        except TimeoutException:
            print(f"⚠️ Timeout: Element {locator} not clickable or not visible.")
            self.driver.save_screenshot("wait_and_click_error.png")
    # Select dropdown by visible text
    def select_dropdown_by_text(self, locator, text):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        Select(element).select_by_visible_text(text)

    # Select dropdown by index
    def select_dropdown_by_index(self, locator, index):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        Select(element).select_by_index(index)

    # Scroll to element
    def scroll_to_element(self, locator):
        element = self.wait.until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    # Navigate to a specific URL
    def go_to_url(self, url):
        self.driver.get(url)

    # Get current page title
    def get_title(self):
        return self.driver.title

    # Get current URL
    def get_current_url(self):
        return self.driver.current_url

    # Accept alert if present
    def accept_alert(self):
        try:
            alert = self.wait.until(EC.alert_is_present())
            alert.accept()
        except TimeoutException:
            print("No alert to accept.")

    # Dismiss alert if present
    def dismiss_alert(self):
        try:
            alert = self.wait.until(EC.alert_is_present())
            alert.dismiss()
        except TimeoutException:
            print("No alert to dismiss.")

    # Switch to frame by locator
    def switch_to_frame(self, locator):
        iframe = self.wait.until(EC.frame_to_be_available_and_switch_to_it(locator))
        return iframe

    # Switch to default content (main page)
    def switch_to_default(self):
        self.driver.switch_to.default_content()

    # Switch to new window/tab
    def switch_to_new_window(self):
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[-1])

    def is_element_visible(self, locator, timeout=5):
        """Check if element is visible within timeout."""
        try:
            WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def is_element_visible_with_text(self, locator, text):
        try:
            element = self.wait.until(EC.visibility_of_element_located(locator))
            return text in element.text
        except:
            return False

    # Capture screenshot (useful for debugging)
    def take_screenshot(self, file_name):
        self.driver.save_screenshot(file_name)

    # Wait for specific seconds (not recommended but useful sometimes)
    def wait_for(self, seconds):
        time.sleep(seconds)

    # Navigate back in browser history
    def navigate_back(self):
        self.driver.back()

    # Navigate forward in browser history
    def navigate_forward(self):
        self.driver.forward()

    def slow_typing(self, locator, text, delay=0.1):
        element = self.driver.find_element(*locator)
        element.clear()
        for char in text:
            element.send_keys(char)
            time.sleep(delay)

    def is_element_present(self, by_locator):
        """
        Check if the element is present in the DOM.
        Returns True if found, else False.
        """
        try:
            self.driver.find_element(*by_locator)
            return True
        except NoSuchElementException:
            return False