from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from tests.conftest import driver


class AssetManagement_page(BasePage):


    asset_management_tab = (By.XPATH,"//div[@data-i18n='Assets']")
    all_assets = (By.XPATH,"//div[@data-i18n='All Assets']")
    asset_categories_tab = (By.XPATH,"//div[@data-i18n='Asset Categories']")
    asset_repairs = (By.XPATH,"//div[@data-i18n='Assets Repairs']")


    # ADD ASSETS

    add_asser_btn = (By.XPATH,"//a[normalize-space()='Add Asset']")
    add_asset_name = (By.XPATH,"//input[@name='name']")
    select_asset_category = (By.XPATH,"//select[@name='category_id']")
    add_assert_quantity = (By.XPATH,"//input[@name='qty']")
    select_status = (By.XPATH,"//select[@name='status']")
    add_assigned_status = (By.XPATH,"//select[@name='assigned']")
    add_brand = (By.XPATH,"//input[@name='brand']")
    add_model = (By.XPATH,"//input[@name='model']")
    add_purchase_date = (By.XPATH,"//input[@name='purchase_date']")
    add_cost = (By.XPATH,"//input[@name='cost']")
    add_descrition = (By.XPATH,"//textarea[@name='description']")
    select_condition = (By.XPATH,"//select[@name='condition']")
    add_location = (By.XPATH,"//input[@name='location']")
    add_warranty_period_month = (By.XPATH,"//input[@name='warranty_period']")
    add_warranty_expire_date = (By.XPATH,"//input[@name='warranty_expiry']")
    add_supplier = (By.XPATH,"//input[@name='supplier']")
    add_serial_number= (By.XPATH,"//input[@name='serial_number']")
    add_asset_image = (By.XPATH,"//input[@id='imageInput']")
    add_save_btn = (By.XPATH,"//button[normalize-space()='Save']")

    # Edit
    # ✅ EDIT Locators (explicitly written with XPath)

    edit_icon = (By.XPATH,"//tbody/tr[1]/td[7]/a[1]/i[1]")
    edit_asset_name = (By.XPATH, "//input[@name='name']")
    edit_select_asset_category = (By.XPATH, "//select[@name='category_id']")
    edit_assert_quantity = (By.XPATH, "//input[@name='qty']")
    edit_select_status = (By.XPATH, "//select[@name='status']")
    edit_assigned_status = (By.XPATH, "//select[@name='assigned']")
    edit_brand = (By.XPATH, "//input[@name='brand']")
    edit_model = (By.XPATH, "//input[@name='model']")
    edit_purchase_date = (By.XPATH, "//input[@name='purchase_date']")
    edit_cost = (By.XPATH, "//input[@name='cost']")
    edit_descrition = (By.XPATH, "//textarea[@name='description']")
    edit_select_condition = (By.XPATH, "//select[@name='condition']")
    edit_location = (By.XPATH, "//input[@name='location']")
    edit_warranty_period_month = (By.XPATH, "//input[@name='warranty_period']")
    edit_warranty_expire_date = (By.XPATH, "//input[@name='warranty_expiry']")
    edit_supplier = (By.XPATH, "//input[@name='supplier']")
    edit_serial_number = (By.XPATH, "//input[@name='serial_number']")
    edit_asset_image = (By.XPATH, "//input[@id='imageInput']")
    edit_save_btn = (By.XPATH, "//button[normalize-space()='Save']")


    # Delete

    delete_btn = (By.XPATH,"//tbody/tr[1]/td[7]/form[1]/button[1]")
    view_deleted_assets = (By.XPATH,"//a[normalize-space()='View Deleted Assets']")
    no_asset_found = (By.XPATH,"//h3[normalize-space()='No Trashed Assets Found']")
    restore_btn = (By.XPATH,"//button[normalize-space()='Restore']")
    delete_forever = (By.XPATH,"//button[normalize-space()='Delete Forever']")
    back_to_assets = (By.XPATH,"//a[normalize-space()='Back']")



    # validate

    validate_msg = (By.XPATH, "//div[@id='flashMessageSuccess']")




    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def clickonAssestmanagmenttab(self):
        self.wait_and_click(self.asset_management_tab)

    def navigate_to_ALL_Assets(self):
        self.wait_and_click(self.all_assets)

    def navigate_to_Asset_categories(self):
        self.wait_and_click(self.asset_categories_tab)

    def navigate_to_Asset_repairs(self):
        self.wait_and_click(self.asset_categories_tab)


    def implementing_all_assets_create(self):
        print("Implementing all assets form filling")
        self.wait_and_click(self.add_asser_btn)

        # 🖊 Enter text fields
        self.enter_text(self.add_asset_name, "Dell XPS 13")
        self.robust_select_dropdown_option(self.select_asset_category, "Laptop",2)
        self.enter_text(self.add_assert_quantity, "5")
        self.robust_select_dropdown_option(self.select_status, "available",2)
        self.robust_select_dropdown_option(self.add_assigned_status, "Yes",2)
        self.enter_text(self.add_brand, "Dell")
        self.enter_text(self.add_model, "XPS 13 9310")
        self.enter_date(
            self.add_purchase_date,
            "13-08-2025",
            input_format="%d-%m-%Y",
            send_format="%d-%m-%Y"
        )
        self.enter_text(self.add_cost, "120000")
        self.enter_text(self.add_descrition, "High-performance developer laptop")
        self.robust_select_dropdown_option(self.select_condition, text="Good")
        self.enter_text(self.add_location, "Chennai HQ")
        self.enter_text(self.add_warranty_period_month, "24")
        self.enter_date(
            self.add_warranty_expire_date,
            "13-12-2025",
            input_format="%d-%m-%Y",
            send_format="%d-%m-%Y"
        )
        self.enter_text(self.add_supplier, "Dell India")
        serial_number = self.get_next_incremental_value(
            folder_path="data/JSONFILES",
            file_name="asset_serials.json",
            key="laptop_serial",
            prefix="DXPS9310-",
            start=1000
        )
        self.enter_text(self.add_serial_number, serial_number)

        # 📷 Upload asset image (optional)
        try:
            self.upload_file(self.add_asset_image, r"data/Sample_images/S.png")
        except:
            print("⚠️ Skipping image upload - no file path provided")

        # 💾 Save
        self.wait_and_click(self.add_save_btn)
        self.assert_flash_message(
            self.validate_msg,
            expected_text="Asset added successfully.",
            timeout=2
        )

    def implementing_all_assets_edit(self):
        print("Editing all assets form filling")
        self.wait_and_click(self.edit_icon)
        # 🖊 Enter text fields (using EDIT locators)
        self.enter_text(self.edit_asset_name, "Dell XPS 13 - Updated")
        self.robust_select_dropdown_option(self.edit_select_asset_category, "Laptop", 2)
        self.enter_text(self.edit_assert_quantity, "10")
        self.robust_select_dropdown_option(self.edit_select_status, "available", 2)
        self.robust_select_dropdown_option(self.edit_assigned_status, "Yes", 2)
        self.enter_text(self.edit_brand, "Dell")
        self.enter_text(self.edit_model, "XPS 13 9310 - 2025 Edition")
        self.enter_date(
            self.edit_purchase_date,
            "15-09-2025",
            input_format="%d-%m-%Y",
            send_format="%d-%m-%Y"
        )
        self.enter_text(self.edit_cost, "125000")
        self.enter_text(self.edit_descrition, "Updated high-performance developer laptop")
        self.robust_select_dropdown_option(self.edit_select_condition, text="Good")
        self.enter_text(self.edit_location, "Chennai HQ - Updated")
        self.enter_text(self.edit_warranty_period_month, "36")
        self.enter_date(
            self.edit_warranty_expire_date,
            "15-12-2026",
            input_format="%d-%m-%Y",
            send_format="%d-%m-%Y"
        )
        self.enter_text(self.edit_supplier, "Dell India - Updated")

        # ✅ Increment Serial Number Dynamically
        serial_number = self.get_next_incremental_value(
            folder_path="data/JSONFILES",
            file_name="asset_serials.json",
            key="laptop_serial",
            prefix="DXPS9310-",
            start=1000
        )
        self.enter_text(self.edit_serial_number, serial_number)

        # 📷 Upload asset image (optional)
        try:
            self.upload_file(self.edit_asset_image, r"data/Sample_images/S.png")
        except:
            print("⚠️ Skipping image upload - no file path provided")

        # 💾 Save
        self.wait_and_click(self.edit_save_btn)

        # ✅ Verify success message
        self.assert_flash_message(
            self.validate_msg,
            expected_text="Asset updated successfully.",
            timeout=2
        )

    def implementing_asset_delete_restore(self):
        print("implementing Asset delete & restore")

        # Click delete button for first Asset
        self.wait_and_click(self.delete_btn)
        self.handle_alert()

        # View deleted Assets
        self.wait_and_click(self.view_deleted_assets)
        self.wait_for_seconds()

        # Restore Asset
        self.wait_and_click(self.restore_btn)
        self.assert_flash_message(
            self.validate_msg,
            expected_text="Asset restored successfully.",
            timeout=2  # flash lasts only a few seconds
        )
        self.wait_for_seconds(4)

        # (Optional) Check if no assets are found message exists
        # self.assert_element_visible(self.no_asset_found, "No deleted assets found.")

        # Navigate back
        self.wait_and_click(self.back_to_assets)

    def implementing_asset_delete_permanently(self):
        print("implementing Asset permanent delete")

        # Click delete button for first Asset
        self.wait_and_click(self.delete_btn)
        self.handle_alert()

        # View deleted Assets
        self.wait_and_click(self.view_deleted_assets)
        self.wait_for_seconds()

        # If no deleted assets are found, delete one first
        if self.is_element_visible(self.no_asset_found, timeout=2):
            print("No deleted assets found. Deleting one asset first...")
            self.wait_and_click(self.back_to_assets)
            self.wait_and_click(self.delete_btn)
            self.handle_alert()
            self.wait_and_click(self.view_deleted_assets)
            self.wait_for_seconds()

        # Delete forever
        self.wait_and_click(self.delete_forever)
        self.handle_alert()

        # Validate success message
        self.assert_flash_message(
            self.validate_msg,
            expected_text="Asset permanently deleted.",
            timeout=2
        )
        self.wait_for_seconds(4)

        # Navigate back
        self.wait_and_click(self.back_to_assets)

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#         implemeneting Asset categories

        # asset categories xpath

    ## ✅ ADD Asset Category Locators
    categories_add_asset_category = (By.XPATH, "//a[normalize-space()='Add Asset Category']")
    categories_add_category_name = (By.XPATH, "//input[@name='name']")
    categories_add_description = (By.XPATH, "//textarea[@name='description']")
    categories_add_save_category = (By.XPATH, "//button[normalize-space()='Save']")

    # ✅ EDIT Asset Category Locators
    categories_edit_asset_category_icon = (By.XPATH, "//tbody/tr[1]/td[5]/a[1]/i[1]")
    categories_edit_category_name = (By.XPATH, "//input[@name='name']")
    categories_edit_description = (By.XPATH, "//textarea[@name='description']")
    categories_edit_save_category = (By.XPATH, "//span[normalize-space()='Submit']")


    # delete

    categories_delete_icon = (By.XPATH,"//tbody/tr[1]/td[5]/form[1]/button[1]/i[1]")

    #   view deleted faqs

    categories_view_deleted= (By.XPATH,"//a[normalize-space()='View Deleted Categories']")
    categories_no_deleted = (By.XPATH,"//h3[normalize-space()='No Categories Found']")
    categories_restore_btn = (By.XPATH,"//a[normalize-space()='Restore']")
    categories_delete_permanently = (By.XPATH,"//button[normalize-space()='Delete Permanently']")
    categories_back= (By.XPATH,"//a[normalize-space()='Back']")

    def implementing_asset_category_create(self):
        print("Creating new asset category")
        self.wait_and_click(self.categories_add_asset_category)

        # ✅ Dynamically generate category name
        category_name = self.get_next_incremental_value(
            folder_path="data/JSONFILES",
            file_name="asset_categories.json",
            key="laptop_category",
            prefix="Laptops-",
            start=1000
        )
        self.enter_text(self.categories_add_category_name, category_name)
        self.enter_text(self.categories_add_description, f"Category for {category_name}")

        self.wait_and_click(self.categories_add_save_category)
        self.assert_flash_message(
            self.validate_msg,
            expected_text="Category created successfully.",
            timeout=2
        )
        self.wait_for_seconds(6)

    def implementing_asset_category_edit(self):
        print("Editing asset category")
        self.wait_and_click(self.categories_edit_asset_category_icon)

        updated_category_name = self.get_next_incremental_value(
            folder_path="data/JSONFILES",
            file_name="asset_categories.json",
            key="laptop_category",
            prefix="Laptops-Updated-",
            start=1000
        )
        self.enter_text(self.categories_edit_category_name, updated_category_name)
        self.enter_text(self.categories_edit_description, f"Updated description for {updated_category_name}")

        self.wait_and_click(self.categories_edit_save_category)
        self.assert_flash_message(
            self.validate_msg,
            expected_text="Category updated successfully.",
            timeout=2
        )
        self.wait_for_seconds(6)

    def implementing_asset_category_delete_restore(self):
        print("Implementing asset category delete & restore")

        # Open deleted categories page first
        self.wait_and_click(self.categories_view_deleted)
        self.wait_for_seconds()

        # If no deleted categories are found, delete one first
        if self.is_element_visible(self.categories_no_deleted, timeout=2):
            print("No deleted categories found. Deleting one category first...")
            self.wait_and_click(self.categories_back)
            self.wait_and_click(self.categories_delete_icon)
            self.handle_alert()
            self.wait_and_click(self.categories_view_deleted)
            self.wait_for_seconds()

        # Restore Category
        self.wait_and_click(self.categories_restore_btn)
        # self.assert_flash_message(
        #     self.validate_msg,
        #     expected_text="Asset Repair Restored Successfully",
        #     timeout=2
        # )
        self.wait_for_seconds(4)

        # Navigate back
        self.wait_and_click(self.categories_back)

    def implementing_asset_category_delete_permanently(self):
        print("Implementing asset category permanent delete")

        # Open deleted categories page first
        self.wait_and_click(self.categories_delete_icon)
        self.handle_alert()


        # Open deleted categories page first
        self.wait_and_click(self.categories_view_deleted)

        # If no deleted categories are found, delete one first
        if self.is_element_visible(self.categories_no_deleted, timeout=2):
            print("No deleted categories found. Deleting one category first...")
            self.wait_and_click(self.categories_back)
            self.wait_and_click(self.categories_delete_icon)
            self.handle_alert()
            self.wait_and_click(self.categories_view_deleted)
            self.wait_for_seconds()

        # Permanently delete
        self.wait_and_click(self.categories_delete_permanently)
        self.handle_alert()

        # self.assert_flash_message(
        #     self.validate_msg,
        #     expected_text="Asset Repair Permanently Deleted",
        #     timeout=2
        # )
        self.wait_for_seconds(4)

        # Navigate back
        self.wait_and_click(self.categories_back)


# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------














