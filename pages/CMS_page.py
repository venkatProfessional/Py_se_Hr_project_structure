import json
import os

from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CMS_page(BasePage):

    COUNTER_FILE = "data/JSONFILES/cms_counter.json"


    def __init__(self, driver):
        super().__init__(driver)
        self.test_counter = self._load_counter()

    def _load_counter(self):
        """Read the counter value from JSON file or initialize with 1 if not found."""
        if os.path.exists(self.COUNTER_FILE):
            with open(self.COUNTER_FILE, "r") as f:
                data = json.load(f)
                return data.get("count", 1)
        return 1

    def _save_counter(self):
        """Write the updated counter back to the JSON file."""
        with open(self.COUNTER_FILE, "w") as f:
            json.dump({"count": self.test_counter}, f)


    cms_xpath = (By.XPATH,"//div[@data-i18n='CMS Pages']")
    page_title = (By.XPATH,"//input[@id='pageTitle']")
    page_slug = (By.XPATH,"//input[@id='pageSlug']")
    page_content = (By.XPATH,"//div[@aria-label='Editor editing area: main']//p")
    select_visible_on = (By.XPATH,"//select[@name='visible_on']")
    select_status = (By.XPATH,"//select[@name='status']")

    create_cms_page = (By.XPATH,"//a[normalize-space()='Create CMS Page']")
    page_title =(By.XPATH,"//input[@id='pageTitle']")

    cms_submit_btn =(By.XPATH,"//span[normalize-space()='Submit']")

    # edit
    cms_edit_icon = (By.XPATH,"//tbody/tr[1]/td[7]/a[1]/i[1]")
    cms_edit_page_title = (By.XPATH,"//input[@id='pageTitle']")
    cms_edit_page_slug = (By.XPATH,"//strong[normalize-space()='SMILIGENCE LEAVE POLICY']")
    select_visible_on = (By.XPATH,"//select[@name='visible_on']")
    select_status = (By.XPATH,"//select[@name='status']")
    cms_edit_submit = (By.XPATH,"//span[normalize-space()='Submit']")

    # delete

    delete_icon = (By.XPATH,"//tbody/tr[1]/td[7]/a[3]/i[1]")
    delete_page_title = (By.XPATH,"//input[@id='pageTitle']")
    view_deleted_btn =(By.XPATH,"//a[normalize-space()='View Deleted CMS Pages']")
    restore_btn = (By.XPATH,"//tbody/tr[1]/td[5]/a[1][1]/i[1]")
    delete_permanently_btn = (By.XPATH,"//body[1]/div[1]/div[1]/div[3]/div[1]/div[2]/div[1]/table[1]/tbody[1]/tr[1]/td[5]/a[2]")
    back_to_cms =(By.XPATH,"//a[normalize-space()='Back to CMS Pages']")

    # validations

    validate_msg = (By.XPATH,"//div[@id='flashMessageSuccess']")



    def navigate_to_cms_page(self):
        print("navigating to cms page")
        self.scroll_to_element(self.cms_xpath)
        self.wait_and_click(self.cms_xpath)

    def implementing_cms_create(self):
        print("implementing cms create")
        self.test_counter += 1
        self._save_counter()  # save back to JSON file
        self.wait_and_click(self.create_cms_page)
        self.enter_text(self.page_title, f"test{self.test_counter}")
        self.enter_text(self.page_content, "test")
        self.robust_select_dropdown_option(self.select_visible_on, "Web", 2, 1)
        self.robust_select_dropdown_option(self.select_status, "Active", 2, 1)
        self.scroll_to_element(self.cms_submit_btn)
        self.wait_and_click(self.cms_submit_btn)
        self.assert_flash_message(
            self.validate_msg,
            expected_text="CMS Page Created Successfully!",
            timeout=2  # because flash lasts only 3 seconds
        )


    def implementing_cms_edit(self):
        print("implementing cms edit")

        # Click edit icon
        self.wait_and_click(self.cms_edit_icon)

        # Find and clear page content text area
        pagecontent_ele = self.find_element(self.page_content)
        pagecontent_ele.clear()
        pagecontent_ele.send_keys("smiligence leaves policy cms")

        # Select dropdowns (use separate locators if needed)
        self.robust_select_dropdown_option(self.select_visible_on, "App", 1, 10)
        self.robust_select_dropdown_option(self.select_status, "Active", 1, 10)

        # Submit the edit form
        self.wait_and_click(self.cms_edit_submit)
        self.assert_flash_message(
            self.validate_msg,
            expected_text="CMS Page Updated Successfully!",
            timeout=2  # because flash lasts only 3 seconds
        )

    def implementing_cms_delete_restore(self):
        print("implementing cms delete")

        self.wait_and_click(self.delete_icon)
        self.handle_alert()
        self.wait_and_click(self.view_deleted_btn)
        self.wait_for_seconds()
        # self.assert_element_visible(self.validate_msg, "CMS Page Soft Deleted!")
        self.wait_and_click(self.restore_btn)
        self.assert_flash_message(
            self.validate_msg,
            expected_text="CMS Page Restored Successfully!",
            timeout=2  # because flash lasts only 3 seconds
        )
        self.wait_and_click(self.back_to_cms)


    def implementing_cms_delete_permenantely(self):
        self.wait_and_click(self.delete_icon)
        self.handle_alert()
        self.wait_and_click(self.view_deleted_btn)
        self.wait_for_seconds()
        # self.assert_element_visible(self.validate_msg, "CMS Page Soft Deleted!")
        self.wait_and_click(self.delete_permanently_btn)
        self.handle_alert()
        # self.wait_and_click(self.back_to_cms)
        self.assert_flash_message(
            self.validate_msg,
            expected_text="CMS Page Permanently Deleted!",
            timeout=2  # because flash lasts only 3 seconds
        )
        self.wait_and_click(self.back_to_cms)











