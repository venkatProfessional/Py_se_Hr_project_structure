from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class AdvanceMaintanencePage(BasePage):

    advanceTab = (By.XPATH, "//a[@href='https://smiligencehr.itsfortesza.com/advance']")

    # create advance amount
    create_advance_amount = (By.XPATH, "//a[normalize-space()='Create Advance Amount']")
    select_employee_se=(By.XPATH, "//div[@class='row']//div[1]//select[1]")
    payment_method_se= (By.XPATH, "//div[2]//select[1]")
    enter_amount_in = (By.XPATH, "//input[@id='payment']")
    settlement_amount_se = (By.XPATH, "//div[4]//select[1]")
    description_in= (By.XPATH, "//textarea[@placeholder='Description']")
    submit = (By.XPATH, "//button[normalize-space()='Submit']")

    # if Emi
    total_month_emi = (By.XPATH, "//span[normalize-space()='Total']")
    emi_each_month = (By.XPATH, "//span[normalize-space()='Each']")


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def navigatetoAdvance(self):
        print("Navigating to Advance")
        self.wait_and_click(self.advanceTab)


    def implementingCreateAdvanceAmount(self):
        print("Implementing Create Advance Amount")
        self.wait_and_click(self.create_advance_amount)
        print('start filling the forms')
        self.robust_select_dropdown_option(self.select_employee_se,"Jack",3)
        self.robust_select_dropdown_option(self.payment_method_se,"Cash",1)
        self.enter_text(self.enter_amount_in,"10000")
        self.robust_select_dropdown_option(self.settlement_amount_se,"Full-Payment",2)
        # self.enter_text(self.total_month_emi,"2")
        # expectedvalueofEMIpermonth = self.get_attribute_value(self.emi_each_month,"value")
        # print("EMI value is: ", expectedvalueofEMIpermonth)
        self.enter_text(self.description_in," test Description")
        self.pause(6.0)
        # self.wait_and_click(self.submit)


