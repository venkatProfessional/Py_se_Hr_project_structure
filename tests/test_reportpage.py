import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.reports_page import ReportsPage


@pytest.mark.usefixtures("driver", "login")
class TestReportsPage:
    # Define locators (corrected duplicates)
    reports_tab = (By.XPATH, "//div[@data-i18n='Reports']")
    salary_report = (By.XPATH, "//div[@data-i18n='Salary Report']")
    employee_attendance_report = (By.XPATH, "//div[@data-i18n='Employee Attendance Report']")
    late_comers_report = (By.XPATH, "//div[normalize-space()='Late Comers Report']")
    permission_report = (By.XPATH, "//div[normalize-space()='Permission Report']")  # Corrected duplicate
    leave_report = (By.XPATH, "//div[normalize-space()='Leave Report']")
    issue_report = (By.XPATH, "//div[normalize-space()='Issue Report']")
    project_report = (By.XPATH, "//div[normalize-space()='Project Report']")  # Corrected duplicate
    overall_report = (By.XPATH, "//div[normalize-space()='Overall Report']")
    final_statement = (By.XPATH, "//div[normalize-space()='Final Statement']")
    accounts_report = (By.XPATH, "//div[normalize-space()='Accounts Reports']")

    def navigate_to_reports_tab(self, driver):
        """
        Navigate to the Reports tab and validate the navigation.

        Args:
            driver: The Selenium WebDriver instance.
            self: The instance of the class containing this method (e.g., ReportsPage).

        Returns:
            bool: True if navigation is successful, False otherwise.
        """
        reports_page = ReportsPage(driver)

        # Perform navigation
        reports_page.clickonreportstab()

        # ✅ Validation: Check if a specific report element is visible (e.g., Reports tab)
        if "report" in driver.current_url.lower():
            print("✅ Successfully navigated to Reports tab.")
            return True
        else:
            print("❌ Reports tab navigation failed!")
            return False

    def test_navigate_to_salary_report(self, driver):
        """
        Test navigation to the Salary Report.
        """
        reports_page = ReportsPage(driver)
        reports_page.clickonreportstab()
        reports_page.wait_and_click(self.salary_report)
        reports_page.implementing_salary_report()


    def test_navigate_to_employee_attendance_report(self, driver):
        """
        Test navigation to the Employee Attendance Report.
        """
        reports_page = ReportsPage(driver)
        reports_page.clickonreportstab()
        reports_page.wait_and_click(self.employee_attendance_report)
        reports_page.implementing_Employee_attendance_report()

    def test_navigate_to_late_comers_report(self, driver):
        """
        Test navigation to the Late Comers Report.
        """
        reports_page = ReportsPage(driver)
        reports_page.clickonreportstab()
        reports_page.wait_and_click(self.late_comers_report)
        reports_page.implementing_Employee_latecommer_report()


    def test_navigate_to_permission_report(self, driver):
        """
        Test navigation to the Permission Report.
        """
        reports_page = ReportsPage(driver)
        reports_page.clickonreportstab()
        reports_page.wait_and_click(self.permission_report)
        WebDriverWait(driver, 10).until(EC.url_contains("permission-report"))
        assert "permission-report" in driver.current_url.lower(), "❌ Navigation to Permission Report failed!"
        print("✅ Successfully navigated to Permission Report.")

    def test_navigate_to_leave_report(self, driver):
        """
        Test navigation to the Leave Report.
        """
        reports_page = ReportsPage(driver)
        reports_page.clickonreportstab()
        reports_page.wait_and_click(self.leave_report)
        WebDriverWait(driver, 10).until(EC.url_contains("leave-report"))
        assert "leave-report" in driver.current_url.lower(), "❌ Navigation to Leave Report failed!"
        print("✅ Successfully navigated to Leave Report.")

    def test_navigate_to_issue_report(self, driver):
        """
        Test navigation to the Issue Report.
        """
        reports_page = ReportsPage(driver)
        reports_page.clickonreportstab()
        reports_page.wait_and_click(self.issue_report)
        WebDriverWait(driver, 10).until(EC.url_contains("issue-report"))
        assert "issue-report" in driver.current_url.lower(), "❌ Navigation to Issue Report failed!"
        print("✅ Successfully navigated to Issue Report.")

    def test_navigate_to_project_report(self, driver):
        """
        Test navigation to the Project Report.
        """
        reports_page = ReportsPage(driver)
        reports_page.clickonreportstab()
        reports_page.wait_and_click(self.project_report)
        WebDriverWait(driver, 10).until(EC.url_contains("project-report"))
        assert "project-report" in driver.current_url.lower(), "❌ Navigation to Project Report failed!"
        print("✅ Successfully navigated to Project Report.")

    def test_navigate_to_overall_report(self, driver):
        """
        Test navigation to the Overall Report.
        """
        reports_page = ReportsPage(driver)
        reports_page.clickonreportstab()
        reports_page.wait_and_click(self.overall_report)
        WebDriverWait(driver, 10).until(EC.url_contains("overall-report"))
        assert "overall-report" in driver.current_url.lower(), "❌ Navigation to Overall Report failed!"
        print("✅ Successfully navigated to Overall Report.")

    def test_navigate_to_final_statement(self, driver):
        """
        Test navigation to the Final Statement.
        """
        reports_page = ReportsPage(driver)
        reports_page.clickonreportstab()
        reports_page.wait_and_click(self.final_statement)
        WebDriverWait(driver, 10).until(EC.url_contains("final-statement"))
        assert "final-statement" in driver.current_url.lower(), "❌ Navigation to Final Statement failed!"
        print("✅ Successfully navigated to Final Statement.")

    def test_navigate_to_accounts_report(self, driver):
        """
        Test navigation to the Accounts Report.
        """
        reports_page = ReportsPage(driver)
        reports_page.clickonreportstab()
        reports_page.wait_and_click(self.accounts_report)
        WebDriverWait(driver, 10).until(EC.url_contains("accounts-report"))
        assert "accounts-report" in driver.current_url.lower(), "❌ Navigation to Accounts Report failed!"
        print("✅ Successfully navigated to Accounts Report.")
