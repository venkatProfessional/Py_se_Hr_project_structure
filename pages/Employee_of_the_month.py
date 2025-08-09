from selenium.webdriver.common.by import By

from pages.base_page import BasePage



class Employee_of_the_month(BasePage):

    employee_of_month = (By.XPATH, "//div[@data-i18n='Employee Of Month']")
    # select Employee
    select_employee = (By.XPATH,"//select[@id='country']")
    select_month = (By.XPATH,"//input[@name='month']")
    start_label = (By.XPATH,"//label[@for='star-3']")
    comment_input = (By.XPATH,"//textarea[@placeholder='Comment']")
    Add_button = (By.XPATH,"//a[normalize-space()='Add']")
    submit_button = (By.XPATH,"//button[normalize-space()='Submit']")

    # edit

    edit_icon = (By.XPATH, "//i[contains(@class, 'bx-edit')]/parent::a")
    delete_icon =(By.XPATH,"/html/body/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div[2]/div/h5/span/a[2]")


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def navigate_to_employee_of_month(self):
        self.wait_and_click(self.employee_of_month)

    def test_employee_of_the_month(self):
        print("starting a automation for employee of month")

        self.wait_and_click(self.Add_button)


        self.select_by_visible_text__(self.select_employee,"Akshaya",print_all_options=True)
        # Example to enter March 2025
        # self.enter_date(self.select_month, "03-2025", input_format="%m-%Y", send_format="%B %Y")
        self.wait_and_click(self.start_label)
        self.pause(2)
        self.enter_text(self.comment_input,"test comment")
        self.wait_and_click(self.submit_button)
        self.pause()

    def test_edit_employee_of_the_month(self):
        print("🛠️ Edit employee of month started")

        # Navigate to the correct page
        self.navigate_to_employee_of_month()
        print("✅ Navigated to Employee of the Month page")

        # Wait and click the edit icon (anchor tag, not <i>)
        print("🔍 Waiting for edit icon to be clickable...")
        self.wait_and_click(self.edit_icon)
        print("🖱️ Edit icon clicked")

        # Wait for comment input to become visible
        print("⏳ Waiting for comment input to appear...")
        self.wait_until_visible(self.comment_input)
        print("✅ Comment input visible")

        # Enter the comment
        self.enter_text(self.comment_input, "test edit comment")
        print("✍️ Entered comment")

        # Submit the form
        print("🔘 Submitting form...")
        self.wait_and_click(self.submit_button)
        print("✅ Submit button clicked")












