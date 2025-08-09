from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class DR_AssignmentPermission(BasePage):
    designation_roles_button = (By.XPATH, "//div[@data-i18n='Designation & Roles']")
    roles_button = (By.XPATH, "//div[@data-i18n='Assign Roles & Permissions']")


    # assign permission edit button
    assign_list_edit_button = (By.XPATH,"//div[@class='row']//div[1]//div[1]//div[1]//a[1]")
    select2_locator = (By.XPATH, "//span[@class='selection']")

    # check box to select all
    modules_check_box_toSelect_all = (By.XPATH,"//input[@id='selectAllPermissions']")
    update_btn = (By.XPATH,"//button[normalize-space()='Update']")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def NavigatingtoAssignpermissions(self):
        print("navigating to assign permissions")
        self.wait_and_click(self.designation_roles_button)
        self.wait_and_click(self.roles_button)
        self.pause(2)

    def implementing_assign_permission_flow(self):
        print("implementing assign permission flow")
        self.wait_and_click(self.assign_list_edit_button)
        self.select2_select_multiple_options(self.select2_locator, ["HR", "Finance", "Manager"])
        self.set_checkbox_state(self.modules_check_box_toSelect_all)
        self.wait_and_click(self.update_btn)
        self.pause(2)






