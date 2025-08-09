import unittest

import pytest

from pages.LeaveMaintenancePage import LeaveMaintenancePage

@pytest.mark.usefixtures("driver", "login")
class Test_leave_maintenance():

    def test_leave_maintenance(self,driver):
        print("Testing leave_maintenance")
        page = LeaveMaintenancePage(driver)
        page.navigating_to_leave_maintenance_page()
        page.selecting_top_fields()
        page.implementing_show_all()







