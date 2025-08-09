from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class EmailTemplatePage(BasePage):

    emailTemplates = (By.XPATH,"//div[normalize-space()='Email Templates']")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    def navigating_to_email_templates(self):
        print("navigating  to email templates")
        self.wait_and_click(self.emailTemplates)






