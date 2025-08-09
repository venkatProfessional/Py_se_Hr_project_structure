import pytest
from pages.PermissionMaintanence import PermissionMaintenance

@pytest.mark.usefixtures("driver", "login")
class TestPermissionMaintenance:

    def test_permission_maintenance(self, driver):
        print("Test page for Permission Maintenance")
        page = PermissionMaintenance(driver)
        page.navigating_to_permission_maintenance_page()
        page.selecting_top_fields()
        page.implementing_view_functionality()




