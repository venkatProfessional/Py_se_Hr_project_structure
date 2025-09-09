# test_accounts_maintenance_page.py

import pytest

from pages.AccountMaintanence_page import accountsMaintanencePage


@pytest.mark.usefixtures("driver", "login")
class TestAccountsMaintenancePage:

    def navigating_to_accounts_maintenance(self, driver):
        """
        Test to navigate to Accounts Maintenance tab
        """
        print("▶️ Starting test: Navigating to Accounts Maintenance")
        accounts_page = accountsMaintanencePage(driver)
        accounts_page.navigating_to_accounts_mainatence()
        print("✅ Navigation completed")

    def test_implementing_accounts(self, driver):
        """
        Test to click on Accounts tab inside Accounts Maintenance
        """
        print("▶️ Starting test: Implementing Accounts")
        accounts_page = accountsMaintanencePage(driver)
        accounts_page.navigating_to_accounts_mainatence()  # Ensure we are on the correct tab
        accounts_page.implementing_accounts()
        print("✅ Implemented Accounts tab action")
        accounts_page.implement_expense_catagories()


