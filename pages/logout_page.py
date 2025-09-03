from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LogoutPage(BasePage):

    logout_menu = (By.XPATH, "//div[@data-i18n='Logout']")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def click_logout(self):
        print("checking logout flow")
        self.wait_and_click(self.logout_menu)
