# login_page.py

import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    EMAIL = (By.NAME, "email")        # Assuming this is correct
    PASSWORD = (By.NAME, "passwords")  # Assuming this is correct
    LOGIN_BTN = (By.XPATH, "//button[text()='Login']")

    @allure.step("Loading login page: {url}")
    def load(self, url):
        self.driver.get(url)

    @allure.step("Logging in with username: {username}")
    def login(self, username, password):
        self.enter_text(self.EMAIL, username)
        self.enter_text(self.PASSWORD, password)
        self.click(self.LOGIN_BTN)
