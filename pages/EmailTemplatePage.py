import time
# from encodings.punycode import selective_find

from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import alert_is_present

from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class EmailTemplatePage(BasePage):

    emailTemplates = (By.XPATH, "//div[normalize-space()='Email Templates']")
    createTemplate = (By.XPATH, "//a[normalize-space()='Create Template']")
    template_type = (By.XPATH, "//input[@id='email_type']")
    enter_subject = (By.XPATH, "//input[@placeholder='Enter Email Subject']")
    iframe_email_content = (By.XPATH, "//iframe[@title='Rich Text Editor, editor']")
    email_body = (By.XPATH, "//body")  # inside the iframe, usually <body> is editable
    Save_template = (By.XPATH, "//button[normalize-space()='Save Template']")


    #
    edit_icon = (By.XPATH, ".//a[@class='btn btn-sm blue-out-btn']/i[@class='bx bx-edit']")
    Edit_email_subject = (By.XPATH, "//input[@name='subject']")
    status = (By.XPATH,"//select[@name='status']")
    update_template_btn = (By.XPATH, "//button[normalize-space()='Update Template']")

    # delete

    delete_icon = (By.XPATH, ".//a[@class='btn btn-sm red-out-btn']/i[@class='bx bx-trash']")
    view_deleted = (By.XPATH,"//a[normalize-space()='View Deleted Templates']")
    restore_btn= (By.XPATH,"//a[normalize-space()='Restore']")
    force_delete_btn = (By.XPATH,"//body[1]/div[1]/div[1]/div[3]/div[1]/div[2]/div[1]/table[1]/tbody[1]/tr[1]/td[4]/a[2]")
    back_to_email_templates = (By.XPATH,"//a[normalize-space()='Back to Email Templates']")



    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def navigating_to_email_templates(self):
        print("navigating to email templates")
        self.wait_and_click(self.emailTemplates)

    def implementing_create_templates(self):
        print("implementing Create email templates")
        self.wait_and_click(self.createTemplate)
        self.enter_text(self.template_type, "Welcome Template 8")
        self.enter_text(self.enter_subject, "Welcome to our journey 8")

        # ✅ Switch into iframe
        iframe_element = self.find_element(self.iframe_email_content)
        self.driver.switch_to.frame(iframe_element)
        self.enter_text(self.email_body, "test 3")
        self.driver.switch_to.default_content()

        time.sleep(4)
        self.wait_and_click(self.Save_template)
        time.sleep(5)

        if self.check_current_url("https://smiligencehr.itsfortesza.com/email_templates/create"):

            self.navigate_back()
            self.navigate_back()
            self.get_current_url()




        # # Validate error message
        # error_message = self.driver.find_element(
        #     By.XPATH, "//div[contains(text(), 'The type has already been taken.')]"
        # )
        # actual_message = error_message.text
        # expected_message = "The type has already been taken."
        # self.assert_text_equals(actual_message, expected_message, "Error message validation failed!")
        #
        # self.navigate_back()

    def implementing_edit(self):
        print("Starting to edit email templates")

        # Wait for and click the edit icon
        try:
            self.wait_and_click(self.edit_icon)
        except Exception as e:
            print(f"Error clicking edit icon: {e}")
            return False

        # Check if the current URL contains the expected edit page substring
        expected_url_part = "https://smiligencehr.itsfortesza.com/email_templates/edit"
        if expected_url_part in self.driver.current_url:
            try:
                # Clear existing text and enter new subject
                self.enter_text(
                    self.Edit_email_subject,
                    "Welcome to our journey, very happy that you are part of our journey"
                )
                print("Successfully updated email template subject")

                iframe_element = self.find_element(self.iframe_email_content)
                self.switch_to_frame(iframe_element)
                self.enter_text(self.email_body, "test edited")
                self.driver.switch_to.default_content()

                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                self.pause(5.0)
                self.robust_select_dropdown_option(self.status, text="Inactive", index=2)
                self.wait_and_click(self.update_template_btn)

                return True
            except Exception as e:
                print(f"Error entering text in subject field: {e}")
                return False
        else:
            print(f"Navigation failed: Not on the edit email template page. Current URL: {self.driver.current_url}")
            return False

    def implementing_delete(self):
        self.get_current_url()
        print("Deleting the email templates")
        self.wait_and_click(self.delete_icon)
        self.handle_alert()
        self.pause()
        self.wait_and_click(self.view_deleted)
        self.wait_and_click(self.restore_btn)
        self.pause()
        self.wait_and_click(self.back_to_email_templates)

    def implmenting_force_delete(self):
        print("implementing force delete")
        self.wait_and_click(self.delete_icon)
        self.handle_alert()
        self.pause()
        self.wait_and_click(self.view_deleted)
        self.wait_and_click(self.force_delete_btn)
        self.pause()
        self.handle_alert()
        self.wait_and_click(self.back_to_email_templates)





















