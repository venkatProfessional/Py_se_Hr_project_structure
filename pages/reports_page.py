import time

from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from tests.conftest import driver


class ReportsPage(BasePage):

    # Xpaths for report

    reports_tab = (By.XPATH, "//div[@data-i18n='Reports']")
    # salary_report = (By.XPATH, "//div[@data-i18n='Salary Report']")
    # employee_attendance_report = (By.XPATH,"//div[@data-i18n='Employee Attendance Report']")
    # late_comers_report = (By.XPATH,"//div[normalize-space()='Late Comers Report']")
    # permission_report = (By.XPATH,"//div[normalize-space()='Late Comers Report']")
    # leave_report = (By.XPATH,"//div[normalize-space()='Leave Report']")
    # issue_report = (By.XPATH,"//div[normalize-space()='Issue Report']")
    # project_report = (By.XPATH,"//div[normalize-space()='Issue Report']")
    # overall_report =(By.XPATH,"//div[normalize-space()='Overall Report']")
    # final_statement = (By.XPATH,"//div[normalize-space()='Final Statement']")
    # accounts_report = (By.XPATH,"//div[normalize-space()='Accounts Reports']")

    # implements x path

    excel_btn = (By.XPATH, "//button[normalize-space()='EXCEL']")
    no_data_available = (By.XPATH,"//div[@class='alert alert-danger']")


    # Salary report

    start_month_date = (By.XPATH,"//input[@id='start_date']")
    end_month_date = (By.XPATH,"//input[@id='end_date']")

    # employee Attendance

    select_emp_attendance = (By.XPATH,"//select[@id='country']")
    select_emp_attendance_month = (By.XPATH,"//input[@placeholder='Select Month']")
    emp_attendance_month_excel_btn = (By.XPATH,"//button[normalize-space()='EXCEL']")
    emp_attendance_month_pdf_btn = (By.XPATH,"//button[normalize-space()='PDF']")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    def clickonreportstab(self):
        print("start validating a report page")
        self.wait_and_click(self.reports_tab)

    def implementing_salary_report(self):
        print("implementing salary report")

        # Enter start date
        self.press_key("1", element=self.start_month_date)
        self.wait_for_seconds(2)

        # Enter end date
        self.press_key("8", element=self.end_month_date)
        self.wait_for_seconds(2)

        # Click on Excel download button
        self.wait_and_click(self.excel_btn)

        # Check if "No salary data available" message appears
        if self.is_element_visible_with_text(self.no_data_available, "No salary data available."):
            print("⚠️ No salary data available")
        else:
            # Verify Excel file downloaded
            self.verify_file_downloaded(".xlsx", timeout=10)

    def implementing_Employee_attendance_report(self):
        print("implementing_Employee_attendance_report")

        # Select employee
        self.robust_select_dropdown_option(self.select_emp_attendance, "Prakash", 2)

        # Enter start date
        self.press_key("1", element=self.select_emp_attendance_month)
        self.wait_for_seconds(2)

        # Click on Excel + PDF download buttons
        self.wait_and_click(self.emp_attendance_month_excel_btn)
        self.wait_and_click(self.emp_attendance_month_pdf_btn)

    def implementing_Employee_latecommer_report(self):
        print("implementing_Employee_latecommer_report")

        # Select employee
        self.robust_select_dropdown_option(self.select_emp_attendance, "Deepa", 2)

        # Enter start date
        self.press_key("1", element=self.select_emp_attendance_month)
        self.wait_for_seconds(2)


        # Click on Excel + PDF download buttons
        self.wait_and_click(self.emp_attendance_month_excel_btn)
        self.wait_and_click(self.emp_attendance_month_pdf_btn)

        # Verify downloads
        excel_downloaded = self.verify_file_downloaded(".xlsx", timeout=10)
        pdf_downloaded = self.verify_pdf_downloaded(".pdf", timeout=10)

        if not excel_downloaded and not pdf_downloaded:
            print("⚠️ No attendance data available")
            return False
        else:
            if excel_downloaded:
                print("✅ Employee attendance Excel downloaded")
            if pdf_downloaded:
                print("✅ Employee attendance PDF downloaded")
            return True





