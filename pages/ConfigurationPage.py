import time

from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class ConfigurationPage(BasePage):
    Reminder_DD = (By.XPATH, "//div[normalize-space()='Reminder']")
    configuration_DD = (By.XPATH,"//div[@data-i19n='Configuration']")
    configuration_arrow = (By.XPATH,"//li[@class='menu-item open']//a[@class='menu-link w-100 m-0 menu-toggle']")
    business_profile = (By.XPATH,"//div[@data-i19n='Business Profile']")


    # update
    submit_btn = (By.XPATH,"//button[@type='button']")
    company_name = (By.XPATH,"//input[@id='company_name']")
    office_location = (By.XPATH,"//input[@id='office_location']")
    Grace_time = (By.XPATH,"//select[@class='form-control']")
    logo_upload = (By.XPATH,"//input[@id='logo']")

    # salary
    salary_tab = (By.XPATH,"//div[@data-i19n='Salary']")


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def navigate_to_configuration_page(self):
        print("navigate to configuration page")
        # sidebar = self.driver.find_element(By.ID, "layout-menu1")  # Example locator
        #
        # # Scroll the sidebar
        # self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight;", sidebar)
        self.scroll_to_element(self.Reminder_DD)
        time.sleep(4)
        self.wait_and_click(self.configuration_DD)
        self.wait_and_click(self.business_profile)

    def validating_submit_without_changing_anydata(self):
        print("started validating submit without changeing anydata")
        self.wait_and_click(self.submit_btn)

    def validating_on_updating_values_and_submit(self):
        print("started validating on updating values and submit")
        self.upload_file(self.logo_upload,
                         "C:\\Users\\Raja\\PycharmProjects\\Py_se_Hr_project_structure\\data\Sample_images\S.png")
        self.enter_text(self.company_name,"smiligence IT solutions")
        self.enter_text(self.office_location,"Madurai,Chennai")
        self.robust_select_dropdown_option(self.Grace_time,"5 minutes",2,1)
        self.wait_and_click(self.submit_btn)
        time.sleep(2)














