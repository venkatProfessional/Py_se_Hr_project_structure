from pandas.core.methods.describe import select_describe_func
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class FAQ_page(BasePage):


    faq_tab = (By.XPATH, "//div[@data-i18n='FAQ']")

    # create
    add_faq = (By.XPATH,"//a[normalize-space()='Add FAQ']")
    create_question = (By.XPATH,"//input[@name='question']")
    create_ansuer = (By.XPATH,"//textarea[@name='answer']")
    create_sort = (By.XPATH,"//input[@name='sort']")
    create_select_status = (By.XPATH,"//input[@name='sort']")
    create_submit_btn = (By.XPATH,"//button[normalize-space()='Submit']")

    # edit

    edit_icon = (By.XPATH,"//tbody/tr[1]/td[6]/a[1]/i[1]")
    edit_question = (By.XPATH,"//input[@name='question']")
    edit_ansuer = (By.XPATH,"//textarea[@name='answer']")
    edit_sort_order = (By.XPATH,"//input[@name='sort']")
    edit_status_select = (By.XPATH,"//select[@name='status']")
    edit_submit_btn = (By.XPATH,"//button[normalize-space()='Submit']")



    # delete

    delete_icon = (By.XPATH,"//tbody/tr[1]/td[6]/form[1]/button[1]/i[1]")

    #   view deleted faqs

    view_deleted_faqs = (By.XPATH,"//a[normalize-space()='View Deleted FAQs']")
    no_deleted_faqs = (By.XPATH,"//h3[normalize-space()='No Deleted FAQs Found']")
    restore_btn = (By.XPATH,"//button[normalize-space()='Restore']")
    delete_forever = (By.XPATH,"//button[normalize-space()='Delete Forever']")
    back_to_faqs = (By.XPATH,"//a[normalize-space()='Back to FAQs']")

    # validations

    validate_msg = (By.XPATH, "//div[@id='flashMessageSuccess']")



    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def navigate_to_FAQ_page(self):
        print("navigating to faq page")
        self.wait_and_click(self.faq_tab)
        self.assert_url_contains("https://smiligencehr.itsfortesza.com/admin/faqs")


    def create_faqs(self):
        print("implementing create faqs")
        self.wait_and_click(self.add_faq)
        self.enter_text(self.create_question,"How the company culture ?")
        self.enter_text(self.create_ansuer,"nice")
        self.enter_text(self.create_sort,"3")
        self.wait_and_click(self.create_submit_btn)
        self.assert_flash_message(
            self.validate_msg,
            expected_text="FAQ added successfully.",
            timeout=2  # because flash lasts only 3 seconds
        )

    def edit_faq(self, question_text="Updated company culture?", answer_text="Very nice", sort_order="2",
                 status="Active"):
        print("implementing edit faqs")

        # Click on the edit icon for the first FAQ
        self.wait_and_click(self.edit_icon)
        # Enter new question
        self.enter_text(self.edit_question, question_text)
        # Enter new answer
        self.enter_text(self.edit_ansuer, answer_text)
        # Enter new sort order
        self.enter_text(self.edit_sort_order, sort_order)
        # Select status from dropdown
        self.robust_select_dropdown_option(self.edit_status_select, status, 1)
        # Click submit
        self.wait_and_click(self.edit_submit_btn)
        # Assert flash message
        self.assert_flash_message(
            self.validate_msg,
            expected_text="FAQ updated successfully.",
            timeout=2  # flash lasts only a few seconds
        )

    def implementing_faq_delete_restore(self):
        print("implementing FAQ delete & restore")

        # Click delete icon for first FAQ
        self.wait_and_click(self.delete_icon)
        self.handle_alert()

        # View deleted FAQs
        self.wait_and_click(self.view_deleted_faqs)
        self.wait_for_seconds()

        # Restore FAQ
        self.wait_and_click(self.restore_btn)
        self.assert_flash_message(
            self.validate_msg,
            expected_text="FAQ restored successfully.",
            timeout=2  # flash lasts only a few seconds
        )
        self.wait_for_seconds(4)

        # Back to FAQ list
        self.wait_and_click(self.back_to_faqs)

    def implementing_faq_delete_permanently(self):
        print("implementing FAQ permanent delete")

        # Click delete icon
        self.wait_and_click(self.delete_icon)
        self.handle_alert()

        # View deleted FAQs
        self.wait_and_click(self.view_deleted_faqs)
        self.wait_for_seconds()

        # Delete forever
        self.wait_and_click(self.delete_forever)
        self.handle_alert()

        # Validate success message
        self.assert_flash_message(
            self.validate_msg,
            expected_text="FAQ permanently deleted.",
            timeout=2
        )
        self.wait_for_seconds(4)

        # Back to FAQ list
        self.wait_and_click(self.back_to_faqs)











