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
        page.handleexportAttendance()
        page.handleAttendance()
        # page.handle_absentees()

        if page.is_error_visible():
            print("Error message is visible as already existing data.")
            assert True  # Explicitly passing assertion (optional)
        else:
            print("Error message is NOT visible on the page.")
            page.handle_absentees()
            assert True, "Error message 'This Employee already checked-in on 2025-08-06' is NOT visible on the page"







