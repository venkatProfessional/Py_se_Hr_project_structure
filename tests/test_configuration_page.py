import time

import pytest
from selenium.common import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.ConfigurationPage import ConfigurationPage


@pytest.mark.usefixtures("driver", "login")
class TestConfigurationPage:

    def test_navigating_to_configuration_page(self, driver):
        configuration_page_obj = ConfigurationPage(driver)
        configuration_page_obj.navigate_to_configuration_page()

        # ✅ Verify we reached the correct URL
        current_url = configuration_page_obj.get_current_url()
        print(f"Current URL after navigation: {current_url}")
        assert "https://smiligencehr.itsfortesza.com/configs/business-profile" in current_url.lower(), \
            f"❌ Expected 'configuration' in URL but got {current_url}"

    def test_validating_submit(self, driver):
        configuration_page_obj = ConfigurationPage(driver)

        try:
            # Navigate to the configuration page
            configuration_page_obj.navigate_to_configuration_page()

            # Perform the submit action without changing data
            configuration_page_obj.validating_submit_without_changing_anydata()

            # Wait for the page to load or a success indicator (adjust as needed)
            time.sleep(2)  # Or use WebDriverWait for a specific element
            # Example: Wait for a success message or element
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "success_message_id")))  # Replace with actual ID

            # Check if 500 error is absent
            if "500" in driver.page_source or "SERVER ERROR" in driver.page_source:
                print("500 Server Error detected on the page.")
                raise AssertionError("Test failed due to 500 Server Error.")

            # Explicitly verify success (add your success criterion here)
            print("No 500 error detected, and submit action completed successfully.")
            # Example assertion: Check for a success element or message
            success_element = driver.find_element(By.ID, "success_message_id")  # Replace with actual ID
            assert success_element.is_displayed(), "Success message not displayed."

        except WebDriverException as e:
            print(f"Test failed due to a WebDriver exception: {str(e)}")
            if "500" in str(e) or "SERVER ERROR" in driver.page_source:
                print("Detected 500 Server Error. This is a server-side issue.")
            raise  # Re-raise the exception to fail the test
        except AssertionError as e:
            print(f"Assertion failed: {str(e)}")
            raise  # Re-raise to fail the test
        except Exception as e:
            print(f"Unexpected error occurred: {str(e)}")
            raise

    def test_validating_on_updating_values_and_submit(self, driver):
        configuration_page_obj = ConfigurationPage(driver)

        try:
            # Navigate to the configuration page
            configuration_page_obj.navigate_to_configuration_page()

            # Perform the validation and submit with updated values
            configuration_page_obj.validating_on_updating_values_and_submit()

            # Wait for page to load or error to appear
            time.sleep(2)  # Consider using WebDriverWait instead
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), '500')]")))

            # Check for 500 error
            if "500" in driver.page_source or "SERVER ERROR" in driver.page_source:
                print("500 Server Error detected on the page.")
                raise AssertionError("Test failed due to 500 Server Error.")

            print("Test completed successfully with updated values and submit.")

        except WebDriverException as e:
            print(f"Test failed due to a WebDriver exception: {str(e)}")
            if "500" in str(e) or "SERVER ERROR" in driver.page_source:
                print("Detected 500 Server Error. This is a server-side issue.")
            raise  # Re-raise to fail the test
        except AssertionError as e:
            print(f"Assertion failed: {str(e)}")
            raise  # Re-raise to fail the test
        except Exception as e:
            print(f"Unexpected error occurred: {str(e)}")
            raise







