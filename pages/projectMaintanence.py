import time
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ProjectMaintenance(BasePage):
    # Main navigation
    project_maintenance_dd = (By.XPATH, "//div[@data-i18n='Project Maintenance']")
    create_btn = (By.XPATH, "//a[normalize-space()='Create']")
    edit_button = (By.XPATH, "//div[@class='container-xxl flex-grow-1 container-p-y']//div[1]//div[1]//div[1]//div[1]//div[1]//a[1]")
    

    # Form input fields
    project_name_locator = (By.XPATH, "//input[@id='project_name']")
    project_address_locator = (By.XPATH, "//input[@id='project_address']")
    owner_name_locator = (By.XPATH, "//input[@id='owner_name']")
    client_phone_locator = (By.XPATH, "//input[@id='owner_phone']")
    owner_distance_locator = (By.XPATH, "//input[@id='distance']")
    google_point_1_locator = (By.XPATH, "(//input[@id='point'])[1]")
    google_point_2_locator = (By.XPATH, "(//input[@id='point'])[2]")
    start_date_locator = (By.XPATH, "//div[8]//input[1]")
    end_date_locator = (By.XPATH, "/html/body/div/div[1]/div[3]/div/div/div/form/div[1]/div[9]/input")

    # Dropdowns and toggle
    status_select = (By.XPATH, '/html/body/div/div[1]/div[3]/div/div/div/form/div[1]/div[10]/select')
    project_lead_select = (By.XPATH, "//select[@id='projectLead']")
    toggle_primary_project = (By.XPATH, "//input[@id='isPrimaryProject']")

    # Submit
    submit_btn = (By.XPATH, "//button[@id='submitBtn']")
    update_submit_btn = (By.XPATH, "//button[normalize-space()='Submit']")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def navigate_to_project_maintenance(self):
        """Navigate to Project Maintenance -> Create page."""
        self.wait_and_click(self.project_maintenance_dd)
        # self.wait_and_click(self.create_btn)

    def fill_project_form(self, data):
        self.wait_and_click(self.create_btn)
        self.enter_text(self.project_name_locator, data["project_name"])
        self.enter_text(self.project_address_locator, data["project_address"])
        self.enter_text(self.owner_name_locator, data["owner_name"])
        self.enter_text(self.client_phone_locator, data["client_phone"])
        self.enter_text(self.owner_distance_locator, data["owner_distance"])
        self.enter_text(self.google_point_1_locator, data["google_point_1"])
        self.enter_text(self.google_point_2_locator, data["google_point_2"])
        self.enter_date(self.start_date_locator, data["start_date"], input_format="%m-%d-%Y",send_format="%m-%d-%Y")
        self.enter_date(self.end_date_locator, data["end_date"], input_format="%m-%d-%Y",send_format="%m-%d-%Y")
        self.select_by_visible_text__(self.status_select, data["status"])
        self.select_by_visible_text__(self.project_lead_select, data["project_lead"])
        # self.toggle_switch(self.toggle_primary_project, target_state=data["is_primary_project"])
        self.wait_and_click(self.submit_btn)
        self.pause(3)


    def edit_project_form(self, data):
        self.wait_and_click(self.edit_button)
        self.enter_text(self.project_name_locator, data["project_name"])
        self.enter_text(self.project_address_locator, data["project_address"])
        self.enter_text(self.owner_name_locator, data["owner_name"])
        self.enter_text(self.client_phone_locator, data["client_phone"])
        self.enter_text(self.owner_distance_locator, data["owner_distance"])
        self.enter_text(self.google_point_1_locator, data["google_point_1"])
        self.enter_text(self.google_point_2_locator, data["google_point_2"])
        self.enter_date(self.start_date_locator, data["start_date"], input_format="%m-%d-%Y",send_format="%m-%d-%Y")
        self.enter_date(self.end_date_locator, data["end_date"], input_format="%m-%d-%Y",send_format="%m-%d-%Y")
        self.select_by_visible_text__(self.status_select, data["status"])
        self.select_by_visible_text__(self.project_lead_select, data["project_lead"])
        self.toggle_switch(self.toggle_primary_project, target_state=data["is_primary_project"])
        self.wait_and_click(self.update_submit_btn)
        self.pause(3)







