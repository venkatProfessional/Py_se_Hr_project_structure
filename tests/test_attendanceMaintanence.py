import pytest
from selenium.webdriver.common.by import By

from pages.Attendance_maintanence import AttendanceMaintenance


@pytest.mark.usefixtures("driver", "login")
class TestAttendanceMaintenance:

    upload_attendance = (By.XPATH,"//button[normalize-space()='Upload Attendance (Excel)']")
    export_attendance = (By.XPATH,"//a[normalize-space()='Export Attendance']")
    absentees = (By.XPATH,"//a[normalize-space()='Absentees']")
    attendance = (By.XPATH,"//a[normalize-space()='Attendance']")


    def test_attendance_maintenance(self, driver):
        page = AttendanceMaintenance(driver)
        page.navigate_to_attendance_maintenance()
        # Add assertions or interactions here
        page.upload_attendance_flow()



