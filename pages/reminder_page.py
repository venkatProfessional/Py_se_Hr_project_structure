from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class reminder_page(BasePage):

    # Xpaths

    Reminder_DD = (By.XPATH,"//div[normalize-space()='Reminder']")

    # create
    create_btn = (By.XPATH,"//a[normalize-space()='Create']")
    Reminder_name = (By.XPATH,"//input[@id='name']")
    Reminder_Date = (By.XPATH,"//input[@name='date']")
    Reminder_Description = (By.XPATH,"//textarea[@placeholder='Description']")
    submit_btn = (By.XPATH,"//span[normalize-space()='Submit']")
    Back_btn = (By.XPATH,"//a[normalize-space()='Back']")

    # delete

    delete_icon = (By.XPATH,
                        "//a[contains(@class, 'btn red-out-btn')]")

    # Edit

    Edit_icon = (By.XPATH,"//tbody/tr[1]/td[6]/div[1]/a[1]")
    edit_remainder_name= (By.XPATH,"//input[@id='name']")
    edit_remainder_date =( By.XPATH,"//input[@name='date']")
    remainder_description = (By.XPATH,"//textarea[@placeholder='Description']")
    update_btn = (By.XPATH,"//button[normalize-space()='Update']")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def navigating_to_reminder_page(self):
        print("Navigating to reminder page")
        self.wait_and_click(self.Reminder_DD)

    def implementing_create1(self):
        print("implementing create1")
        self.wait_and_click(self.create_btn)
        self.enter_text(self.Reminder_name,"test")
        self.enter_date(self.Reminder_Date,"10-09-2025","%d-%m-%Y","%d-%m-%Y")
        self.enter_text(self.Reminder_Description,"test")
        self.wait_and_click(self.submit_btn)


    def implementing_delete(self):
        self.get_current_url()
        print("Deleting the email templates")
        self.wait_and_click(self.delete_icon)
        self.handle_alert()

    def implementing_edit(self):
        print("Implementing edit page")
        self.wait_and_click(self.Edit_icon)
        self.enter_text(self.edit_remainder_name,"test update ")
        self.enter_text(self.edit_remainder_date,"test update ")
        self.enter_text(self.remainder_description,"test update ")
        self.wait_and_click(self.update_btn)




