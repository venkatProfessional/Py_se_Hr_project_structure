import allure
import pytest

from pages.DR_Roles import RolesPage


@pytest.mark.usefixtures("driver", "login")
class TestDesignationRolesValidation:

    @allure.title("Blank Submit Validation with Multiple Edits")
    def test_validating_DR_roles(self, driver):
        page = RolesPage(driver)
        page.navigating_roles_list()

        page.delete_roles_for_multiple_rows()
        page.create_roles()
        page.edit_roles_for_multiple_rows()

