from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class AttendanceMaintenance(BasePage):
    # Locator
    attendance_maintenance = (By.XPATH, "//div[@data-i18n='Attendance Maintenance']")

    Upload_attendance = (By.XPATH, "//button[normalize-space()='Upload Attendance (Excel)']")
    select_excel_file = (By.XPATH,"//input[@id='attendanceFile']")
    download_sample_xlsx = (By.XPATH,"//a[normalize-space()='Download Sample XLSX']")
    upload_btn = (By.XPATH,"//button[@type='submit']")
    export_attendance = (By.XPATH,"/html/body/div/div[1]/div[3]/div/div[1]/div/div/a[2]")



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
            r"C:\\Users\\User\\PycharmProjects\\SmiligenceHrAdmin\\data\\demo_files\\Book 3.xlsx"
        )

        self.wait_and_click(self.download_sample_xlsx)
        # self.verify_pdf_downloaded(expected_filename="attendance_sample (9).pdf")
        self.wait_and_click(self.upload_btn)
        # self.navigate_back()

    def handleuploadattendance(self):
        print("handling uploading the attendance flow...")
        self.wait_and_click(self.export_attendance)


