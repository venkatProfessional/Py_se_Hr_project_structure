from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class officialDocument(BasePage):

    official_document_tab = (By.XPATH,"//div[@data-i18n='Official document']")
    offer_letter_tab = (By.XPATH,"//div[@data-i18n='Offer Letter']")
    reliving_letter = (By.XPATH,"//div[@data-i18n='Relieving Letter']")
    Termination_letter = (By.XPATH,"//div[@data-i18n='Termination Letter']")
    Salary_revision_letter = (By.XPATH,"//div[@data-i18n='Salary Revision Letter']")
    offer_download_button = (By.XPATH,"//tbody/tr[1]/td[8]/a[1]")

    # relieving

    relieving_download = (By.XPATH,"//a[normalize-space()='Download']")
    salary_revision_download = (By.XPATH,"/html/body/div/div[1]/div[3]/div/div/div/div[1]/div/table/tbody/tr/td[7]/a")


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def navigate_official_document_page(self):
        print("Navigating to official document page")
        self.scroll_to_element(self.official_document_tab)
        self.wait_and_click(self.official_document_tab)
        self.wait_for_seconds(5)

    def Implement_offer_letter(self):
        print("Navigating to offer letter page")
        self.wait_and_click(self.offer_letter_tab)
        self.get_current_url()
        self.wait_and_click(self.offer_download_button)
        self.wait_for_seconds(4)
        self.switch_to_new_window()
        self.switch_to_default()
        self.take_screenshot("500 screenshot")
        self.switch_to_parent_window()


    def Implement_Relieving_letter(self):
        print("Navigating to offer letter page")
        self.wait_and_click(self.reliving_letter)
        self.get_current_url()
        self.wait_and_click(self.relieving_download)
        self.wait_for_seconds(4)
        self.switch_to_new_window()
        self.take_screenshot("500 screenshot")
        self.switch_to_parent_window()
        self.navigate_back()

    def Implement_termination_letter(self):
        print("Navigating to termination page")
        self.wait_and_click(self.Termination_letter)

    def implement_salary_revision_letter(self):
        print("Navigating to salary revision page")
        self.wait_and_click(self.Salary_revision_letter)
        self.wait_and_click(self.salary_revision_download)
        self.wait_for_seconds()
        self.navigate_back()
        self.wait_for_seconds(4)





