import json

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pages.base_page import BasePage
import allure


@allure.feature("Sales Maintenance")
class SalesMaintenance(BasePage):
    # Locators
    sales_maintenance_dropdown = (By.XPATH, "//div[@data-i18n='Sales Maintenance']")
    lead_maintenance_link = (By.XPATH, "//div[@data-i18n='Lead Maintenance']")
    edit_button = (By.XPATH, "//tbody/tr[1]/td[9]/a[1]")



    # Edit sales lead flow
    company_name_input = (By.XPATH, "/html/body/div/div/div[3]/div/div/div[2]/div/div/form/div[1]/input")
    clientname_input = (By.XPATH,"/html/body/div/div/div[3]/div/div/div[2]/div/div/form/div[1]/input")
    clinephone_input = (By.XPATH,"//input[@type='number']")
    clientaddress_input = (By.XPATH, "/html/body/div/div/div[3]/div/div/div[2]/div/div/form/div[4]/textarea")
    clientEmail_input = (By.XPATH, "/html/body/div/div/div[3]/div/div/div[2]/div/div/form/div[5]/input")
    file_locator = (By.XPATH, "//input[@type='file']")
    submit_button = (By.XPATH, "//span[normalize-space()='Submit']")

    # create flow

    create_btn = (By.XPATH,"//a[normalize-space()='Create']")
    create_companyname = (By.XPATH, "/html/body/div/div[1]/div[3]/div/div[2]/div/div/form/div[1]/input")
    create_clientname = (By.XPATH,"/html/body/div/div[1]/div[3]/div/div[2]/div/div/form/div[2]/input")
    create_clientphone = (By.XPATH,"/html/body/div/div[1]/div[3]/div/div[2]/div/div/form/div[3]/input")
    create_clientaddress = (By.XPATH,"/html/body/div/div[1]/div[3]/div/div[2]/div/div/form/div[4]/textarea")
    create_clientEmail = (By.XPATH,"/html/body/div/div[1]/div[3]/div/div[2]/div/div/form/div[5]/input")
    create_file_upload = (By.XPATH,"//input[@type='file']")

    # delete and Restore
    delete_btn = (By.XPATH,"/html/body/div/div[1]/div[3]/div/div[1]/div[2]/div[2]/table/tbody/tr[1]/td[9]/button")
    view_delete_lead_btn  =(By.XPATH,"//a[normalize-space()='View Deleted Lead']")
    restore_btn = (By.XPATH,"//button[normalize-space()='Restore']")
    back_btn = (By.XPATH,"//a[normalize-space()='Back']")

    # search functionality
    search_by_company_name = (By.XPATH,"//input[@placeholder='Search by Company Name']")
    search_by_date = (By.XPATH,"//input[@type='date']")

    # lead visit
    # lead visit locator
    lead_visit = (By.XPATH,"//a[@href='https://smiligencehr.itsfortesza.com/admin/lead-checkins']//div[@data-i18n='Lead Visit']")

    # select month
    select_month = (By.XPATH,"//input[@placeholder='Select Month']")

    # select week
    select_week = (By.XPATH,"//select[@id='weekFilter']")
    select_value = "2025-07-01 to 2025-07-08"

    # sales claims
    sales_claims_DD = (By.XPATH,"//div[normalize-space()='Sales Claims']")
    search_by_name = (By.XPATH,"//input[@id='searchName']")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @allure.story("Navigate to Lead Maintenance Edit")
    @allure.step("Navigating to Sales > Lead Maintenance and clicking edit")
    def navigate_to_lead_maintenance_and_edit(self):
        print("📁 Navigating to Sales Maintenance page...")
        self.wait_and_click(self.sales_maintenance_dropdown)

        print("📂 Clicking on 'Lead Maintenance' menu...")
        self.wait_and_click(self.lead_maintenance_link)



    @allure.step("Editing Sales Lead with valid details")
    def Implementing_edit_Sales_lead(self):
        print("📝 Implementing edit Sales lead page...")
        print("✏️ Clicking on the first 'Edit' button...")
        self.wait_and_click(self.edit_button)
        self.pause(2)

        with allure.step("Entering Company Name"):
            self.enter_text(self.company_name_input, "TechNova Solutions")

        with allure.step("Entering Client Name"):
            self.enter_text(self.clientname_input, "Ravi Kumar")

        with allure.step("Entering Client Phone Number"):
            self.enter_text(self.clinephone_input, "9876543210")

        with allure.step("Entering Client Address"):
            self.enter_text(self.clientaddress_input, "45, Mount Road, Chennai, Tamil Nadu - 600002")

        with allure.step("Entering Client Email"):
            self.enter_text(self.clientEmail_input, "ravi.kumar@technova.com")

        with allure.step("Entering Uploading file"):
            self.upload_file(self.file_locator,"C:\\Users\\User\\Downloads\\gg.png")
            self.pause(2)

        with allure.step("Entering Submission button"):
            self.wait_and_click(self.submit_button)
            self.pause(4)
            self.navigate_back()

        print("✅ Sales lead Edit details filled successfully.")

    def load_sales_leads(self, filepath):
        import json
        with open(filepath, 'r') as f:
            return json.load(f)

    def implementing_create_Sales_leads(self):
        """Reads multiple sales leads from JSON and creates them one by one."""
        # Use raw string for file path to avoid escape character issues
        data_list = self.load_sales_leads(r"C:\Users\User\PycharmProjects\SmiligenceHrAdmin\data\create_sales_leads.json")

        for lead_data in data_list:
            print("clicking create btn")
            self.wait_and_click(self.create_btn)
            self.pause(2)
            print("Starting to create sales lead from JSON data:", lead_data["company_name"])
            with allure.step("Creating Company Name"):
                self.enter_text(self.create_companyname, lead_data["company_name"])

            with allure.step("Creating Client Name"):
                self.enter_text(self.create_clientname, lead_data["client_name"])

            with allure.step("Creating Client Phone Number"):
                self.enter_text(self.create_clientphone, lead_data["client_phone"])

            with allure.step("Creating Client Address"):
                self.enter_text(self.create_clientaddress, lead_data["client_address"])

            with allure.step("Creating Email"):
                self.enter_text(self.create_clientEmail, lead_data["client_email"])

            with allure.step("Uploading lead image"):
                self.upload_file(self.file_locator, lead_data["image_path"])
                self.pause(2)

            with allure.step("submit creation"):
                self.wait_and_click(self.submit_button)
                self.pause(2)

    def handleDeleteandRestore(self):
        print("🔁 Step 1: Starting delete and restore operation...")

        print("🧹 Clicking the delete button...")
        self.wait_and_click(self.delete_btn)
        print("✅ Delete button clicked.")

        print("⏳ Waiting before accepting the delete confirmation alert...")
        self.pause(3)

        print("⚠️ Accepting alert...")
        self.accept_alert()
        print("✅ Alert accepted.")

        print("⏳ Waiting before viewing deleted leads...")
        self.pause(3)

        print("📂 Clicking 'View Deleted Leads' button...")
        self.wait_and_click(self.view_delete_lead_btn)
        print("✅ 'View Deleted Leads' opened.")

        print("⏳ Waiting before restoring the lead...")
        self.pause(2)

        print("♻️ Clicking the restore button...")
        self.wait_and_click(self.restore_btn)
        print("✅ Lead restored.")
        self.pause(3)
        self.accept_alert()
        self.pause(3)
        self.wait_and_click(self.back_btn)
        self.pause(1)
        self.check_current_url("https://smiligencehr.itsfortesza.com/admin/sales/lead-maintenance")

        print("🎯 Delete and restore process completed.")

    def validate_search_functionality(self):
        print("Entering into validate search functionality...")
        self.enter_text(self.search_by_company_name,"prom")
        self.pause(2)
        self.is_text_visible_on_page("Promoter")
        self.pause(2)
        self.enter_date(self.search_by_date, "01-08-2025", input_format="%d-%m-%Y", send_format="%d-%m-%Y")
        self.pause(2)

    def navigate_to_leadVisit(self):
        print("Entering into navigate to lead visit...")
        self.wait_and_click(self.lead_visit)
        self.enter_date(self.select_month, "07-2025", input_format="%m-%Y", send_format="%B %Y")
        self.pause(2)
        # emp_exp_element = self.find_element(self.select_week)
        # emp_exp_DD = Select(emp_exp_element)
        #
        # # Debug: print all options in dropdown
        # options = [opt.text for opt in emp_exp_DD.options]
        # print("Available options in dropdown:", options)
        #
        # emp_exp_DD.select_by_visible_text("Week 3 (17-08-2025 to 23-08-2025)")
        # self.pause(2)
        self.select_by_visible_text__(self.select_week, "Week 3 (17-08-2025 to 23-08-2025)")
        self.pause(2)

    def navigate_to_sales_claims(self):
        self.wait_and_click(self.sales_claims_DD)
        self.pause(2)
        self.enter_date(self.select_month, "07-2025", input_format="%m-%Y", send_format="%B %Y")
        self.select_by_visible_text__(self.select_week, "Week 3 (17-08-2025 to 23-08-2025)")
        self.enter_text(self.search_by_name,"yu")
        self.is_text_visible_on_page("Yuva")
        self.pause(2)





