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

    # permission report

    permission_report_status_select = (By.XPATH, "//select[@id='country']")
    permission_report_status_select_month = (By.XPATH, "//input[@placeholder='Select Month']")
    permission_Excel_btn = (By.XPATH, "//input[@placeholder='Select Month']")
    permission_pdf_btn = (By.XPATH, "//button[normalize-space()='PDF']")

    # leave report
    Leave_report_status_select = (By.XPATH, "//select[@id='country']")
    Leave_report_status_select_month = (By.XPATH, "//input[@placeholder='Select Month']")
    Leave_Excel_btn = (By.XPATH, "//input[@placeholder='Select Month']")
    Leave_pdf_btn = (By.XPATH, "//button[normalize-space()='PDF']")

    # issue report page

    issue_report_start_date = (By.XPATH,"//input[@id='start_date']")
    issue_report_end_date = (By.XPATH,"//input[@id='end_date']")
    issue_report_excel_btn = (By.XPATH, "//button[normalize-space()='EXCEL']")
    issue_report_pdf_btn = (By.XPATH, "//button[normalize-space()='PDF']")

    # Issue report raise issue

    issue_report_btn = (By.XPATH, "//a[@id='addbtn']")
    select_select_employee = (By.XPATH, "//select[@id='country']")
    date_issue_date = (By.XPATH,"//input[@name='Date']")
    issue_remarks = (By.XPATH,"//textarea[@id='description']")
    File_issue_photo = (By.XPATH,"//input[@id='name']")
    save_btn = (By.XPATH, "//button[normalize-space()='Save']")

    # project report

    # --- Locators for Project Report ---
    Project_report_status_select = (By.XPATH, "//select[@id='country']")
    Project_report_status_select_month = (By.XPATH, "//input[@placeholder='Select Month']")
    Project_Excel_btn = (By.XPATH, "//button[normalize-space()='Excel']")
    Project_pdf_btn = (By.XPATH, "//button[normalize-space()='PDF']")

    # overall report xpath

    overall_start_date = (By.XPATH,"//input[@id='start_date']")
    overall_end_date = (By.XPATH,"//input[@id='end_date']")
    overall_pdf_button = (By.XPATH, "//button[normalize-space()='PDF']")

    # final statement

    final_statement_create = (By.XPATH,"//a[normalize-space()='Create']")
    final_statement_select_employee = (By.XPATH, "//select[@id='country']")
    final_statement_date = (By.XPATH,"//input[@id='Date']")
    final_due_cleared_radio = (By.XPATH,"//input[@id='due_no']")
    final_statement_submit = (By.XPATH, "//button[normalize-space()='Submit']")
    final_statement_deduction_amount = (By.XPATH,"//input[@id='deduction']")
    final_statement_extra_payment = (By.XPATH,"//input[@id='extra']")
    final_statemt_comments = (By.XPATH,"//textarea[@id='reason']")

    # Account reports sub reports

    EPF_report_tab = (By.XPATH, "//div[@data-i19n='EPF Report']")
                # EPF report XPATHS
    EPF_select_employees = (By.XPATH, "//select[@id='user_id']")
    EPF_start_month_date = (By.XPATH,"//input[@id='start_date']")
    EPF_End_month_date = (By.XPATH,"//input[@id='end_date']")
    EPF_Export_btn = (By.XPATH, "//button[normalize-space()='Export']")



    ESI_report_tab = (By.XPATH,"//div[@data-i19n='ESI Report']")


    Top_sheet_report = (By.XPATH,"//div[@data-i19n='Expense Report']")

    Top_sheet_start_date = (By.XPATH,"//input[@id='start_date']")
    Top_sheet_end_date = (By.XPATH,"//input[@id='end_date']")
    Top_Sheet_pdf_button = (By.XPATH, "//button[normalize-space()='PDF']")






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
            self.verify_recent_download(".xlsx", timeout=10,download_dir ="C:\\Users\\Raja\\Downloads")

    def implementing_employee_attendance_report(self):
        print("▶️ Implementing Employee Attendance Report flow")

        # --- Excel Download ---
        # Select employee
        self.robust_select_dropdown_option(self.select_emp_attendance, "Prakash", 2)

        # Enter start date
        self.press_key("1", element=self.select_emp_attendance_month)
        self.wait_for_seconds(2)

        # Click Excel download button
        self.wait_and_click(self.emp_attendance_month_excel_btn)

        # --- Verify Excel Download ---
        excel_downloaded = self.verify_recent_download(".xlsx", timeout=30,download_dir ="C:\\Users\\Raja\\Downloads")

        # --- PDF Download ---
        # Re-select employee (sometimes UI resets after download)
        self.robust_select_dropdown_option(self.select_emp_attendance, "Prakash", 2)

        # Enter start date again
        self.press_key("1", element=self.select_emp_attendance_month)
        self.wait_for_seconds(2)

        # Click PDF download button
        self.wait_and_click(self.emp_attendance_month_pdf_btn)

        # --- Verify PDF Download ---
        pdf_downloaded = self.verify_recent_download(".pdf", timeout=30,download_dir ="C:\\Users\\Raja\\Downloads")

        # --- Final Status ---
        if not excel_downloaded and not pdf_downloaded:
            print("⚠️ No attendance data available (Excel & PDF not downloaded)")
            return False

        if excel_downloaded:
            print("✅ Employee attendance Excel downloaded successfully")

        if pdf_downloaded:
            print("✅ Employee attendance PDF downloaded successfully")

        return True

    def implementing_employee_latecomer_report(self):
        print("▶️ Implementing Employee Latecomer Report flow")

        # --- Excel Download ---
        # Select employee
        self.robust_select_dropdown_option(self.select_emp_attendance, "Deepa", 2)

        # Enter start date (month + year)
        self.press_key("1", element=self.select_emp_attendance_month)  # Month
        self.press_key("tab", element=self.select_emp_attendance_month)  # Move to Year field
        self.press_key("2025", element=self.select_emp_attendance_month)  # Year
        self.wait_for_seconds(2)

        # Click Excel download button
        self.wait_and_click(self.emp_attendance_month_excel_btn)

        # ✅ Verify Excel Download
        excel_downloaded = self.verify_recent_download(".xlsx", timeout=15,download_dir ="C:\\Users\\Raja\\Downloads")

        # --- PDF Download ---
        # Select employee
        self.robust_select_dropdown_option(self.select_emp_attendance, "Deepa", 2)

        # Enter start date (month + year)
        self.press_key("1", element=self.select_emp_attendance_month)  # Month
        self.press_key("tab", element=self.select_emp_attendance_month)  # Move to Year field
        self.press_key("2025", element=self.select_emp_attendance_month)  # Year
        self.wait_for_seconds(2)

        # Click PDF download button
        self.wait_and_click(self.emp_attendance_month_pdf_btn)

        # ✅ Verify PDF Download
        pdf_downloaded = self.verify_recent_download(".pdf", timeout=15,download_dir ="C:\\Users\\Raja\\Downloads")

        # --- Final Status ---
        if not excel_downloaded and not pdf_downloaded:
            print("⚠️ No latecomer data available (Excel & PDF not downloaded)")
            return False

        if excel_downloaded:
            print("✅ Employee latecomer Excel downloaded successfully")

        if pdf_downloaded:
            print("✅ Employee latecomer PDF downloaded successfully")

        return True

    def implementing_permission_report(self):
        print("▶️ Implementing Permission Report flow")

        try:
            # --- Select Employee ---
            self.robust_select_dropdown_option(self.permission_report_status_select, "Approved", 2)

            # --- Enter Month & Year ---
            self.press_key("1", element=self.permission_report_status_select_month)  # Month
            self.press_key("tab", element=self.permission_report_status_select_month)  # Move to Year field
            self.press_key("2025", element=self.permission_report_status_select_month)  # Year
            self.wait_for_seconds(2)

            # --- Click Excel Download ---
            self.wait_and_click(self.permission_Excel_btn)

            # --- Click PDF Download ---
            self.wait_and_click(self.permission_pdf_btn)

            # --- Verify Downloads ---
            download_dir = "C:\\Users\\Raja\\Downloads"

            excel_downloaded = self.verify_recent_download(".xlsx", timeout=12, download_dir=download_dir)
            pdf_downloaded = self.verify_recent_download(".pdf", timeout=12, download_dir=download_dir)

            # --- Final Status ---
            if not excel_downloaded and not pdf_downloaded:
                print("⚠️ Neither Excel nor PDF was downloaded.")
                return False
            elif excel_downloaded and not pdf_downloaded:
                print("✅ Excel downloaded successfully, ❌ PDF not downloaded.")
            elif pdf_downloaded and not excel_downloaded:
                print("✅ PDF downloaded successfully, ❌ Excel not downloaded.")
            else:
                print("✅ Both Excel and PDF downloaded successfully.")

            return True

        except Exception as e:
            print(f"🔥 Unexpected error while implementing permission report: {e}")
            return False

    def implementing_leave_report(self):
        print("▶️ Implementing Leave Report flow")

        try:
            # --- Select Employee / Status ---
            self.robust_select_dropdown_option(self.Leave_report_status_select, "Approved", 2)

            # --- Enter Month & Year ---
            self.press_key("1", element=self.Leave_report_status_select_month)  # Month
            self.press_key("tab", element=self.Leave_report_status_select_month)  # Move to Year field
            self.press_key("2025", element=self.Leave_report_status_select_month)  # Year
            self.wait_for_seconds(2)

            # --- Click Excel Download ---
            self.wait_and_click(self.Leave_Excel_btn)

            # --- Click PDF Download ---
            self.wait_and_click(self.Leave_pdf_btn)

            # --- Verify Downloads ---
            download_dir = "C:\\Users\\Raja\\Downloads"

            excel_downloaded = self.verify_recent_download(".xlsx", timeout=12, download_dir=download_dir)
            pdf_downloaded = self.verify_recent_download(".pdf", timeout=12, download_dir=download_dir)

            # --- Final Status ---
            if not excel_downloaded and not pdf_downloaded:
                print("⚠️ Neither Excel nor PDF was downloaded.")
                return False
            elif excel_downloaded and not pdf_downloaded:
                print("✅ Excel downloaded successfully, ❌ PDF not downloaded.")
            elif pdf_downloaded and not excel_downloaded:
                print("✅ PDF downloaded successfully, ❌ Excel not downloaded.")
            else:
                print("✅ Both Excel and PDF downloaded successfully.")

            return True

        except Exception as e:
            print(f"🔥 Unexpected error while implementing leave report: {e}")
            return False

    def implementing_issue_report(self):
        print("▶️ Implementing Issue Report flow")

        try:
            # --- Enter Start & End Dates ---
            self.enter_date(self.issue_report_start_date, "06/08/2025", "%d/%m/%Y", "%d/%m/%Y")
            self.enter_date(self.issue_report_end_date, "06/08/2025", "%d/%m/%Y", "%d/%m/%Y")
            self.wait_for_seconds(1)

            # --- Click Excel & PDF Download ---
            self.wait_and_click(self.issue_report_excel_btn)
            self.get_latest_file("C:\\Users\\Raja\\Downloads", extension=".pdf")
            self.wait_and_click(self.issue_report_pdf_btn)
            self.get_latest_file("C:\\Users\\Raja\\Downloads", extension="xlsx")

            # --- Verify Downloads ---
            download_dir = "C:\\Users\\Raja\\Downloads"
            excel_downloaded = self.verify_recent_download(".xlsx", timeout=12, download_dir=download_dir)
            pdf_downloaded = self.verify_recent_download(".pdf", timeout=12, download_dir=download_dir)

            # --- Final Status ---
            if not excel_downloaded and not pdf_downloaded:
                print("⚠️ Neither Excel nor PDF was downloaded.")
                return False
            elif excel_downloaded and not pdf_downloaded:
                print("✅ Excel downloaded successfully, ❌ PDF not downloaded.")
            elif pdf_downloaded and not excel_downloaded:
                print("✅ PDF downloaded successfully, ❌ Excel not downloaded.")
            else:
                print("✅ Both Excel and PDF downloaded successfully.")

            return True

        except Exception as e:
            print(f"🔥 Unexpected error while implementing issue report: {e}")
            return False

    def implementing_issue_report_raise_issues(self):
        print("implementing raise issues report")
        self.wait_and_click(self.issue_report_btn)
        self.robust_select_dropdown_option(self.select_select_employee,"Vimal",1)
        self.enter_date(self.date_issue_date, "08/09/2025", "%m/%d/%Y", "%m/%d/%Y")
        self.enter_text(self.issue_remarks,"test")
        self.upload_file(
            (By.XPATH, "//input[@id='name']"),
            r"C:\Users\Raja\PycharmProjects\Py_se_Hr_project_structure\data\Sample_images\S.png"
        )
        self.wait_and_click(self.save_btn)
        self.wait_for_seconds(3)

    def implementing_project_report(self):
        print("▶️ Implementing Project Report flow")

        try:
            # --- Select Status ---
            self.robust_select_dropdown_option(self.Project_report_status_select, "Completed", timeout=2)

            # --- Enter Month & Year ---
            self.press_key("1", element=self.Project_report_status_select_month)  # Month
            self.press_key("tab", element=self.Project_report_status_select_month)  # Move to Year field
            self.press_key("2025", element=self.Project_report_status_select_month)  # Year
            self.wait_for_seconds(2)

            # --- Trigger Excel Download ---
            self.wait_and_click(self.Project_Excel_btn)
            self.wait_for_seconds(5)
            self.get_latest_file(
                "C:\\Users\\Raja\\Downloads", extension=".pdf")
            self.verify_file_downloaded(file_extension=".xlsx", timeout=20)

            # --- Enter Month & Year ---
            self.press_key("1", element=self.Project_report_status_select_month)  # Month
            self.press_key("tab", element=self.Project_report_status_select_month)  # Move to Year field
            self.press_key("2025", element=self.Project_report_status_select_month)  # Year
            self.wait_for_seconds(2)

            # --- Trigger PDF Download ---
            self.wait_and_click(self.Project_pdf_btn)
            self.wait_for_seconds(5)
            self.get_latest_file(
                "C:\\Users\\Raja\\Downloads", extension=".pdf")
            self.verify_file_downloaded(file_extension=".pdf", timeout=20)

        except Exception as e:
            print(f"🔥 Unexpected error while implementing project report: {e}")
            return False

    def implementing_Overall_report_download(self):
        print("implementing Overall report download")
        # --- Enter Month & Year ---
        self.press_key("1", element=self.overall_start_date)  # Month
        self.press_key("tab", element=self.overall_start_date)  # Move to Year field
        self.press_key("2025", element=self.overall_start_date)  # Year
        self.wait_for_seconds(2)

        self.press_key("8", element=self.overall_end_date)  # Month
        self.press_key("tab", element=self.overall_end_date)  # Move to Year field
        self.press_key("2025", element=self.overall_end_date)  # Year

        self.wait_for_seconds(2)

        self.wait_and_click(self.overall_pdf_button,"10")
        self.wait_for_seconds(4)
        self.get_latest_file(
            "C:\\Users\\Raja\\Downloads", extension=".pdf")
        self.wait_for_seconds(4)
        self.verify_file_downloaded(expected_filename="overall_report (2).pdf", timeout=20)


    def implementing_final_report_download_no(self):
        print("implementing final report download no flow")
        self.wait_and_click(self.final_statement_create)
        self.robust_select_dropdown_option(self.final_statement_select_employee, "Vimal", 1)
        self.enter_date(
            self.final_statement_date,
            "13-08-2025",
            input_format="%d-%m-%Y",
            send_format="%d-%m-%Y"
        )
        self.select_radio_button("//input[@id='due_no']", by='xpath')
        self.enter_text(self.final_statement_deduction_amount,"10000")
        self.enter_text(self.final_statement_extra_payment,"10000")
        self.enter_text(self.final_statemt_comments,"test")
        self.wait_and_click(self.final_statement_submit)
        self.wait_for_seconds(5)

    def implementing_final_report_download_yes(self):
        print("implementing final report download yes flow")
        self.wait_and_click(self.final_statement_create)
        self.robust_select_dropdown_option(self.final_statement_select_employee, "Vimal", 1)
        self.enter_date(
            self.final_statement_date,
            "13-08-2025",
            input_format="%d-%m-%Y",
            send_format="%d-%m-%Y"
        )
        self.select_radio_button("//input[@id='due_yes']", by='xpath')
        self.wait_and_click(self.final_statement_submit)
        self.wait_for_seconds(5)


    def implementing_accounts_report_EPF_report(self):
        print("implementing accounts report")
        self.wait_for_seconds(3)
        self.wait_and_click(self.EPF_report_tab)
        self.wait_for_seconds(3)

        self.get_current_url()
        self.robust_select_dropdown_option(self.EPF_select_employees, "Vimal", 1)
        self.press_key("1", element=self.EPF_start_month_date)  # Month
        self.press_key("tab", element=self.EPF_start_month_date)  # Move to Year field
        self.press_key("2025", element=self.EPF_start_month_date)  # Year
        self.wait_for_seconds(2)

        self.press_key("8", element=self.EPF_End_month_date)  # Month
        self.press_key("tab", element=self.EPF_End_month_date)  # Move to Year field
        self.press_key("2025", element=self.EPF_End_month_date)  # Year
        self.wait_for_seconds(2)

        self.wait_and_click(self.EPF_Export_btn)
        self.wait_for_seconds(5)

    def implementing_accounts_report_ESI_report(self):
        print("implementing accounts report")
        self.wait_for_seconds(3)
        self.wait_and_click(self.ESI_report_tab)
        self.wait_for_seconds(3)

        self.get_current_url()
        self.robust_select_dropdown_option(self.EPF_select_employees, "Vimal", 1)
        self.press_key("1", element=self.EPF_start_month_date)  # Month
        self.press_key("tab", element=self.EPF_start_month_date)  # Move to Year field
        self.press_key("2025", element=self.EPF_start_month_date)  # Year
        self.wait_for_seconds(2)

        self.press_key("8", element=self.EPF_End_month_date)  # Month
        self.press_key("tab", element=self.EPF_End_month_date)  # Move to Year field
        self.press_key("2025", element=self.EPF_End_month_date)  # Year
        self.wait_for_seconds(2)

    def implementing_accounts_report_Top_sheet_report(self):
        print("implementing accounts report")
        self.wait_for_seconds(3)
        self.wait_and_click(self.Top_sheet_report)
        self.wait_for_seconds(3)

        self.get_current_url()

        self.enter_date(self.Top_sheet_start_date, "06/08/2025", "%d/%m/%Y", "%d/%m/%Y")
        self.enter_date(self.Top_sheet_end_date, "06/08/2025", "%d/%m/%Y", "%d/%m/%Y")
        self.wait_and_click(self.Top_Sheet_pdf_button)
        self.wait_for_seconds(4)
        self.get_latest_file("C:\\Users\\Raja\\Downloads", extension=".pdf")



















