import time

from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class Document_template(BasePage):

    document_template_tab = (By.XPATH,"//div[@data-i18n='Official Documents']")
    create_document = (By.XPATH,"//a[normalize-space()='Create Document']")
    document_subject = (By.XPATH,"//input[@placeholder='Enter Document Subject']")
    iframe_Doc_content = (By.XPATH,"//iframe[@id='editor_ifr']")
    iframe_P_content = (By.XPATH,"/html/body/p")
    save_doc_btn = (By.XPATH,"//button[normalize-space()='Save Document']")
    back_btn = (By.XPATH,"//a[@class='btn btn-secondary']")

    # Edit

    edit_icon = (By.XPATH,"(//a[@class='btn blue-out-btn btn-sm'])[1]")
    edit_document_subject = (By.XPATH,"//input[@name='subject']")
    submit_btn = (By.XPATH,"//span[normalize-space()='Submit']")
    back_BTN = (By.XPATH,"//a[normalize-space()='Back']")

    # view

    View_btn = (By.XPATH,"//a[contains(@class, 'green-out-btn')]")
    Undertaking_text = (By.XPATH, "//strong[normalize-space()='Candidate Undertaking']")

    # delete

    soft_delete_icon = (By.XPATH, "//body[1]/div[1]/div[1]/div[3]/div[1]/div[2]/div[1]/table[1]/tbody[1]/tr[1]/td[5]/a[3]")
    view_deleted = (By.XPATH, "//a[normalize-space()='View Deleted Documents']")
    restore_btn = (By.XPATH, "//a[normalize-space()='Restore']")
    Delete_permanently = (By.XPATH,
                        "(//a[@class='btn btn-sm red-out-btn'][normalize-space()='Delete Permanently'])[1]")
    backbtn = (By.XPATH, "//a[normalize-space()='Back']")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def navigating_to_template(self):
        print("navigating to email templates")
        self.wait_and_click(self.document_template_tab)

    def implementing_create_document(self):
        print("implementing create document")
        self.wait_and_click(self.create_document)
        self.enter_text(self.document_subject,"OFFER FOR DEV")
        iframe_element = self.find_element(self.iframe_Doc_content)
        self.driver.switch_to.frame(iframe_element)
        self.enter_text(self.iframe_P_content, "test 3")
        self.driver.switch_to.default_content()
        self.wait_and_click(self.save_doc_btn)
        self.wait_and_click(self.back_btn)
        self.check_current_url("https://smiligencehr.itsfortesza.com/official_documents_tinymce")

    def implementing_edit_flow(self):
        print("implementing edit flow")
        self.wait_and_click(self.edit_icon)
        self.enter_text(self.edit_document_subject,"Permanent Employment Offer with PF with UAN")
        self.wait_and_click(self.submit_btn)

    def implementing_view(self):
        print("implementing view")
        self.wait_and_click(self.View_btn)
        self.check_current_url_contains("https://smiligencehr.itsfortesza.com/official_documents")
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.scroll_to_element(self.Undertaking_text)
        self.scroll_to_element(self.back_BTN)
        self.wait_and_click(self.back_BTN)
        time.sleep(5)


    def implementing_delete(self):
        self.get_current_url()
        print("Deleting the email templates")
        self.wait_and_click(self.soft_delete_icon)
        self.handle_alert()
        self.pause()
        self.wait_and_click(self.view_deleted)
        self.wait_and_click(self.restore_btn)
        self.pause()
        self.wait_and_click(self.backbtn)

    def implmenting_force_delete(self):
        print("implementing force delete")
        self.wait_and_click(self.soft_delete_icon)
        self.handle_alert()
        self.pause()
        self.wait_and_click(self.view_deleted)
        self.wait_and_click(self.Delete_permanently)
        self.pause()
        self.handle_alert()
        self.wait_and_click(self.backbtn)















