from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class accountsMaintanencePage(BasePage):

    Account_maintanence_tab = (By.XPATH,"//div[normalize-space()='Accounts Maintenance']")

    Accounts_tab =    (By.XPATH, "(//div[@data-i18n='Expense Maintenance'])[1]")
    Expense_category = (By.XPATH,  "//div[@data-i18n='Expense Category']")


    # Add claim and expenses
    Add_claim_expenses_btn = (By.XPATH,"//a[normalize-space()='Add Claim and Expenses']")

    claim_enter_name = (By.XPATH,"//input[@placeholder='Enter Name']")
    select_select_type = (By.XPATH, "//select[@id='expense_type']")
    select_select_method = (By.XPATH, "//select[@id='expense_method']")
    select_employee = (By.XPATH, "//select[@id='user_id']")
    transcation_type =(By.XPATH,"//select[@id='transaction_type']")
    transaction_date = (By.XPATH, "//input[@name='date']")
    transcation_enter_amount = (By.XPATH, "//input[@placeholder='Enter the amount']")
    upload_file_attachment = (By.XPATH, "//input[@placeholder='Upload file attachment']")
    description = (By.XPATH, "//textarea[@placeholder='Description']")
    transaction_submit_btn = (By.XPATH,"//button[@type='button']")
    select_project = (By.XPATH,"//select[@id='project']")

    # Expense catagories btn

    add_expense_catagories_btn = (By.XPATH,"//a[normalize-space()='Add Expense Categories']")
    expense_category_name = (By.XPATH, "//input[@id='category_name']")
    submit_btn = (By.XPATH,"//button[normalize-space()='Submit']")


    date_accounts_report = (By.XPATH, "//input[@name='date']")
    eye_icon = (By.XPATH, "//tbody/tr[1]/td[9]/a[1]/button[1]")
    view_back = (By.XPATH,"//a[normalize-space()='Back']")



    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def navigating_to_accounts_mainatence(self):
        print("navigating to accounts mainatence")
        self.wait_and_click(self.Account_maintanence_tab)

    def implementing_accounts(self):
        print("implementing accounts")
        self.wait_and_click(self.Accounts_tab)
        self.wait_and_click(self.Add_claim_expenses_btn)
        self.enter_text(self.claim_enter_name,"test")
        self.robust_select_dropdown_option(self.select_select_type,"Expense",1)
        self.robust_select_dropdown_option(self.select_select_method,"Project",1)
        self.robust_select_dropdown_option(self.select_project," Smiligence products-(W4PM+4XV, Chinna Chokikulam, Madurai, Tamil Nadu 625002, India)",1)
        self.robust_select_dropdown_option(self.select_employee,"Vimal",1)
        self.robust_select_dropdown_option(self.transcation_type,"NEFT",1)
        self.enter_date(
            self.transaction_date,
            "13-08-2025",
            input_format="%d-%m-%Y",
            send_format="%d-%m-%Y"
        )
        self.enter_text(self.transcation_enter_amount,"1000")
        self.upload_file(
            (By.XPATH, "//input[@id='document']"),
            r"C:\Users\Raja\PycharmProjects\Py_se_Hr_project_structure\data\demo_files\salary_history_Kavya (19).pdf"
        )
        self.enter_text(self.description,"test")
        self.wait_and_click(self.transaction_submit_btn)
        self.wait_for_seconds(5)

    def implement_expense_catagories(self):
        print("implement expense catagories")
        self.wait_and_click(self.Accounts_tab)
        self.wait_and_click(self.add_expense_catagories_btn)
        self.enter_text(self.expense_category_name, "Office Supplies test ")
        self.navigate_back()
        self.wait_and_click(self.submit_btn)
        self.wait_for_seconds(5)
        self.enter_date(self.date_accounts_report, "05/09/2025", "%d/%m/%Y", "%d/%m/%Y")
        self.wait_and_click(self.eye_icon)
        self.scroll_to_element(self.view_back)
        self.wait_and_click(self.view_back)
        self.wait_for_seconds(5)




