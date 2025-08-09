import pytest
from pages.DR_AssignmentPermission import DR_AssignmentPermission


@pytest.mark.usefixtures("driver", "login")
class TestAssignmentPermission:

    def test_valid_assignment_permissions(self, driver):
        page = DR_AssignmentPermission(driver)
        page.NavigatingtoAssignpermissions()
        page.implementing_assign_permission_flow()


