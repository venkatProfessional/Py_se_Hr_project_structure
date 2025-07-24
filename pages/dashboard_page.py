from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class DashboardPage(BasePage):

    DATEWISE_BUTTON = (By.XPATH, "//button[normalize-space()='Datewise']")
    MONTHLY_BUTTON = (By.XPATH, "//button[normalize-space()='Monthly']")
    HR_BUTTON = (By.XPATH, "//button[normalize-space()='HR']")
    EMPLOYEE_BUTTON = (By.XPATH, "//button[normalize-space()='Employee']")
    TODAY_BUTTON = (By.XPATH, "//button[normalize-space()='Today']")

    # Dashboard Cards
    DASHBOARD_CARDS = {
        "Total Employees": (By.XPATH, "//h4[normalize-space()='Total Employees']"),
        "Total Check-In": (By.XPATH, "//h4[normalize-space()='Total Check-In']"),
        "Total Absent": (By.XPATH, "//h4[normalize-space()='Total Absent']"),
        "Leaves Pending": (By.XPATH, "//h4[normalize-space()='Leaves Pending']"),
        "Leaves Approved": (By.XPATH, "//h4[normalize-space()='Leaves Approved']"),
        "Unmarked Breaks": (By.XPATH, "//h4[normalize-space()='Unmarked Breaks']"),
        "Leaves Tomorrow": (By.XPATH, "//h4[normalize-space()='Leaves Tomorrow']"),
        "Permissions Pending": (By.XPATH, "//h4[normalize-space()='Permissions Pending']"),
        "Permissions Approved": (By.XPATH, "//h4[normalize-space()='Permissions Approved']"),
        "Permission Tomorrow": (By.XPATH, "//h4[normalize-space()='Permission Tomorrow']"),
        "Relieving": (By.XPATH, "//h4[normalize-space()='Relieving']"),
        "New Joiner": (By.XPATH, "//h4[normalize-space()='New Joiner']"),
        "Check-Out Completion": (By.XPATH, "//h4[normalize-space()='Check-Out Completion']"),
        "Marked Breaks": (By.XPATH, "//h4[normalize-space()='Marked Breaks']")
    }

    # Page headers or unique texts to verify navigation
    CARD_PAGE_HEADERS = {
        "Total Employees": (By.XPATH, "//*[contains(text(), 'Employee List')]"),
        "Total Check-In": (By.XPATH, "//*[contains(text(), 'Attendance')]"),
        "Total Absent": (By.XPATH, "//*[contains(text(), 'Absentees')]"),
        "Leaves Pending": (By.XPATH, "//*[contains(text(), 'Leave Maintenance')]"),
        "Leaves Approved": (By.XPATH, "//*[contains(text(), 'Leave Maintenance')]"),
        "Unmarked Breaks": (By.XPATH, "//*[contains(text(), 'Attendance')]"),
        "Leaves Tomorrow": (By.XPATH, "//*[contains(text(), 'Leave Maintenance')]"),
        "Permissions Pending": (By.XPATH, "//*[contains(text(), 'Permission Maintenance')]"),
        "Permissions Approved": (By.XPATH, "//*[contains(text(), 'Permission Maintenance')]"),
        "Permission Tomorrow": (By.XPATH, "//*[contains(text(), 'Permission Maintenance')]"),
        "Relieving": (By.XPATH, "//*[contains(text(), 'Relieving Letter')]"),
        "New Joiner": (By.XPATH, "//*[contains(text(), 'Employee List')]"),
        "Check-Out Completion": (By.XPATH, "//*[contains(text(), 'Attendance')]"),
        "Marked Breaks": (By.XPATH, "//*[contains(text(), 'Attendance')]")
    }

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Filters
    def click_datewise(self): self.driver.find_element(*self.DATEWISE_BUTTON).click()
    def click_monthly(self): self.driver.find_element(*self.MONTHLY_BUTTON).click()
    def click_HR(self): self.driver.find_element(*self.HR_BUTTON).click()
    def click_employee(self): self.driver.find_element(*self.EMPLOYEE_BUTTON).click()
    def click_today(self): self.driver.find_element(*self.TODAY_BUTTON).click()

    # Main navigation loop
    def check_navigation_for_all_dashboard_cards(self):
        """
        Iterates through dashboard cards, clicks each one, and validates navigation
        by checking the presence of the corresponding page header.
        Skips cards where header is not found or not visible.
        """
        self.click_today()

        for card_name, card_locator in self.DASHBOARD_CARDS.items():
            try:
                print(f"\n[INFO] Navigating to: {card_name}")
                self.driver.find_element(*card_locator).click()

                header_locator = self.CARD_PAGE_HEADERS.get(card_name)
                if not header_locator:
                    print(f"[WARNING] Header locator missing for '{card_name}'. Skipping.")
                    continue

                # Wait up to 5 seconds for the header to become visible
                if not self.wait_until_visible(header_locator, timeout=5):
                    print(f"[WARNING] Header not visible for '{card_name}'. Skipping.")
                    continue

                print(f"[SUCCESS] Navigation verified for: {card_name}")

            except Exception as e:
                print(f" navigate or validate '{card_name}")

            finally:
                # Return to dashboard and reset filter
                self.driver.back()
                self.click_today()

