from datetime import datetime
import json
import os
from pathlib import Path


import allure
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, UnexpectedTagNameException, \
    NoAlertPresentException, ElementNotInteractableException, WebDriverException, JavascriptException, \
    StaleElementReferenceException, ElementClickInterceptedException
import time

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)
        # self.remove_debug_bar()

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
        # Retrieve entered text
        entered_text = element.get_attribute("value")

        # Print confirmation message
        print(f"✅ Successfully entered text: '{entered_text}' in element located by {locator}")

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
            try:
                element.click()
                print(f"✅ Element clicked successfully: {locator}")
            except ElementClickInterceptedException:
                print(f"⚠️ Element present but could not be clicked: {locator}")
                self.driver.save_screenshot("wait_and_click_error.png")
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
        try:
            print(f"🔍 Waiting for element to be present: {locator}")
            element = self.wait.until(EC.presence_of_element_located(locator))

            print("📜 Scrolling to element...")
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

            if element.is_displayed():
                print("✅ Element is visible after scrolling.")
                return True
            else:
                print("❌ Element is present but not visible after scrolling.")
                return False

        except Exception as e:
            print(f"❌ Failed to scroll to element {locator}: {e}")
            return False

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

    def select2_select_option(self, select2_container_locator, option_text):
        """
        Select a single option from a Select2 dropdown.

        :param select2_container_locator: A tuple locator (By.XPATH, "...") for the Select2 container <span>
        :param option_text: The visible text of the option to select (must be a string)
        """
        try:
            print(f"[🔍] Clicking Select2 container: {select2_container_locator}")
            container = self.wait.until(EC.element_to_be_clickable(select2_container_locator))
            container.click()

            print(f"[⌨️] Typing and selecting: {option_text}")
            input_box = self.wait.until(
                EC.presence_of_element_located((By.XPATH, "//input[contains(@class,'select2-search__field')]"))
            )
            input_box.clear()
            input_box.send_keys(str(option_text))  # Ensures it's a string
            input_box.send_keys(Keys.ENTER)

            print(f"[✔] Selected: {option_text}")
        except Exception as e:
            print(f"[❌] Error selecting '{option_text}': {e}")

    def select2_select_multiple_options(self, select2_container_locator, options_list):
        """
        Select multiple options from a Select2 dropdown.

        :param select2_container_locator: A tuple locator (By.XPATH, "...") for the Select2 container <span>
        :param options_list: A list of strings to select
        """
        if not isinstance(options_list, list):
            raise TypeError("options_list must be a list of strings.")

        for option in options_list:
            self.select2_select_option(select2_container_locator, option)

    def select2_clear_selected_options(self):
        """
        Clicks the 'clear all' button in Select2 dropdown if available.
        """
        try:
            clear_btn = self.driver.find_element(By.CLASS_NAME, "select2-selection__clear")
            clear_btn.click()
            print("[✔] Cleared all selected options.")
        except:
            print("[ℹ] Clear button not found or nothing to clear.")

    def set_checkbox_state(self, checkbox_locator, should_be_checked=True):
        """
        Set the checkbox to a desired state (checked or unchecked).

        :param checkbox_locator: Tuple (By.XPATH, "xpath") or (By.ID, "id")
        :param should_be_checked: True to check, False to uncheck
        """
        try:
            checkbox = self.wait.until(EC.element_to_be_clickable(checkbox_locator))
            is_checked = checkbox.is_selected()

            print(f"[🔎] Checkbox current state: {'checked' if is_checked else 'unchecked'}")
            print(f"[✅] Desired state: {'checked' if should_be_checked else 'unchecked'}")

            if should_be_checked and not is_checked:
                checkbox.click()
                print("[☑] Checkbox has been checked.")
            elif not should_be_checked and is_checked:
                checkbox.click()
                print("[🔲] Checkbox has been unchecked.")
            else:
                print("[ℹ] Checkbox already in desired state. No action taken.")
        except Exception as e:
            print(f"[❌] Error while setting checkbox state: {e}")

    def is_text_visible_on_page(self, text, timeout=10):
        """
        Check if any element containing the given text is visible on the page.

        :param text: The text to search for on the page.
        :param timeout: Maximum wait time in seconds.
        :return: True if text is found and visible, False otherwise.
        """
        xpath =  f"//*[contains(.,'{text}')]"
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located((By.XPATH, xpath))
            )
            print(f"Text '{text}' is visible on the page.")
            return True
        except Exception:
            print(f"Text '{text}' is NOT visible on the page.")
            return False

    def scroll_and_click(self, identifier, by="text", direction="vertical", timeout=10):
        """
        Scroll in the given direction to the element and click it.

        :param identifier: The visible text or XPath of the element.
        :param by: "text" (default) or "xpath"
        :param direction: "vertical", "horizontal", or "both"
        :param timeout: Timeout in seconds
        """
        try:
            if by == "text":
                xpath = f"//*[contains(text(), '{identifier}')]"
            elif by == "xpath":
                xpath = identifier
            else:
                raise ValueError("Parameter 'by' must be 'text' or 'xpath'")

            # Wait for element to appear
            element = self.wait.until(EC.presence_of_element_located((By.XPATH, xpath)))

            # Choose scroll direction
            scroll_script = {
                "vertical": "arguments[0].scrollIntoView({block: 'center'});",
                        "horizontal": "arguments[0].scrollIntoView({inline: 'center'});",
                "both": "arguments[0].scrollIntoView({block: 'center', inline: 'center'});"
            }

            script = scroll_script.get(direction.lower())
            if not script:
                raise ValueError("Invalid direction. Use 'vertical', 'horizontal', or 'both'.")

            # Scroll
            self.driver.execute_script(script, element)

            # Wait for clickable
            self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))

            # Click
            element.click()
            print(f"✅ Clicked element with {by}: {identifier}")
            return  True

        except Exception as e:
            print(f"❌ Failed to click element with {by} '{identifier}': {e}")
            return False

    def scroll_and_find(self, identifier, by="text", direction="vertical", timeout=10, poll_frequency=0.5):
        """
        Scroll until element is found or timeout occurs.
        """
        try:
            # Build XPath
            if by == "text":
                xpath = f"//*[contains(text(), '{identifier}')]"
            elif by == "xpath":
                xpath = identifier
            else:
                raise ValueError("Parameter 'by' must be 'text' or 'xpath'")

            scroll_script = {
                "vertical": "arguments[0].scrollIntoView({block: 'center'});",
                "horizontal": "arguments[0].scrollIntoView({inline: 'center'});",
                "both": "arguments[0].scrollIntoView({block: 'center', inline: 'center'});"
            }
            script = scroll_script.get(direction.lower())
            if not script:
                raise ValueError("Invalid direction. Use 'vertical', 'horizontal', or 'both'.")

            end_time = time.time() + timeout  # Python-based timer

            while time.time() < end_time:
                try:
                    elements = self.driver.find_elements(By.XPATH, xpath)
                    if elements:
                        element = elements[0]
                        self.driver.execute_script(script, element)
                        print(f"✅ Found element with {by}: {identifier}")
                        return element

                    # Scroll slightly if not found
                    if direction.lower() in ["vertical", "both"]:
                        self.driver.execute_script("window.scrollBy(0, 300);")
                    if direction.lower() in ["horizontal", "both"]:
                        self.driver.execute_script("window.scrollBy(300, 0);")

                except (NoSuchElementException, StaleElementReferenceException):
                    pass

                time.sleep(poll_frequency)  # short delay

            print(f"❌ Element with {by} '{identifier}' not found in {timeout} seconds")
            return None

        except Exception as e:
            print(f"❌ Error in scroll_and_find: {e}")
            return None

    def verify_pdf_downloaded(self, expected_filename=None, timeout=15, download_dir=None):
        """
        Verifies that a PDF file is downloaded within a timeout.

        :param expected_filename: If known, pass the exact file name (e.g., "report.pdf")
        :param timeout: Max wait time (in seconds) for the download
        :param download_dir: Folder where the file is expected to download
        :return: True if file found, False otherwise
        """
        if download_dir is None:
            download_dir = os.path.join(os.path.expanduser("~"), "Downloads")

        print(f"🔍 Waiting for PDF download in: {download_dir}")
        print(f"⏳ Timeout: {timeout} seconds")

        end_time = time.time() + timeout
        while time.time() < end_time:
            files = os.listdir(download_dir)
            pdf_files = [f for f in files if f.endswith(".pdf")]

            if expected_filename:
                if expected_filename in pdf_files:
                    print(f"✅ PDF '{expected_filename}' downloaded.")
                    return True
            else:
                if pdf_files:
                    latest = max(
                        [os.path.join(download_dir, f) for f in pdf_files],
                        key=os.path.getctime
                    )
                    print(f"✅ PDF downloaded: {os.path.basename(latest)}")
                    return True

            time.sleep(1)

        print("❌ PDF download failed or timed out.")
        return False

    def verify_file_downloaded(self, expected_filename=None, file_extension=None, timeout=15, download_dir=None):
        """
        Verifies if the latest matching file is downloaded within the given timeout.

        - If expected_filename is given → partial match (contains), case-insensitive.
        - If file_extension is given → matches extension (with or without filename).
        - Picks the most recently downloaded matching file.

        :param expected_filename: Partial file name to check (e.g., 'attendance')
        :param file_extension: File extension to check (e.g., 'pdf', 'xlsx')
        :param timeout: Max wait time in seconds
        :param download_dir: Download folder (default: system Downloads)
        :return: Path of the latest matching file, else None
        """
        if download_dir is None:
            download_dir = str(Path.home() / "Downloads")

        if file_extension:
            file_extension = file_extension.lower().lstrip('.')  # normalize extension

        print(f"🔍 Checking for latest downloaded file in: {download_dir}")
        print(f"⏳ Waiting up to {timeout} seconds")
        if expected_filename:
            print(f"📄 Looking for filename containing: {expected_filename}")
        if file_extension:
            print(f"📑 Expected file extension: .{file_extension}")

        end_time = time.time() + timeout

        while time.time() < end_time:
            matching_files = []

            for file in os.listdir(download_dir):
                file_path = os.path.join(download_dir, file)

                # Skip incomplete downloads
                if file.endswith(".crdownload") or file.endswith(".part"):
                    continue

                # Mode 1: Only filename given (partial match)
                if expected_filename and not file_extension:
                    if expected_filename.lower() in file.lower():
                        matching_files.append(file_path)

                # Mode 2: Filename + extension
                elif expected_filename and file_extension:
                    if expected_filename.lower() in file.lower() and file.lower().endswith(f".{file_extension}"):
                        matching_files.append(file_path)

                # Mode 3: Only extension given
                elif file_extension and not expected_filename:
                    if file.lower().endswith(f".{file_extension}"):
                        matching_files.append(file_path)

            # If we found any matching files, pick the latest
            if matching_files:
                latest_file = max(matching_files, key=os.path.getmtime)
                print(f"✅ Latest matching file found: {os.path.basename(latest_file)}")
                return latest_file

            time.sleep(1)

        print("❌ File not found within timeout.")
        return None

    def handle_popup_and_click(self, popup_locator, button_locator, timeout=10):
        """
        Waits for a popup to be visible, then clicks the specified button inside it.

        :param popup_locator: tuple (By, value) for the popup container
        :param button_locator: tuple (By, value) for the button inside the popup
        :param timeout: seconds to wait for the popup
        """
        try:
            print("⏳ Waiting for popup to appear...")
            popup = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(popup_locator)
            )
            print("✅ Popup is visible.")

            print("👉 Clicking button inside popup...")
            button = popup.find_element(*button_locator)
            button.click()
            print("✅ Button clicked successfully.")

        except TimeoutException:
            print("❌ Popup did not appear in time.")
            return False
        except Exception as e:
            print(f"⚠️ Error interacting with popup: {str(e)}")
            return False
        return True

    def check_current_url(self, expected_url_part: str, timeout: int = 10) -> bool:
        """
        Waits for the current URL to contain the expected URL part.
        Returns True if matched, False otherwise.
        """
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC

        print(f"🔍 Waiting for URL to contain: '{expected_url_part}'")
        try:
            WebDriverWait(self.driver, timeout).until(
                lambda driver: expected_url_part in driver.current_url
            )
            print(f"✅ URL matched: {self.driver.current_url}")
            return True
        except Exception as e:
            print(f"❌ URL did not match within {timeout} seconds. Current URL: {self.driver.current_url}")
            return False

    def upload_file(self, file_input_locator, file_path):
        """Uploads a file using the <input type='file'> element, with proper exception handling."""
        try:
            absolute_path = os.path.abspath(file_path)

            if not os.path.isfile(absolute_path):
                print(f"❌ File does not exist: {absolute_path}")
                return False

            print(f"📤 Uploading file: {absolute_path}")
            input_element = self.driver.find_element(*file_input_locator)
            input_element.send_keys(absolute_path)
            print("✅ File upload triggered successfully.")
            return True

        except NoSuchElementException:
            print("❌ File input element not found.")
        except ElementNotInteractableException:
            print("❌ File input element is not interactable (maybe hidden or disabled).")
        except TimeoutException:
            print("⏳ Timed out while trying to find or interact with the file input element.")
        except WebDriverException as e:
            print(f"🚨 WebDriver error during file upload: {str(e)}")
        except Exception as e:
            print(f"⚠️ Unexpected error during file upload: {str(e)}")

        return False  # In case of failure

    def wait_until_clickable(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )

    def enter_date(self, locator, value, input_format=None, send_format="%Y-%m-%d", clear_first=True, wait_time=10):
        print(f"[🔍] Raw input value: {value}")

        # Convert input value to datetime object
        if isinstance(value, str):
            if input_format:
                try:
                    date_obj = datetime.strptime(value, input_format)
                    print(f"[✅] Parsed datetime object: {date_obj}")
                except Exception as e:
                    print(f"[❌] Error parsing date with format {input_format}: {e}")
                    return
            else:
                print("[❌] input_format is required for string values.")
                return
        elif isinstance(value, datetime):
            date_obj = value
            print(f"[✅] datetime object provided directly: {date_obj}")
        else:
            print("[❌] Invalid value type. Must be str or datetime.")
            return

        formatted_date = date_obj.strftime(send_format)
        print(f"[📤] Final date to send: {formatted_date}")

        # Wait for element and enter date
        try:
            wait = WebDriverWait(self.driver, wait_time)
            elem = wait.until(EC.element_to_be_clickable(locator))
            if clear_first:
                elem.clear()
            elem.send_keys(formatted_date)
            print("[✅] Date entered successfully.")
        except TimeoutException:
            print("[❌] Element was not clickable within the wait time.")
        except Exception as e:
            print(f"[❌] Could not send date to input field: {e}")

    def select_dropdown_option(self, locator, value=None, text=None, index=None):
        """
        Select an option from a <select> dropdown by value, visible text, or index.
        """
        try:
            element = self.find_element(locator)
            dropdown = Select(element)

            if value is not None:
                dropdown.select_by_value(value)
                print(f"✅ Selected by value: {value}")
            elif text is not None:
                dropdown.select_by_visible_text(text)
                print(f"✅ Selected by visible text: {text}")
            elif index is not None:
                dropdown.select_by_index(index)
                print(f"✅ Selected by index: {index}")
            else:
                raise ValueError("Please provide value, text, or index for dropdown selection.")

        except NoSuchElementException:
            print(f"❌ No option found with visible text: {text} (Locator: {locator})")
            self.capture_screenshot(f"dropdown_not_found_{text.replace(' ', '_')}.png")

        except UnexpectedTagNameException:
            print(f"❌ The element is not a <select> tag for locator: {locator}")
            self.capture_screenshot("unexpected_tag_dropdown_error.png")

        except Exception as e:
            print(f"❌ An unexpected error occurred: {e}")
            self.capture_screenshot("unexpected_dropdown_error.png")

    def click_by_visible_text(self, text, timeout=10):
        """
        Clicks an element using its exact visible text.
        """
        try:
            print(f"🔍 Looking for element with text: '{text}'")
            xpath = f"//*[normalize-space(text())='{text}']"
            element = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable((By.XPATH, xpath))
            )
            element.click()
            print(f"✅ Clicked on element with text: '{text}'")
        except Exception as e:
            print(f"❌ Failed to click element with text '{text}': {e}")
            raise

    def capture_screenshot(self, name="error_screenshot.png"):
        """Captures a screenshot with the given name."""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{timestamp}_{name}"
        path = os.path.join(os.getcwd(), "screenshots", filename)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        self.driver.save_screenshot(path)
        print(f"📸 Screenshot saved: {path}")

    def select_by_visible_text__(self, locator, visible_text, print_all_options=False):
        """
        Selects a dropdown option by visible text.
        Optionally prints available options for debugging if print_all_options=True.
        """
        try:
            element = self.find_element(locator)
            select = Select(element)

            # Debug: List all options if requested
            if print_all_options:
                options = [opt.text.strip() for opt in select.options]
                print("📋 Available dropdown options:", options)

            # Attempt to select
            select.select_by_visible_text(visible_text)
            print(f"✅ Selected option: '{visible_text}'")

        except NoSuchElementException:
            print(f"❌ Dropdown not found for locator: {locator}")
        except UnexpectedTagNameException:
            print(f"❌ Element at locator {locator} is not a <select> tag.")
        except Exception as e:
            print(f"⚠️ Option '{visible_text}' not found or error occurred: {e}")
            try:
                if select.options:
                    first_option_text = select.options[0].text.strip()
                    select.select_by_index(0)
                    print(f"🔁 Fallback: Selected first available option: '{first_option_text}'")
                else:
                    print("❌ No options available in the dropdown to select.")
            except Exception as fallback_exception:
                print(f"❌ Failed fallback selection: {fallback_exception}")

    def toggle_switch(self, locator, target_state="on"):
        """
        Toggle a switch to the desired state.

        Args:
            locator (tuple): (By.XPATH, "your_xpath") or any other locator
            target_state (str): "on" or "off"
        """
        toggle = self.wait_until_visible(locator)

        # Determine current state
        current_class = toggle.get_attribute("class").lower()

        is_on = "on" in current_class or "active" in current_class or "checked" in current_class

        if (target_state.lower() == "on" and not is_on) or (target_state.lower() == "off" and is_on):
            toggle.click()
            print(f"[🔁] Toggled to {target_state.upper()}")
        else:
            print(f"[✅] Toggle already in desired state: {target_state.upper()}")

    def handle_load_test_data_from_json(self, file_path, callback_function):
        import json
        import os

        if not os.path.exists(file_path):
            raise FileNotFoundError(f"JSON file not found: {file_path}")

        entries = []

        with open(file_path, 'r') as file:
            try:
                # Try loading as a whole: works for array or dict
                data = json.load(file)
                if isinstance(data, dict):
                    entries = [data]
                else:
                    entries = data
            except json.JSONDecodeError:
                # If fails, try line-by-line (NDJSON)
                file.seek(0)
                for line in file:
                    if line.strip():
                        try:
                            entry = json.loads(line)
                            entries.append(entry)
                        except json.JSONDecodeError:
                            continue  # Or handle/log error as needed

        for entry in entries:
            print(f"[📋] Running test with entry: {entry}")
            callback_function(entry)

    def remove_debug_bar(self):
        try:
            # Wait for presence of the debug bar element in the DOM (not necessarily visible)
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".phpdebugbar"))
            )
            # Execute JS to remove debug bar and resize handle
            self.driver.execute_script("""
                let bar = document.querySelector('.phpdebugbar');
                if (bar) bar.remove();

                let resize = document.querySelector('.phpdebugbar-resize-handle');
                if (resize) resize.remove();
            """)
            print("✅ Debug bar found and removed.")
        except TimeoutException:
            print("⚠️ Debug bar not found or already removed.")
        except JavascriptException as js_err:
            print(f"⚠️ JavaScript error occurred while removing debug bar: {js_err}")
        except Exception as e:
            print(f"⚠️ Unexpected error while removing debug bar: {e}")

    def load_json_data_robust(json_path):
        """
        Loads JSON data from a file with complete error handling.

        :param json_path: Path to the JSON file.
        :return: Parsed JSON data (dict or list) or None if failed.
        """
        try:
            if not json_path or not isinstance(json_path, str):
                print("❌ Invalid path: Must be a non-empty string.")
                return None

            if not os.path.exists(json_path):
                print(f"❌ File not found: {json_path}")
                return None

            if not json_path.lower().endswith(".json"):
                print("❌ Invalid file type: Expected a .json file.")
                return None

            with open(json_path, "r", encoding="utf-8") as f:
                content = f.read().strip()
                if not content:
                    print("❌ File is empty.")
                    return None
                try:
                    data = json.loads(content)
                except json.JSONDecodeError as e:
                    print(f"❌ JSON decoding error: {e}")
                    return None

            if not isinstance(data, (dict, list)):
                print(f"❌ Invalid JSON structure. Expected dict or list but got {type(data).__name__}")
                return None

            print("✅ JSON data loaded successfully.")
            return data

        except Exception as e:
            print(f"❌ Unexpected error occurred while loading JSON: {e}")
            return None

    def select_radio_button(self, locator, value=None, by='name', timeout=10, poll_frequency=0.5):
        """
        Robustly select a radio button given a locator and optionally a value within a radio group.

        :param locator: The locator string (e.g., name or XPath or ID) to identify the radio buttons.
                        If by='xpath' or 'css selector', should point directly to radio buttons.
                        If by='name' or 'id', will find all radios with that attribute.
        :param value: (Optional) The value attribute of the radio button to select in a group.
                      If None and multiple radios exist, selects the first.
        :param by: Locator type - 'id', 'name', 'xpath', 'css selector'. Default is 'name'.
        :param timeout: Maximum seconds to wait for radio buttons to be clickable.
        :param poll_frequency: Time interval between retries while waiting.
        :return: True if selection succeeded, False otherwise.
        """

        try:
            wait = WebDriverWait(self.driver, timeout, poll_frequency)

            # Locate radio button(s)
            if by.lower() in ['id', 'name']:
                # Usually radio buttons are grouped by name, so find all with that name or by id (rare)
                radios = wait.until(EC.presence_of_all_elements_located((getattr(By, by.upper()), locator)))
                if not radios:
                    print(f"❌ No radio buttons found with {by}='{locator}'")
                    return False
                # If value specified, find matching value attribute
                if value is not None:
                    target_radio = None
                    for rb in radios:
                        rb_value = rb.get_attribute('value')
                        if rb_value == value:
                            target_radio = rb
                            break
                    if not target_radio:
                        print(f"❌ No radio button with value='{value}' found in group {by}='{locator}'")
                        return False
                else:
                    # No value specified, pick first radio button
                    target_radio = radios[0]
            elif by.lower() in ['xpath', 'css selector']:
                # When locator targets single radio button directly via xpath/css
                target_radio = wait.until(EC.element_to_be_clickable((getattr(By, by.upper()), locator)))
            else:
                print(f"❌ Unsupported locator type '{by}'")
                return False

            # Scroll into view (optional)
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", target_radio)

            # Click the radio button if not already selected
            if not target_radio.is_selected():
                wait.until(EC.element_to_be_clickable(target_radio))
                target_radio.click()

            # Verify selection
            if target_radio.is_selected():
                print(
                    f"✅ Radio button selected successfully: {by}='{locator}'" + (f", value='{value}'" if value else ''))
                return True
            else:
                print(
                    f"❌ Failed to select the radio button: {by}='{locator}'" + (f", value='{value}'" if value else ''))
                return False

        except (NoSuchElementException, StaleElementReferenceException, TimeoutException) as e:
            print(f"❌ Exception occurred while selecting radio button: {e}")
            return False

    def select_calendar_date(
            self,
            target_date,
            calendar_root_xpath,
            month_label_xpath=".//span[contains(@class,'month') or contains(text(),'August')]",
            year_label_xpath=".//span[contains(@class,'year')]",
            prev_btn_xpath=".//button[contains(@class,'Prev') or contains(text(),'Prev')]",
            next_btn_xpath=".//button[contains(@class,'Next') or contains(text(),'Next')]",
            day_cell_xpath=".//td[not(contains(@class,'disabled')) and text()='%d']",
            timeout=10
    ):
        """
        Select a date in a popup calendar widget.
        Parameters:
            self                 : Your class instance with self.driver
            target_date          : The date to select. Accepts 'YYYY-MM-DD' string or datetime.date
            calendar_root_xpath  : XPath for calendar root/container (for context)
            *_label_xpath        : XPath for month/year navigation labels (relative to root)
            *_btn_xpath          : XPath for prev/next month navigation buttons (relative to root)
            day_cell_xpath       : XPath pattern for day cell, use %d for the day (relative to root)
            timeout              : Timeout for all waits
        Returns:
            True on success. False otherwise.
        """
        # 1. Parse the date
        if isinstance(target_date, str):
            target = datetime.datetime.strptime(target_date, "%Y-%m-%d").date()
        elif isinstance(target_date, datetime.date):
            target = target_date
        else:
            print(f"❌ Invalid target_date: {target_date}")
            return False

        try:
            wait = WebDriverWait(self.driver, timeout)
            # 2. Focus calendar root only: all lookups are relative to the open calendar
            root = wait.until(EC.visibility_of_element_located((By.XPATH, calendar_root_xpath)))
            # 3. Find displayed month and year
            month_label = root.find_element(By.XPATH, month_label_xpath)
            year_label = root.find_element(By.XPATH, year_label_xpath)
            # Month names for parsing
            months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
                      "November", "December"]

            def get_displayed_month_year():
                month_text = month_label.text.strip()
                year_text = year_label.text.strip()
                # Safe conversion for "August 2025"
                try:
                    month_idx = months.index(month_text) + 1
                except Exception:
                    month_idx = None
                try:
                    year_idx = int(year_text)
                except Exception:
                    year_idx = None
                return month_idx, year_idx

            # 4. Navigate to correct month/year
            max_steps = 24  # Prevent infinite loop
            while max_steps > 0:
                disp_month, disp_year = get_displayed_month_year()
                if disp_month == target.month and disp_year == target.year:
                    break
                elif (disp_year, disp_month) < (target.year, target.month):
                    next_btn = root.find_element(By.XPATH, next_btn_xpath)
                    next_btn.click()
                else:
                    prev_btn = root.find_element(By.XPATH, prev_btn_xpath)
                    prev_btn.click()
                # Re-fetch current month and year
                wait.until(lambda d: get_displayed_month_year() != (disp_month, disp_year))
                max_steps -= 1
            if max_steps == 0:
                print("❌ Calendar navigation failed to reach the target month/year")
                return False

            # 5. Click on the day cell
            day_xpath = day_cell_xpath % target.day
            day_cell = wait.until(EC.element_to_be_clickable(
                (By.XPATH, f"{calendar_root_xpath}{day_xpath if day_xpath.startswith('/') else '/' + day_xpath}")))
            day_cell.click()
            print(f"✅ Selected date: {target}")
            return True

        except (TimeoutException, NoSuchElementException) as e:
            print(f"❌ Failed to select date {target_date}: {e}")
            return False
        except Exception as e:
            print(f"❌ Unexpected error selecting date: {e}")
            return False

    def robust_select_dropdown_option(self, locator, text=None, index=None, timeout=10):
        from selenium.webdriver.support.ui import Select
        from selenium.common.exceptions import NoSuchElementException, TimeoutException
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC

        try:
            dropdown_element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
            select = Select(dropdown_element)

            if text:
                try:
                    select.select_by_visible_text(text)
                    print(f"✅ Selected by text: '{text}'")
                    return
                except NoSuchElementException:
                    print(f"⚠️ Option '{text}' not found, falling back to index if provided...")

            if index is not None:
                try:
                    select.select_by_index(index)
                    print(f"✅ Selected by index: {index}")
                    return
                except NoSuchElementException:
                    raise Exception(f"❌ Index {index} not found in dropdown options.")

            raise Exception("❌ No valid option found. Provide a correct visible text or index.")

        except TimeoutException:
            raise Exception(f"❌ Dropdown {locator} not found within {timeout} seconds.")

    def get_attribute_value(self, locator, attribute_name):
        """
        Get the value of an attribute from the element located by `locator`.

        Args:
            locator (tuple): Selenium locator tuple, e.g., (By.ID, "element_id")
            attribute_name (str): The attribute name whose value is to be fetched

        Returns:
            str: The value of the attribute

        Raises:
            TimeoutException: If element is not found within timeout
            NoSuchElementException: If element is not found in DOM
            Exception: For other unexpected errors
        """
        try:
            element = WebDriverWait(self.driver, self.timeout).until(
                EC.presence_of_element_located(locator)
            )
            value = element.get_attribute(attribute_name)
            return value
        except TimeoutException:
            raise TimeoutException(f"Timed out waiting for element {locator} to get attribute '{attribute_name}'")
        except NoSuchElementException:
            raise NoSuchElementException(f"Element not found {locator} when fetching attribute '{attribute_name}'")
        except Exception as e:
            raise Exception(f"Failed to get attribute '{attribute_name}' from element {locator}: {e}")



