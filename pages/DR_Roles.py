import json
import time
from tkinter.tix import Select

import allure
from selenium.common import TimeoutException, NoAlertPresentException
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class RolesPage(BasePage):
    designation_roles_button = (By.XPATH, "//div[@data-i18n='Designation & Roles']")
    roles_button = (By.XPATH, "//div[@data-i18n='Roles & Permissions']")

    # Edit button
    edit_button = (By.XPATH, "//tbody/tr[1]/td[5]/a[1]")
    role_name = (By.XPATH,"//input[@id='name']")
    status = (By.XPATH, "//select[@id='status']")
    update_role = (By.XPATH, "//button[normalize-space()='Update Role']")

    # delete
    soft_delete_button =(By.XPATH,"(//a[contains(text(),'Soft Delete')])[1]")

    # create button
    create_button =(By.XPATH, "//a[normalize-space()='Create']")
    create_role_name = (By.XPATH, "//input[@id='name']")
    pick_status_select = (By.XPATH, "/html/body/div/div[1]/div[3]/div/div/div/form/div[1]/div[2]/select")
    submit_btn_create =(By.XPATH, "//button[normalize-space()='Submit']")




    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def navigating_roles_list(self):
        print("🔍 Navigating to 'Designation Roles' section...")
        self.wait_and_click(self.designation_roles_button)
        print("✅ Clicked on 'Designation Roles'.")

        print("🔍 Navigating to 'Roles' subsection...")
        self.wait_and_click(self.roles_button)
        print("✅ Clicked on 'Roles'.")

        print("⏳ Waiting for roles list to load...")
        time.sleep(1)
        print("✅ Roles list navigation complete.")

    def create_roles(self):
        print("🔁 [Step 1] Role creation started...")

        # Load roles from JSON file
        with open(r"C:\Users\User\PycharmProjects\SmiligenceHrAdmin\data\roles.json", "r") as file:
            roles = json.load(file)

        for role in roles:
            role_name = role["role_name"]
            status = role["status"]

            try:
                print(f"🔍 [Step 2] Clicking the 'Create' button for role '{role_name}'...")
                self.wait_and_click(self.create_button)
                print("✅ [Step 2] 'Create' button clicked.")
            except Exception as e:
                print(f"❌ [Error] Failed to click 'Create' button: {e}")
                continue

            try:
                print(f"📝 [Step 3] Typing role name: '{role_name}'")
                self.enter_text(self.create_role_name, role_name)
                print("✅ [Step 3] Role name entered.")
            except Exception as e:
                print(f"❌ [Error] Failed to enter role name: {e}")
                continue

            try:
                print(f"📂 [Step 4] Selecting status: '{status}'")
                self.select_by_visible_text__(self.pick_status_select, status)
                print("✅ [Step 4] Status selected.")
            except Exception as e:
                print(f"❌ [Error] Failed to select status: {e}")
                continue

            try:
                print("🚀 [Step 5] Clicking the 'Submit' button...")
                self.wait_and_click(self.submit_btn_create)
                print(f"✅ [Step 5] Submit button clicked. Role '{role_name}' creation submitted.")
            except Exception as e:
                print(f"❌ [Error] Failed to click submit button: {e}")
                continue

        print("🎉 [Done] Role creation process completed for all roles.")

    def  edit_roles_for_multiple_rows(self):
        for row_index in range(1, 4):
            print(f"\n🔄 Editing role at row {row_index}...")
            isalreadytakenvisible = self.is_text_visible_on_page("The name has already been taken.")
            if isalreadytakenvisible:
                self.navigate_back()

            edit_button_xpath = f"//tbody/tr[{row_index}]/td[5]/a[1]"
            print(f"🔍 Locating edit button for row {row_index}: {edit_button_xpath}")
            self.wait_and_click((By.XPATH, edit_button_xpath))
            print(f"✅ Clicked edit button at row {row_index}")

            role_name_value = f"Global Admin {row_index}"
            print(f"🔍 Typing role name: {role_name_value}")
            self.enter_text(self.role_name, role_name_value)
            print("✅ Role name entered.")

            print("🔍 Locating status dropdown...")
            status_select_element = self.find_element(self.status)
            print("✅ Status dropdown located.")

            print("🔍 Selecting 'Active' from status dropdown...")
            self.select_dropdown(status_select_element, method="text", option="Active")
            print("✅ Status 'Active' selected.")

            print("🔍 Clicking 'Update Role' button...")
            self.wait_and_click(self.update_role)
            print("✅ Role updated successfully.")
            time.sleep(1)

        print("🛑 Done editing roles. No further clicks will be performed.")

    def delete_roles_for_multiple_rows(self):
        print("🗑️ Starting deletion flow for multiple roles...")

        try:
            print("🔍 Attempting to click the soft delete button...")
            self.wait_and_click(self.soft_delete_button)
            print("✅ Soft delete button clicked.")

            print("⏳ Waiting for alert to appear (timeout: 10s)...")
            self.pause(1.5)  # Give time for alert to appear visibly
            self.handle_alert(action="accept", timeout=10)
            print("✅ Alert accepted successfully.")
            self.pause(2)
            self.navigate_back()

        except Exception as e:
            print(f"❌ Exception occurred during role deletion: {e}")
            current_url = self.driver.current_url
            print(f"🌐 Current URL at failure: {current_url}")

            # Take screenshot and attach to Allure
            screenshot_path = self.take_screenshot("delete_role_failure")

            with open(screenshot_path, "rb") as image_file:
                allure.attach(image_file.read(), name="Role_Deletion_Failure_Screenshot",
                              attachment_type=allure.attachment_type.PNG)

            allure.attach(current_url, name="Current URL",
                          attachment_type=allure.attachment_type.TEXT)

            raise  # Re-raise the exception to let test fail












