from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class PermissionMaintenance(BasePage):

    permission_maintenance = (By.XPATH, "//div[@data-i18n='Permission Maintenance']")

    select_emp_dd = (By.XPATH, "//select[@id='user_id']")
    select_status_dd = (By.XPATH, "//select[@name='status']")
    select_date_input = (By.XPATH, "//input[@id='date']")

    apply_button = (By.XPATH, "//button[normalize-space()='Apply']")
    reset_button = (By.XPATH, "//a[normalize-space()='Reset']")
    clear_button = (By.XPATH, "//a[normalize-space()='Clear']")
    all_button = (By.XPATH, "//a[normalize-space()='All']")

    checked_first_checkbox = (By.XPATH, "//input[@value='54']")

    view_btn = (By.XPATH, "//tbody/tr[1]/td[8]/div[1]/a[1]")

    Approve_btn = (By.XPATH, "//button[normalize-space()='Approve']")
    Decline_btn = (By.XPATH, "//button[normalize-space()='Decline']")
    Enter_reason_input = (By.XPATH,"//textarea[@placeholder='Enter approve reason...']")
    confirmApprove = (By.XPATH, "//button[normalize-space()='Confirm Approve']")

    bulk_update = (By.XPATH,"//button[@id='approve-selected']")

    def __init__(self, driver):
        super().__init__(driver)

    def navigating_to_permission_maintenance_page(self):
        self.wait_and_click(self.permission_maintenance)

    def selecting_top_fields(self):
        print("🔽 Selecting top filter fields")

        print("➡️ Selecting employee: Akshaya")
        self.select_by_visible_text__(self.select_emp_dd, "Akshaya")
        print("✅ Employee 'Akshaya' selected")

        print("➡️ Selecting date: 08/09/2025")
        self.enter_date(self.select_date_input, "08/09/2025", "%m/%d/%Y", "%m/%d/%Y")
        print("✅ Date '08/09/2025' selected")

        print("➡️ Selecting status: Approved")
        self.select_by_visible_text__(self.select_status_dd, "Approved")
        print("✅ Status 'Approved' selected")

        self.pause(1)

        print("🔘 Clicking Apply button")
        self.wait_and_click(self.apply_button)
        self.pause(2)
        self.wait_and_click(self.all_button)
        self.pause(2)
        self.wait_and_click(self.clear_button)
        self.pause(2)

        # Make sure table is scrolled into view
        element = self.scroll_and_find("//th[normalize-space()='Employee Name']",
                                       by="xpath",
                                       direction="vertical",
                                       timeout=10)
        if element:
            print("✅ Found employee element:", element.text)
        else:
            print("❌ Employee element not found")

    def implementing_view_functionality(self):
        try:
            print("Starting the view...")
            self.wait_and_click(self.view_btn)
            print("Clicked the view button.")

            if self.is_text_visible_on_page("Approve") and self.is_text_visible_on_page("Decline") :
               self.pause(4)
               self.wait_and_click(self.Approve_btn)
               self.pause(2)
               self.enter_text(self.Enter_reason_input,"test")
               self.wait_and_click(self.confirmApprove)
               self.wait(6)

            else:
                print("May already be approved or rejected.")

        except Exception as e:
            print(f"Error while implementing view functionality: {e}")

    def clicking_check_box(self):
        print("clicking the check box")
        self.check_current_url("//input[@value='54']")
        self.wait_and_click(self.bulk_update)



