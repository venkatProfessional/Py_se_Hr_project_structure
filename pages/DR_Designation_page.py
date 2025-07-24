# designation_page.py
import time

from exceptiongroup import catch
from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage


class DesignationPage(BasePage):
    designation_roles_button = (By.XPATH, "//div[@data-i18n='Designation & Roles']")
    designation_drop_down = (By.XPATH, "//div[@data-i18n='Designation']")
    create_button = (By.XPATH, "//a[normalize-space()='Create']")
    designation_name = (By.XPATH, "//input[@id='name']")
    designation_description = (By.XPATH, "//textarea[@id='description']")
    submit_button = (By.XPATH, "//span[normalize-space()='Submit']")

    # ✅ Validation error locators
    # More reliable XPaths based on partial text match
    error_name_required = (By.XPATH, "//div[normalize-space()='The name field is required.']")
    error_description_required = (By.XPATH, "//div[normalize-space()='The description field is required.']")

    # success_message = (By.XPATH, "//div[@id='flashMessageMessage']")
    back_button = (By.XPATH, "//a[normalize-space()='Back']")

    # edit
    edit_button =(By.XPATH, "//tbody/tr[1]/td[6]/a[1]")
    edit_input = (By.XPATH, "//input[@id='name']")
    edit_description = (By.XPATH, "//textarea[@id='description']")
    edit_submit_button = (By.XPATH, "//span[normalize-space()='Submit']")

    def __init__(self, driver):
        super().__init__(driver)
        print("📄 Entered Designation Page")

    def handle_designation_page(self):
        self.wait_and_click(self.designation_roles_button)
        self.wait_and_click(self.designation_drop_down)

    def handle_create_designation(self, name="DEV", desc="test"):
        self.wait_and_click(self.create_button)
        self.enter_text(self.designation_name, name)
        self.enter_text(self.designation_description, desc)
        self.wait_and_click(self.submit_button)

    def submit_without_entering_data(self):
        self.wait_and_click(self.create_button)
        self.wait_and_click(self.submit_button)
        time.sleep(4)
        self.wait_and_click(self.back_button)

    def is_name_required_error_displayed(self) -> bool:
        """
        Checks if the 'name required' validation message is displayed.

        Returns:
            bool: True if the exact error text is found, False otherwise.
        """
        expected_text = "The name field is required."
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.error_name_required)
            )
            return element.text.strip() == expected_text
        except TimeoutException:
            print("⚠️ Timeout: 'Name required' error message not found.")
            return False

    def is_description_required_error_displayed(self) -> bool:
        """
        Checks if the 'description required' validation message is displayed.

        Returns:
            bool: True if the exact error text is found, False otherwise.
        """
        expected_text = "The description field is required."
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.error_description_required)
            )
            return element.text.strip() == expected_text
        except TimeoutException:
            print("⚠️ Timeout: 'Description required' error message not found.")
            return False

    def is_designation_created_successfully(self):
        return self.is_element_visible_with_text(self.success_message, "Designation Created")

    def handleedit(self):
        print("📝 Attempting to edit the item...")
        self.wait_and_click(self.edit_button)
        print("✅ Edit action performed.")
        self.slow_typing(self.edit_input, "Software Engineer")
        time.sleep(1)  # Give time for validation JS to process
        print("Updated a designation name")
        self.slow_typing(self.edit_description, "JuniorEngineer")
        time.sleep(1)
        print("description updated")
        self.wait_and_click(self.edit_submit_button)
        print("submit button in edit page is clicked")

    def handlemultipleedits(self):
        print("🛠️ Starting multiple edit operations...")

        try:
            # Locate all edit buttons
            edit_buttons = WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located((By.XPATH, "//tbody/tr/td[6]/a[1]"))
            )

            count = min(5, len(edit_buttons))
            print(f"🔍 Found {len(edit_buttons)} edit buttons, performing edit on first {count}.")

            for i in range(count):
                print(f"\n✏️ Editing row {i + 1} of {count}")

                # Refresh list to avoid stale references
                edit_buttons = self.driver.find_elements(By.XPATH, "//tbody/tr/td[6]/a[1]")
                self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", edit_buttons[i])
                edit_buttons[i].click()

                # Wait and enter new designation name (no spaces)
                WebDriverWait(self.driver, 10).until(
                    EC.visibility_of_element_located(self.edit_input)
                )
                name = f"SoftwareEngineer{i + 1}"
                self.enter_text(self.edit_input, name)
                print(f"📝 Name updated to: {name}")

                # Wait and enter new description (no spaces)
                WebDriverWait(self.driver, 10).until(
                    EC.visibility_of_element_located(self.edit_description)
                )
                description = f"JuniorEngineer{i + 1}"
                self.enter_text(self.edit_description, description)
                print(f"📝 Description updated to: {description}")

                # Submit changes
                self.wait_and_click(self.edit_submit_button)
                print("🚀 Submitted the edit form. Waiting for result...")

                time.sleep(1)  # Slow down to allow UI update

                # Retry if name invalid and form still open
                if self.is_element_present(self.edit_input):
                    print("⚠️ Name might be invalid or form still open. Re-submitting...")
                    self.wait_and_click(self.edit_submit_button)
                    time.sleep(1)

                else:
                    print("✅ Edit form submitted successfully.")

                # Wait for name to appear in table
                WebDriverWait(self.driver, 10).until(
                    EC.text_to_be_present_in_element(
                        (By.XPATH, f"//tbody/tr[{i + 1}]/td[1]"),
                        name
                    )
                )

        except TimeoutException:
            print("⚠️ Timeout occurred while locating elements.")
        except NoSuchElementException:
            print("❌ Some required elements were not found on the page.")

    def is_invalid_name_format_displayed(self):
        try:
            error_locator = (By.XPATH, "//div[contains(text(),'The name format is invalid.')]")
            element = WebDriverWait(self.driver, 3).until(
                EC.visibility_of_element_located(error_locator)
            )
            return element.is_displayed()
        except TimeoutException:
            return False

    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    import time

    def toggle_status_all_rows(self):
        print("🔁 Starting status toggle for all rows...")

        row_index = 0
        while True:
            try:
                # Wait for table to load
                WebDriverWait(self.driver, 10).until(
                    EC.presence_of_all_elements_located((By.XPATH, "//tbody/tr/td[6]/a[1]"))
                )
                edit_buttons = self.driver.find_elements(By.XPATH, "//tbody/tr/td[6]/a[1]")

                if row_index >= len(edit_buttons):
                    print("✅ All rows processed.")
                    break

                print(f"\n✏️ Editing row {row_index + 1} of {len(edit_buttons)}")
                # Re-fetch edit buttons (page reloads every time)
                edit_buttons = self.driver.find_elements(By.XPATH, "//tbody/tr/td[6]/a[1]")
                self.driver.execute_script("arguments[0].scrollIntoView(true);", edit_buttons[row_index])
                edit_buttons[row_index].click()

                # Wait for radio buttons
                active_radio = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, "//input[@value='1']"))
                )
                inactive_radio = self.driver.find_element(By.XPATH, "//input[@value='0']")

                # Toggle the status
                if inactive_radio.is_selected():
                    print("📌 Status is Inactive → Changing to Active")
                    active_radio.click()
                elif active_radio.is_selected():
                    print("📌 Status is Active → Changing to Inactive")
                    inactive_radio.click()
                else:
                    print("⚠️ No radio button selected")

                # Click Submit
                submit_btn = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "//span[text()='Submit']"))
                )
                submit_btn.click()
                print("🚀 Submitted. Waiting to return to table...")

                # Wait for page to return to table with Edit buttons again
                WebDriverWait(self.driver, 10).until(
                    EC.presence_of_all_elements_located((By.XPATH, "//tbody/tr/td[6]/a[1]"))
                )
                time.sleep(1)
                row_index += 1

            except Exception as e:
                print(f"❌ Error in row {row_index + 1}: {str(e)}")
                break

    def handle_all_status_edits(self):
        # Find all edit buttons
        edit_buttons = self.driver.find_elements(By.XPATH,
                                                 "//a[@class='btn btn-sm btn-primary'][normalize-space()='Edit']")
        print(f"Found {len(edit_buttons)} edit buttons.")

        for i in range(len(edit_buttons)):
            # Re-fetch buttons every loop in case DOM changes after edits
            edit_buttons = self.driver.find_elements(By.XPATH,
                                                     "//a[@class='btn btn-sm btn-primary'][normalize-space()='Edit']")
            if i >= len(edit_buttons):
                print(f"Row {i + 1}: Edit button no longer present (possibly already processed).")
                break

            print(f"\nEditing row {i + 1}:")

            edit_buttons[i].click()
            time.sleep(1)  # Wait for edit modal/form

            # Radio button section—same as before
            locator = (By.XPATH, "//input[@type='radio' and contains(@name,'status')]")
            radio_buttons = WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located(locator)
            )
            time.sleep(0.5)

            if len(radio_buttons) < 2:
                print("⚠️ Less than 2 radio buttons found.")
                # Try to close form if possible
                continue

            first = radio_buttons[0]
            second = radio_buttons[1]

            if first.is_selected():
                print("First radio button is selected, switching to second.")
                if not second.is_selected():
                    second.click()
                    time.sleep(0.5)
            elif second.is_selected():
                print("Second radio button is selected, switching to first.")
                if not first.is_selected():
                    first.click()
                    time.sleep(0.5)
            else:
                print("No radio button selected. Selecting the first by default.")
                first.click()
                time.sleep(0.5)

            # Click the submit button
            submit_locator = (By.XPATH, "//button[@type='button']")
            submit_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(submit_locator)
            )
            time.sleep(0.5)
            submit_button.click()
            print("🚀 Submit button clicked for this row.")
            time.sleep(1)  # Allow form to close/table to update

        print("\n✅ All Edit buttons processed.")


