import pytest
from selenium.webdriver.common.by import By

from pages.Attendance_maintanence import AttendanceMaintenance


@pytest.mark.usefixtures("driver", "login")
class TestAttendanceMaintenance:

    def test_attendance_maintenance(self, driver):
        page = AttendanceMaintenance(driver)
        page.navigate_to_attendance_maintenance()
        # Add assertions or interactions here
        page.upload_attendance_flow()
        # page.handleuploadattendance()





