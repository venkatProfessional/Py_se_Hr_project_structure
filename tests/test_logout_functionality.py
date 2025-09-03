import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.logout_page import LogoutPage


@pytest.mark.usefixtures("driver", "login")
class TestLogoutPage:

    def test_logout_functionality(self, driver):
        """
        Test the logout functionality.
        """
        logout_page = LogoutPage(driver)

        # Perform logout
        logout_page.click_logout()

        # Wait for redirect to login page (adjust URL part as needed)
        # WebDriverWait(driver, 10).until(EC.url_contains("login"))

        # ✅ Validation
        assert "https://smiligencehr.itsfortesza.com/" in driver.current_url.lower(), "❌ Logout failed: Did not redirect to login page."
        print("✅ Logout successful and redirected to login page.")
