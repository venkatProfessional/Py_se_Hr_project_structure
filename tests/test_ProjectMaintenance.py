import pytest

from pages.projectMaintanence import ProjectMaintenance


@pytest.mark.usefixtures("driver", "login")
class TestProjectMaintenance:

    def test_navigate_to_project_maintenance(self,driver):
        page = ProjectMaintenance(driver)
        page.navigate_to_project_maintenance()
        # Call the data handler, which will internally loop and call fill_project_form(data)
        page.handle_load_test_data_from_json(
            "C:\\Users\\User\\PycharmProjects\\SmiligenceHrAdmin\\data\\project_maintanence_datas\\project_create_data.json",
            page.fill_project_form
        )

        page.handle_load_test_data_from_json(
            "C:\\Users\\User\\PycharmProjects\\SmiligenceHrAdmin\\data\\project_maintanence_datas\\project_edit_data.json",
            page.edit_project_form
        )


        # Optional: Add an assertion to verify success
        # assert page.is_element_displayed((By.XPATH, "//div[@class='some-unique-class']"))
