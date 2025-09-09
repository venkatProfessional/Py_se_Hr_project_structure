from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class HolidayAndCalender(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    Holiday_tab = (By.XPATH, "//div[normalize-space()='Holiday']")
    Calender_tab = (By.XPATH, "//div[normalize-space()='Calendar']")

    # calender

    left_arrow = (By.XPATH,"//span[@class='fc-icon fc-icon-chevron-left']")
    right_arrow = (By.XPATH,"//span[@class='fc-icon fc-icon-chevron-right']")
    today = (By.XPATH,"//button[normalize-space()='today']")
    Holiday_btn = (By.XPATH,"//a[@class='btn btn-primary']")
    today_date_click = (By.XPATH,"//td[contains(@class,'fc-daygrid-day fc-day fc-day-mon fc-day-today')]")
    swal_popup_input_create = (By.XPATH,"//input[@id='swal2-input']")
    swal_popup_save = (By.XPATH,"//button[normalize-space()='Save']")


    # update

    swal_input_update = (By.XPATH,"//input[@id='swal-input1']")
    swal_update_btn = (By.XPATH, "//button[normalize-space()='Update']")
    swal_delete = (By.XPATH, "//button[normalize-space()='Delete']")
    yes_delete_it = (By.XPATH, "//button[normalize-space()='Yes, delete it!']")


    def navigate_to_holiday(self):
        print("Navigating to holiday")
        self.wait_and_click(self.Holiday_tab)


    def navigate_to_calender(self):
        print("Navigating to calender")
        self.wait_and_click(self.Calender_tab)

    def implementing_calender(self):
        print("Implementing calendar flow")
        # go left 3 times
        for _ in range(3):
            self.wait_and_click(self.left_arrow)
            self.wait_for_seconds(1)

        # go right 3 times
        for _ in range(3):
            self.wait_and_click(self.right_arrow)
            self.wait_for_seconds(1)



        print("🏖️ Creating Holiday")
        self.wait_and_click(self.today_date_click)
        if self.is_element_visible(self.swal_update_btn):
            print("✏️ Holiday already exists, updating...")

            # Use update locator if needed
            self.wait_until_visible(self.swal_input_update, timeout=10)
            self.enter_text(self.swal_input_update, "summa update")
            self.wait_and_click(self.swal_update_btn)
            self.wait_and_click(self.today_date_click)

            self.wait_until_visible(self.swal_delete, timeout=10)
            self.wait_and_click(self.swal_delete)
            self.wait_and_click(self.yes_delete_it)


        else:
            print("➕ Creating new holiday...")

            self.wait_until_visible(self.swal_popup_input_create, timeout=10)
            self.enter_text(self.swal_popup_input_create, "summa")
            self.wait_and_click(self.swal_popup_save)

        # Click Holiday button
        self.wait_and_click(self.Holiday_btn)

        # Capture current URL
        current_url = self.get_current_url()
        print(f"🌐 Current URL after holiday action: {current_url}")