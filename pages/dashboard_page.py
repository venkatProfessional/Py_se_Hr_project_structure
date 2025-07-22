from selenium.webdriver.common.by import By

class DashboardPage:
    DATEWISE_BUTTON = (By.XPATH, "//button[normalize-space()='Datewise']")
    MONTHLY_BUTTON = (By.XPATH, "//button[normalize-space()='Monthly']")
    HR_BUTTON = (By.XPATH, "//button[normalize-space()='HR']")
    EMPLOYEE_BUTTON = (By.XPATH, "//button[normalize-space()='Employee']")
    TODAY_BUTTON = (By.XPATH, "//button[normalize-space()='Today']")

    def __init__(self, driver):
        self.driver = driver

    def click_datewise(self):
        self.driver.find_element(*self.DATEWISE_BUTTON).click()

    def click_monthly(self):
        self.driver.find_element(*self.MONTHLY_BUTTON).click()

    def click_HR(self):
        self.driver.find_element(*self.HR_BUTTON).click()

    def click_employee(self):
        self.driver.find_element(*self.EMPLOYEE_BUTTON).click()

    def click_Today(self):
        self.driver.find_element(*self.TODAY_BUTTON).click()
