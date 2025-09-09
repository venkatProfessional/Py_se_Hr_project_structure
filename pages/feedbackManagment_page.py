import random
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class FeedbackManagmentPage(BasePage):

    # Tabs
    feedback_management_tab = (By.XPATH, "//div[@data-i18n='Feedback Management']")
    feedback_list_tab = (By.XPATH, "//div[@data-i18n='Feedback List']")
    feedback_category = (By.XPATH, "//div[@data-i18n='Feedback Category']")

    # Feedback locators
    Add_feedback = (By.XPATH, "//a[normalize-space()='Add Feedback']")
    feeback_question = (By.XPATH, "//textarea[@name='comments']")
    select_category_feedback = (By.XPATH, "//select[@id='category_id']")
    feeback_type = (By.XPATH, "//select[@id='feedback_type']")
    feedback_submit = (By.XPATH, "//span[normalize-space()='Submit']")
    feedback_start_date = (By.XPATH, "//input[@name='start_date']")
    feedback_end_date = (By.XPATH, "//input[@name='end_date']")

    # Edit
    list_edit_icon = (By.XPATH, "//body[1]/div[1]/div[1]/div[3]/div[1]/div[2]/div[1]/table[1]/tbody[1]/tr[1]/td[8]/a[1]")
    update_btn = (By.XPATH, "//button[normalize-space()='Update']")

    # Assertions
    validate_created_successfully = (By.XPATH, "//div[@id='flashMessageSuccess']")
    validate_updated_successfully = (By.XPATH, "//div[@id='flashMessageSuccess']")

    # delete
    delete_icon = (By.XPATH,"//tbody/tr[1]/td[8]/form[1]/button[1]")
    view_deleted_feedback = (By.XPATH, "//a[normalize-space()='View Deleted Feedback']")
    restore_btn = (By.XPATH,"//button[normalize-space()='Restore']")
    delete_permanently = (By.XPATH, "//button[normalize-space()='Delete Permanently']")

    # View response

    view_response = (By.XPATH,"//tbody/tr[1]/td[8]/a[2]")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # ---------------- NAVIGATION ---------------- #
    def navigate_to_feedback_management(self):
        print("Navigating to Feedback Management")
        self.wait_and_click(self.feedback_management_tab)



    def open_feedback_list(self):
        print("Opening Feedback Category")
        self.wait_and_click(self.feedback_list_tab)

    def open_feedback_category(self):
        print("Opening Feedback Category")
        self.wait_and_click(self.feedback_category)

    # ---------------- CREATE FEEDBACK ---------------- #
    def implement_create_feedback(self, question="Test question"):
        print("📝 Implementing Create Feedback")

        # Open Add Feedback
        self.wait_and_click(self.Add_feedback)
        self.enter_text(self.feeback_question, question)

        # Select random category
        categories = ["test", "test"]
        selected_category = random.choice(categories)
        self.robust_select_dropdown_option(self.select_category_feedback, text=selected_category, index=2)
        print(f"✅ Selected Feedback Category: {selected_category}")

        # Select random type
        types = ["Life-long", "Date Range"]
        selected_type = random.choice(types)
        self.robust_select_dropdown_option(self.feeback_type, text=selected_type, index=1)
        print(f"✅ Selected Feedback Type: {selected_type}")

        # Enter dates if Date Range
        if selected_type == "Date Range":
            print("📅 Entering start/end dates")
            self.enter_date(self.feedback_start_date, "20-09-2025", input_format="%d-%m-%Y", send_format="%d-%m-%Y")
            self.enter_date(self.feedback_end_date, "30-09-2025", input_format="%d-%m-%Y", send_format="%d-%m-%Y")

        self.scroll_to_element(self.feedback_submit)
        self.wait_and_click(self.feedback_submit)
        print("💾 Feedback created successfully")

        # Assert creation
        self.assert_element_visible(self.validate_created_successfully, "Feedback Created Successfully!")

    # ---------------- EDIT FEEDBACK ---------------- #
    def implement_edit_feedback(self, question="Test question edit"):
        self.refresh_page()
        print("✏️ Implementing Edit Feedback")

        # Click edit icon
        self.wait_and_click(self.list_edit_icon)
        print("✅ Clicked Edit icon")

        # Update question
        self.enter_text(self.feeback_question, question)

        # Update category
        categories = ["Satisfaction", "Work Environment"]
        updated_category = random.choice(categories)
        self.robust_select_dropdown_option(self.select_category_feedback, text=updated_category, index=2)
        print(f"✅ Updated Feedback Category: {updated_category}")

        # Update type
        types = ["Life-long", "Date Range"]
        updated_type = random.choice(types)
        self.robust_select_dropdown_option(self.feeback_type, text=updated_type, index=1)
        print(f"✅ Updated Feedback Type: {updated_type}")

        # Update dates if Date Range
        if updated_type == "Date Range":
            print("📅 Updating start/end dates")
            self.enter_date(self.feedback_start_date, "10-09-2025", input_format="%d-%m-%Y", send_format="%d-%m-%Y")
            self.enter_date(self.feedback_end_date, "10-09-2025", input_format="%d-%m-%Y", send_format="%d-%m-%Y")

        # Save changes
        self.wait_and_click(self.update_btn)
        print("💾 Feedback updated successfully")

        # Assert update
        self.assert_element_visible(self.validate_updated_successfully, "Feedback updated successfully")

#   # ---------------- DELETE FEEDBACK ---------------- #

    def delete_feedback(self):
        print("Deleting Feedback")
        self.wait_and_click(self.delete_icon)
        self.handle_alert()
        self.wait_for_seconds(4)
        self.wait_and_click(self.view_deleted_feedback)
        self.wait_and_click(self.restore_btn)
        self.handle_alert()

        self.assert_element_visible(self.validate_updated_successfully, "Feedback Restored Successfully!")
        self.navigate_back_until_url("https://smiligencehr.itsfortesza.com/admin/feedback")

        #   # ---------------- DELETE FEEDBACK PERMANENTLY ---------------- #

    def delete_feedback_permanently(self):
        print("🗑️ Deleting Feedback")

        self.wait_and_click(self.delete_icon)
        self.handle_alert()
        self.wait_and_click(self.view_deleted_feedback)

        if self.is_text_visible_on_page("No Feedback Found"):
            print("⚠️ No items to delete.")
            self.navigate_back()
            return  # exit early, no restore action needed

        try:
            self.wait_and_click(self.delete_permanently)
            print("✅ Delete permanently button clicked.")
            self.handle_alert()
            print("✅ Alert handled successfully.")
        except Exception as e:
            print(f"❌ Failed to restore feedback: {e}")


        self.assert_element_visible(self.validate_updated_successfully, "Feedback Permanently Deleted!")
        self.navigate_back_until_url("https://smiligencehr.itsfortesza.com/admin/feedback")



    def Implementing_view_response(self):
        print("view response page")
        self.wait_and_click(self.view_response)
        if self.is_text_visible_on_page("No Feedback Found"):
            print("⚠️ No reponse.")
            self.navigate_back()
            return  # exit early, no restore action needed

# ------------------------implementing feedback category----------------------------------------------------------


    #  Xpaths

    # create

    Addcategory = (By.XPATH,"//a[normalize-space()='Add Category']")
    category_name = (By.XPATH,"//input[@name='name']")
    category_description = (By.XPATH,"//textarea[@id='description']")
    category_submit = (By.XPATH,"//span[normalize-space()='Submit']")


    # edit

    edit_icon = (By.XPATH,"//tbody/tr[1]/td[5]/a[1]")


    # delete

    category_delete = (By.XPATH,"//tbody/tr[1]/td[5]/form[1]/button[1]")
    category_restore_btn = (By.XPATH,"//button[normalize-space()='Restore']")
    category_delete_permanently = (By.XPATH,"//button[normalize-space()='Delete Permanently']")
    back_to_categories = (By.XPATH,"//a[normalize-space()='Back to Categories']")


    def  implementing_categories_create(self):
        print("starting categories create")
        self.wait_and_click(self.Addcategory)
        self.enter_text(self.category_name,"test")
        self.enter_text(self.category_description,"test")
        self.wait_and_click(self.category_submit)

    def implementing_categories_edit(self):
        print("starting categories edit")
        self.wait_and_click(self.edit_icon)
        self.enter_text(self.category_name, "test edit")
        self.enter_text(self.category_description, "test edit")
        self.wait_and_click(self.category_submit)

    def implementing_categories_delete(self):
        print("implementing delete")
        self.wait_and_click(self.category_delete)
        self.wait_and_click(self.category_restore_btn)
        self.wait_and_click(self.category_delete)
        self.wait_and_click(self.category_delete_permanently)
        self.handle_alert()








