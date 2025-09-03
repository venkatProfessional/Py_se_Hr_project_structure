import time

from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class ConfigurationSalaryPage(BasePage):
    Reminder_DD = (By.XPATH, "//div[normalize-space()='Reminder']")
    configuration_DD = (By.XPATH, "//div[@data-i19n='Configuration']")
    configuration_arrow = (By.XPATH, "//li[@class='menu-item open']//a[@class='menu-link w-100 m-0 menu-toggle']")
    business_profile = (By.XPATH, "//div[@data-i19n='Business Profile']")

    # salary
    salary_tab = (By.XPATH, "//div[@data-i19n='Salary']")

    # update salary details

    basic_salary_type = (By.XPATH, "//select[@id='basic_salary_type']")
    basic_salary = (By.XPATH,"//input[@id='basic_salary']")
    howse_rent_allowance = (By.XPATH, "//input[@id='hra']")
    employer_pf_contribution = (By.XPATH, "//input[@id='employer_pf']")
    employee_pf_contribution = (By.XPATH, "//input[@id='employee_pf']")
    employer_esi_contribution = (By.XPATH, "//input[@id='employer_esi']")
    employee_esi_contribution = (By.XPATH, "//input[@id='employee_esi']")
    salary_calculation_unpaid_leave = (By.XPATH, "//select[@id='lop_calculation_option']")
    Checkbox_leave_deduction_don_sunday = (By.XPATH, "//input[@id='leave_deduction_on_sunday']")
    sales_amount_daily = (By.XPATH, "//input[@id='sales_claim_per_day']")
    update_configuration = (By.XPATH, "//button[normalize-space()='Update Configuration']")





    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        # Salary

    def Navigating_to_salary(self):
        print("Navigating to salary")
        print("navigate to configuration page")
        # sidebar = self.driver.find_element(By.ID, "layout-menu1")  # Example locator
        #
        # # Scroll the sidebar
        # self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight;", sidebar)
        self.scroll_to_element(self.Reminder_DD)
        time.sleep(4)
        self.wait_and_click(self.configuration_DD)
        self.wait_and_click(self.salary_tab)

    def update_salary_status(self):
        print("Started updating salary status")
        # self.enter_text(self.basic_salary_type, "Monthly")
        self.robust_select_dropdown_option(self.basic_salary_type,"Amount",1)
        self.enter_text(self.basic_salary, "50000")
        self.enter_text(self.howse_rent_allowance, "15000")
        self.enter_text(self.employer_pf_contribution, "1800")
        self.enter_text(self.employee_pf_contribution, "1200")
        self.enter_text(self.employer_esi_contribution, "500")
        self.enter_text(self.employee_esi_contribution, "300")
        # self.enter_text(self.salary_calculation_unpaid_leave, "10")
        self.robust_select_dropdown_option(self.salary_calculation_unpaid_leave, "Total Salary / 30", 1)
        self.set_checkbox_state(self.Checkbox_leave_deduction_don_sunday, True)
        self.enter_text(self.sales_amount_daily, "2000")
        self.wait_and_click(self.update_configuration)