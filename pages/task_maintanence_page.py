from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class task_maintanence_page(BasePage):

    task_maintanence = (By.XPATH, "//div[@data-i18n='Task Maintenance']")
    create_btn = (By.XPATH,"//a[normalize-space()='Create']")
    select_employee = (By.XPATH,"/html/body/div/div[1]/div[3]/div/div/div/form/div[1]/div[1]/select")
    select_project = (By.NAME,'project')
    submit_btn = (By.XPATH,"//button[normalize-space()='Submit']")


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def navigate_to_task_maintanence_page(self):
        print("Entering into task maintanence page")
        self.wait_and_click(self.task_maintanence)

    def create_task_maintenance_page(self, data):
        print("create task maintenance page")
        self.wait_and_click(self.create_btn)
        self.select_by_visible_text__(self.select_employee, data["employee"])
        self.select_by_visible_text__(self.select_project, data["project"])
        self.wait_and_click(self.submit_btn)









