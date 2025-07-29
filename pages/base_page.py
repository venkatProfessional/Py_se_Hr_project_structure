import datetime
import json
import os

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, UnexpectedTagNameException, \
    NoAlertPresentException
import time

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def find_element(self, locator):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(locator)
        )
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


    def select_dropdown(self, element: WebElement, method: str = "text", option=None):
        """
        Selects an option in a <select> element using the specified method.

        Args:
            element (WebElement): The <select> dropdown WebElement.
            method (str): The selection strategy - "text", "value", or "index".
            option (str|int): The option to select.

        Raises:
            ValueError: If method is invalid or option is None.
            NoSuchElementException: If the dropdown or option is not found.
            UnexpectedTagNameException: If the element is not a <select>.
            usage
            self.select_dropdown(status_select_element, method="text", option="Active")
        """
        if not option and option != 0:
            raise ValueError("You must provide a non-null option to select.")

        try:
            select = Select(element)

            if method == "text":
                select.select_by_visible_text(str(option))
            elif method == "value":
                select.select_by_value(str(option))
            elif method == "index":
                select.select_by_index(int(option))
            else:
                raise ValueError(f"Unsupported selection method: {method}")

            print(f"✅ Selected '{option}' using method '{method}'.")

        except (NoSuchElementException, UnexpectedTagNameException) as e:
            print(f"❌ Dropdown selection failed: {e}")
            raise

    def handle_alert(self, action="accept", timeout=5, text=None):
        """
        Handles JavaScript alerts.

        Args:
            action (str): "accept", "dismiss", or "gettext".
            timeout (int): Maximum time to wait for alert.
            text (str): Optional text to send to prompt alerts.

        Returns:
            str: Alert text if action is "gettext", else None.

        Raises:
            NoAlertPresentException: If no alert is present.
            usage

        usage
         self.handle_alert(action="accept")

        """
        try:
            print("⏳ Waiting for alert to be present...")
            WebDriverWait(self.driver, timeout).until(EC.alert_is_present())

            alert = self.driver.switch_to.alert
            print("✅ Alert found.")

            if text:
                print(f"💬 Sending text to alert: {text}")
                alert.send_keys(text)

            if action == "accept":
                print("🔘 Accepting the alert...")
                alert.accept()
            elif action == "dismiss":
                print("🔘 Dismissing the alert...")
                alert.dismiss()
            elif action == "gettext":
                alert_text = alert.text
                print(f"📝 Alert text: {alert_text}")
                return alert_text
            else:
                raise ValueError(f"Unsupported alert action: {action}")

        except TimeoutException:
            print("❌ Alert did not appear within the timeout.")
            raise
        except NoAlertPresentException:
            print("❌ No alert present.")
            raise

    def take_screenshot(self, name_prefix="screenshot"):
        try:
            # Create folder path in project root
            folder = os.path.join(os.getcwd(), "error_screenshots")
            os.makedirs(folder, exist_ok=True)

            # Build filename with timestamp
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"{name_prefix}_{timestamp}.png"
            full_path = os.path.join(folder, filename)

            # Take screenshot
            success = self.driver.save_screenshot(full_path)
            if success:
                print(f"📸 Screenshot saved successfully at: {full_path}")
            else:
                print("⚠️ Screenshot capture failed.")
            return full_path

        except Exception as e:
            print(f"❌ Failed to save screenshot: {e}")
            return None

    def pause(self, seconds: float = 1.0, reason: str = "") -> None:
        """
        Pause execution for a specified number of seconds.

        Args:
            seconds (float): Duration to pause in seconds. Default is 1.0.
            reason (str): Optional reason for the pause, useful for logging/debugging.

        Returns:
            None
        """
        if reason:
            print(f"⏸️ Pausing for {seconds} seconds — {reason}")
        else:
            print(f"⏸️ Pausing for {seconds} seconds...")

        time.sleep(seconds)

        # ✅ Fix: Add 'file_path' parameter

    def read_employee_json(self):
        path = r"C:\Users\User\PycharmProjects\SmiligenceHrAdmin\data\employee_data.json"
        with open(path, "r", encoding="utf-8") as file:
            return json.load(file)

    def safe_select_dropdown(self, dropdown_element, option_text):
        try:
            select = Select(dropdown_element)
            select.select_by_visible_text(option_text)
        except Exception as e:
            print(f"⚠️ Option '{option_text}' not found, selecting first available option.")
            try:
                select.select_by_index(2)
            except:
                print("❌ Dropdown is empty or not interactable.")