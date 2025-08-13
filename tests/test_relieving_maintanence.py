
import pytest
from pages.Relieving_maintanence import RelievingMaintenancePage


@pytest.mark.usefixtures("driver", "login")
class TestRelievingMaintenance:

    def test_relieving_maintenance(self, driver):
        print("Test page for Permission Maintenance")
        page = RelievingMaintenancePage(driver)
        page.navigating_to_Releving_Maintenance()
        # page.implementing_ApprovingFlow_view()
        # page.implementing_DecliningFlow_view()
        page.implementing_ApprovingFlow_view_all()














