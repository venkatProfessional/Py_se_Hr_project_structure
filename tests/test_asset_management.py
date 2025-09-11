# test_employee_creation.py
import pytest

from pages.AssetManagementpage import AssetManagement_page
from pages.FAQ_page import FAQ_page


@pytest.mark.usefixtures("driver", "login")
class TestAssetManagement:

    def test_asset_management(self, driver):
        page =AssetManagement_page(driver)
        page.clickonAssestmanagmenttab()
        page.navigate_to_ALL_Assets()
        page.implementing_all_assets_create()
        page.implementing_all_assets_edit()
        page.implementing_asset_delete_restore()
        page.implementing_asset_delete_permanently()

#         catagories

    def test_asset_category(self, driver):
        page = AssetManagement_page(driver)
        page.clickonAssestmanagmenttab()
        page.navigate_to_Asset_categories()
        page.implementing_asset_category_create()
        page.implementing_asset_category_edit()
        page.implementing_asset_category_delete_restore()
        page.implementing_asset_category_delete_permanently()






