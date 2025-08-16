import time

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pages.base_page import BasePage

class AttendanceMaintenance(BasePage):
    # Locator
    attendance_maintenance = (By.XPATH, "//div[@data-i18n='Attendance Maintenance']")

    Upload_attendance = (By.XPATH, "//button[normalize-space()='Upload Attendance (Excel)']")
    select_excel_file = (By.XPATH,"//input[@id='attendanceFile']")
    download_sample_xlsx = (By.XPATH,"//a[normalize-space()='Download Sample XLSX']")
    upload_btn = (By.XPATH,"//button[@type='submit']")

    # export attendance

    export_attendance_btn = (By.XPATH,"//a[normalize-space()='Export Attendance']")

    #
    absentees_btn = (By.XPATH,"//a[normalize-space()='Absentees']")
    absentees_date_select =(By.XPATH,"//input[@type='date']")
    pagination_date = (By.XPATH,"//a[normalize-space()='8']")



    # Export Attendance Data

    start_date_select = (By.XPATH,"//input[@id='start_date']")
    end_date_select= (By.XPATH,"//input[@id='end_date']")
    excel_btn = (By.XPATH,"//button[normalize-space()='EXCEL']")

    #Attendance Module
    Attendance_btn = (By.XPATH,"//a[normalize-space()='Attendance']")
    # AttendanceInputs forms
    selectEmployee = (By.XPATH,"//select[@id='selectEmployee']")
    selectProject = (By.XPATH,"//select[@id='selectProject']")
    enterDate = (By.XPATH,"//input[@id='Date']")
    checkinInput = (By.XPATH,"//input[@id='checkin_time']")
    morningBreaktimeInput = (By.XPATH,"//input[@id='break_time']")
    Lunchtime = (By.XPATH,"//input[@id='lunch_time']")
    EveningBreaktime = (By.XPATH,"//input[@id='break_time3']")
    clientMeetingTime = (By.XPATH,"//input[@id='break_time4']")
    otherOfficeVisitTime = (By.XPATH,"//input[@id='break_time5']")
    EmergencyPersonalBreakTime = (By.XPATH,"//input[@id='break_time6']")
    checkouttime = (By.XPATH,"//input[@id='checkout_time']")
    workStatus = (By.XPATH,"//textarea[@id='reason']")
    submit_btn = (By.XPATH,"//button[normalize-space()='Submit']")





    def __init__(self, driver):
        super().__init__(driver)

    def navigate_to_attendance_maintenance(self):
        print("Navigating to Attendance Maintenance...")
        self.wait_and_click(self.attendance_maintenance)

    def upload_attendance_flow(self):
        print("upload attendance flow...")

        self.wait_and_click(self.Upload_attendance)

        self.upload_file(
            (By.XPATH, "//input[@id='attendanceFile']"),
            r"C:\Users\Raja\PycharmProjects\Py_se_Hr_project_structure\data\demo_files\attendance_sample (8).xlsx"
        )
        self.pause(3.0)

        self.wait_and_click(self.download_sample_xlsx)
        # self.verify_pdf_downloaded(expected_filename="attendance_sample (9).pdf")
        self.verify_file_downloaded(expected_filename="attendance_sample.xlsx", timeout=20)
        self.wait_and_click(self.upload_btn)
        self.pause(3.0)
        # self.navigate_back()

    def handleexportAttendance(self):
        print("handling uploading the attendance flow...")
        self.wait_and_click(self.export_attendance_btn)
        self.enter_date(
            self.start_date_select,
            "13-08-2025",
            input_format="%d-%m-%Y",
            send_format="%d-%m-%Y"
        )
        self.enter_date(
            self.end_date_select,
            "20-08-2025",
            input_format="%d-%m-%Y",
            send_format="%d-%m-%Y"
        )
        self.wait_and_click(self.excel_btn)
        self.verify_file_downloaded(expected_filename="attendance.xlsx", timeout=20)
        self.navigate_back()

    def handle_absentees(self):
        with allure.step("Click on Absentees button"):
            print("handling absentees...")
            self.wait_and_click(self.absentees_btn)

        with allure.step("Enter date in the Absentees date field"):
            self.enter_date(
                self.absentees_date_select,
                "28-07-2025",
                input_format="%d-%m-%Y",
                send_format="%d-%m-%Y"
            )

        with allure.step("Scroll to pagination element"):
            self.scroll_to_element(self.pagination_date)

        with allure.step("Wait until pagination element is visible"):
            self.wait_until_visible(self.pagination_date)
            time.sleep(5)  # optional, can remove if unnecessary

        with allure.step("Click on pagination element"):
            self.wait_and_click(self.pagination_date)
            time.sleep(10)

        with allure.step("Verify current URL matches expected"):
            expected_url = "https://smiligencehr.itsfortesza.com/absentees?search=2025-08-13&page=8"
            assert self.check_current_url(expected_url), f"URL does not match! Expected: {expected_url}"

        with allure.step("Take screenshot of absentees page"):
            screenshot_path = "absentees.png"
            self.take_screenshot(screenshot_path)
            # Attach screenshot to Allure report
            with open(screenshot_path, "rb") as f:
                allure.attach(f.read(), name="Absentees Screenshot", attachment_type=allure.attachment_type.PNG)



    def handleAttendance(self):
        print("clicking on Attendance...")
        self.wait_and_click(self.Attendance_btn)
        self.robust_select_dropdown_option(self.selectEmployee, text="Jack", index=2)
        self.enter_date(self.enterDate, "06/08/2025", "%d/%m/%Y", "%d/%m/%Y")
        self.enter_text(self.checkinInput,"12.00 PM ")
        self.enter_text(self.morningBreaktimeInput,"12.00 PM")
        self.enter_text(self.Lunchtime,"12.00 PM")
        self.enter_text(self.EveningBreaktime,"12.00 PM")
        self.enter_text(self.clientMeetingTime,"12.00 PM")
        self.enter_text(self.otherOfficeVisitTime,"12.00 PM")
        self.enter_text(self.EmergencyPersonalBreakTime,"12.00 PM")
        self.enter_text(self.checkouttime,"12.00 PM")
        self.enter_text(self.workStatus,"test")
        self.wait_and_click(self.submit_btn)



    def is_error_visible(self):
        with allure.step("Verify error message"):
            print("Entering error message check...")

            # Call a utility method that returns True/False if text is visible on page
            is_visible = self.is_text_visible_on_page("This Employee already checked-in on 2025-08-06")

            if is_visible:
                print("Error message is visible as expected.")
                self.navigate_back()
            else:
                print("Error message is NOT visible on the page.")

                # # Assert with a clear message
                # assert is_visible, "Error message 'This Employee already checked-in on 2025-08-06' is NOT visible on the page"
                # print("Error message is visible as expected.")
                #
                # self.navigate_back()

            # Optionally navigate back if needed

            return is_visible



















