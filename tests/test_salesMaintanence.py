import pytest

from pages.SalesMaintanence import SalesMaintenance


@pytest.mark.usefixtures("driver", "login")
class TestMaintenance:
    # Add your test methods here
    def test_sales_maintanence(self, driver):
        print("✅ TestMaintenance class is running correctly.")
        page = SalesMaintenance(driver)
        page.navigate_to_lead_maintenance_and_edit()
        page.Implementing_edit_Sales_lead()
        page.implementing_create_Sales_leads()
        page.handleDeleteandRestore()
        page.validate_search_functionality()
        page.navigate_to_leadVisit()
        page.navigate_to_sales_claims()








