from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LeaveMaintenancePage(BasePage):

    Leave_maintenance_tab = (By.XPATH, "//div[@data-i18n='Leave Maintenance']")
    select_emp_dd = (By.XPATH, "//select[@id='user_id']")
    select_status_dd = (By.XPATH, "//select[@name='status']")
    select_leave_type = (By.XPATH, "//select[@name='request_type']")
    apply_button = (By.XPATH, "//button[normalize-space()='Apply']")
    reset_button = (By.XPATH, "//a[normalize-space()='Reset']")
    show_all_button = (By.XPATH, "//a[normalize-space()='Show All']")
    No_leaves_found = (By.XPATH, "//h4[normalize-space()='No leave records found.']")
    date = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[2]/table[1]/tbody[1]/tr[6]/td[3]")
    scroll_to_emp_name = (By.XPATH, "//th[normalize-space()='Employee Name']")
    checkallboxes = (By.XPATH, "//input[@id='select-all']")
    scroll_and_click_view =(By.XPATH, "(//a[@class='btn btn-sm btn-primary'][normalize-space()='View'])[1]")
    back_btn = (By.XPATH, "//a[normalize-space()='Back']")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        print("✅ Initialized LeaveMaintenancePage")

    def navigating_to_leave_maintenance_page(self):
        print("🔁 Navigating to 'Leave Maintenance' tab")
        self.wait_and_click(self.Leave_maintenance_tab)
        print("✅ Clicked on 'Leave Maintenance' tab")

    def selecting_top_fields(self):
        print("🔽 Selecting top filter fields")

        print("➡️ Selecting employee: Akshaya")
        self.select_by_visible_text__(self.select_emp_dd, "Akshaya")
        print("✅ Employee 'Akshaya' selected")

        print("➡️ Selecting status: Approved")
        self.select_by_visible_text__(self.select_status_dd, "Approved")
        print("✅ Status 'Approved' selected")

        print("➡️ Selecting leave type: Personal Leave")
        self.select_by_visible_text__(self.select_leave_type, "Personal Leave")
        print("✅ Leave type 'Personal Leave' selected")

        self.pause(1)

        print("🔘 Clicking Apply button")
        self.wait_and_click(self.apply_button)

        print("🔍 Checking for 'No leave records found'")
        is_visible = self.scroll_to_element(self.No_leaves_found)
        print(f"👁️ 'No leave records found' visible: {is_visible}")

        if is_visible:
            print("ℹ️ No leave data available for the selected filters.")
        else:
            print("✅ Leave records found, checking employee table")
            if self.scroll_to_element(self.scroll_to_emp_name):
                print("👤 'Employee Name' column is visible")
                print("☑️ Selecting all checkboxes")
                self.set_checkbox_state(self.checkallboxes)
                print("scroll and clicking a view button")
                self.pause(4)
                self.scroll_to_element(self.scroll_and_click_view)
                self.scroll_and_click("View", "text", "horizontal")
                self.pause(2)
                self.check_current_url("https://smiligencehr.itsfortesza.com/leave")
                print("🔍 Trying to click Back button using scroll_and_click")
                result = self.scroll_and_click("//a[normalize-space()='Back']", by="xpath", direction="vertical")
                print(f"➡️ Back button click result: {result}")
                if self.check_current_url("https://smiligencehr.itsfortesza.com/leave"):
                    print("selecting top fields flow finishes succesfully")
                else:
                    print("top fields flow does not work as expected")



            else:
                print("❌ 'Employee Name' column not visible — can't proceed")
