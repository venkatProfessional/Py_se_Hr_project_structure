# login_page.py
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPage(BasePage):
    EMAIL = (By.NAME, "email")        # Assuming this is correct
    PASSWORD = (By.NAME, "passwords")  # Assuming this is correct
    LOGIN_BTN = (By.XPATH, "//button[text()='Login']")

    def load(self, url):
        self.driver.get(url)

    def login(self, username, password):
        self.enter_text(self.EMAIL, username)
        self.enter_text(self.PASSWORD, password)

        self.click(self.LOGIN_BTN)
