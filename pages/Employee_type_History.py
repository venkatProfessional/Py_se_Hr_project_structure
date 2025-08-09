import time

import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

@allure.feature("Employee Maintenance")
class EmployeeTypeHistory(BasePage):  # ✅ Class name should follow CamelCase convention
    # Locators
    employee_maintenance_dropdown = (
        By.XPATH,
        "//div[@data-i18n='Employee Maintenance']"
    )
    employee_type_history_link = (  # ✅ Renamed to avoid name conflict with class
        By.XPATH,
        "//div[@data-i18n='Employee Type History']"
    )



    employee_salary_revision =( By.XPATH,"//div[@data-i18n='Salary Revisions']")
    
    search_box_input = (By.XPATH,"//input[@type='search']")
    close_btn = (By.XPATH,"//button[normalize-space()='Close']")

    History_button = (By.XPATH, "(//a[contains(text(),'History')])[1]")
    download_pdf_btn = (By.XPATH, "//a[normalize-space()='Download PDF']")

    # employee Assets list
    employee_assets = (By.XPATH, '//*[@id="layout-menu1"]/li[3]/ul/li[4]/a/div')
    remove_btn = (By.XPATH, "//tbody/tr[1]/td[9]/button[1]")
    YES_REMOVE_IT_btn = (By.XPATH,"//button[normalize-space()='Yes, remove it!']")
    popuplocator_popup = (By.XPATH, "//div[@role='dialog']")
    view_remove_assets = (By.XPATH,"//a[normalize-space()='View Removed Assets']")
    back_on_remove_assets = (By.XPATH,"//a[normalize-space()='Back']")




    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @allure.story("Employee Type History Navigation")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.step("Navigating to Employee Type History page")
    def navigating_to_employee_type_history(self):
        print("Navigating to Employee Type History page...")
        self.wait_and_click(self.employee_maintenance_dropdown)
        self.wait_and_click(self.employee_type_history_link)
        self.pause(2)

    @allure.story("Search Bar Validation")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.step("Validating Employee Type search functionality")
    def validating_search_bar(self):
        print("Validating search bar...")
        self.enter_text(self.search_box_input,"sneha ")
        if self.is_text_visible_on_page("Divya"):
            print("Text is visible on the page")
        else:
            print("Text not found or not visible")

    @allure.story("View Button Functionality")
    @allure.step("Clicking and closing view button popup")
    def Validating_view_button(self):
        print("\n🔍 Step 1: Pausing before view button interaction...")
        self.pause(2)

        print("🔍 Step 2: Attempting to scroll and click the first 'View' button (horizontally)...")
        self.scroll_and_click("(//button[contains(text(),'View')])[1]", by="xpath", direction="horizontal")

        print("✅ 'View' button clicked. Waiting for details to load...")
        self.pause(3)

        print("🔍 Step 3: Attempting to click the 'Close' button on the view popup...")
        self.wait_and_click(self.close_btn)

        print("✅ View popup closed successfully.\n")


    @allure.story("Salary Revision Navigation")
    @allure.step("Navigating to Salary Revision page")
    def navigatingtosalaryrevision(self):
        # print("\n🔍 Step 1: Clicking on 'Employee Maintenance' dropdown...")
        # self.wait_and_click(self.employee_maintenance_dropdown)

        print("🔍 Step 2: Clicking on 'Employee Salary Revision' option...")
        self.wait_and_click(self.employee_salary_revision)


        print("✅ Navigation to 'Employee Salary Revision' page completed.\n")


    @allure.story("Download Salary History PDF")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.step("Checking history and downloading PDF")
    def check_history_and_download(self):
        print("check history and download...")
        self.wait_and_click(self.History_button)
        self.wait_and_click(self.download_pdf_btn)
        assert self.verify_pdf_downloaded(expected_filename="salary_history_Kavya (1).pdf")
        self.pause(4)

    @allure.story("Employee Assets Maintenance")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.step("Navigating and removing employee assets")
    @allure.story("Employee Assets Maintenance")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.step("Navigating and removing employee assets")
    def navigating_Employee_Assets(self):
        print("📁 Navigating to Employee Assets page...")

        print("📂 Clicking 'Employee Maintenance' dropdown...")
        self.wait_and_click(self.employee_maintenance_dropdown)

        print("🖱️ Clicking 'Employee Assets' menu...")
        self.wait_and_click(self.employee_assets)
        self.pause(2)  # Give some time for the table to load

        try:
            if self.is_text_visible_on_page("No Employee Assets Found"):
                print("❌ No data available. Please enter data and try again.")
                return  # Stop further execution if no data found
        except Exception as e:
            print("⚠️ Could not determine if data is present. Proceeding with caution.", str(e))

        print("🗑️ Clicking 'Remove' button...")
        self.wait_and_click(self.remove_btn)
        self.pause(3)

        print("⚠️ Handling confirmation popup for removal...")
        self.handle_popup_and_click(self.popuplocator_popup, self.YES_REMOVE_IT_btn)
        self.pause(2)

        print("✅ Popup handled and removal confirmed.")
        self.wait_and_click(self.view_remove_assets)
        print("🔍 Entering into removed employee asset page...")
        self.wait_and_click(self.back_on_remove_assets)
        self.check_current_url("https://smiligencehr.itsfortesza.com/admin/employee-assets")









        
