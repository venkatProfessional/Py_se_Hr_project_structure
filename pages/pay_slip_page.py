import time
from datetime import datetime

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage


class PaySlipPage(BasePage):

    AdvanceTab = (By.XPATH,"//div[normalize-space()='Payslip']")
    select_payslip_month =(By.XPATH,"//input[@placeholder='Select Month']")
    input_search_by_name = (By.XPATH,"//input[@id='searchName']")
    generate_payslip = (By.XPATH,"//button[@class='btn btn-primary']")


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def navigatingtopayslip(self):
        print("Navigating to payslip page")
        self.wait_and_click(self.AdvanceTab)

    def implementing_generate_payslip(self):
        self.enter_text(self.input_search_by_name, "sak")

        # Select the month
        month_input = self.driver.find_element(By.XPATH, "//input[@type='month']")
        month_input.click()
        month_input.send_keys("2025-07")

        # Normal scrolling logic (no base class)
        try:
            last_height = self.driver.execute_script("return document.body.scrollHeight")
            scrolls = 0

            while True:
                # Scroll down
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                scrolls += 1

                # Wait for new content (if any)
                import time
                time.sleep(2)

                # Calculate new scroll height
                new_height = self.driver.execute_script("return document.body.scrollHeight")
                if new_height == last_height:
                    # Reached bottom
                    break
                last_height = new_height

            print(f"✅ Finished scrolling with {scrolls} scrolls.")

        except Exception as e:
            print(f"❌ Error during scrolling: {e}")







