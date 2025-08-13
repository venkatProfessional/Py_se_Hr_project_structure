from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class RelievingMaintenancePage(BasePage):
    releavingMaintanenceTab = (By.XPATH, "//div[@data-i18n='Relieving Maintenance']")
    viewXpath = (By.XPATH,"(//a[contains(@class,'btn-primary') and normalize-space(text())='View'])[4]")
    Approve_btn = (By.XPATH, "//button[normalize-space()='Approved']")
    decline_btn = (By.XPATH, "//button[normalize-space()='Declined']")
    allstatusvalues = (By.XPATH, "//table[@class='table']//tbody//tr/td[7]")
    allviewvalues = (By.XPATH, "(//a[contains(@class,'btn-primary') and normalize-space(text())='View'])")



    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver  # Fixed: store driver in self, not a local variable
        print("[INIT] RelievingMaintenancePage initialized with driver.")

    def navigating_to_Releving_Maintenance(self):
        print("[ACTION] Navigating to Relieving Maintenance tab...")
        print(f"[LOCATOR] Using locator: {self.releavingMaintanenceTab}")

        self.wait_and_click(self.releavingMaintanenceTab)

        print("[SUCCESS] Clicked on 'Relieving Maintenance' tab successfully.")

    def implementing_ApprovingFlow_view(self):
        print("Started implementing Approving Flow view...")

        # Step 1: Scroll to and click 'View'
        self.scroll_and_find(
            "(//a[contains(@class,'btn-primary') and normalize-space(text())='View'])[3]",
            "xpath", "horizontal"
        )
        self.wait_and_click(self.viewXpath)
        self.pause(1)

        # Step 2: Try to locate the Approve button
        btnapprove = self.scroll_and_find(
            "//button[normalize-space()='Approved']",
            "xpath",
            "vertical",
            timeout=30
        )

        # Step 3: Decide based on presence of Approve button
        if btnapprove:
            print("🚀 Approve button found, proceeding with approval process...")

            # Upload file
            self.upload_file(
                (By.XPATH, "//input[@id='document']"),
                r"C:\Users\User\PycharmProjects\SmiligenceHrAdmin\data\demo_files\salary_history_Kavya (19).pdf"
            )

            # Click Approve button
            self.wait_and_click(self.Approve_btn)
            self.pause(3)
        else:
            print("✅ Already approved")
            self.navigate_back()

    def implementing_DecliningFlow_view(self):
        print("Started implementing Approving Flow view...")

        # Step 1: Scroll to and click 'View'
        self.scroll_and_find(
            "(//a[contains(@class,'btn-primary') and normalize-space(text())='View'])[3]",
            "xpath", "horizontal"
        )
        self.wait_and_click(self.viewXpath)
        self.pause(1)

        # Step 2: Try to locate the Approve button
        btnapprove = self.scroll_and_find(
            "//button[normalize-space()='Approved']",
            "xpath",
            "vertical",
            timeout=30
        )

        # Step 3: Decide based on presence of Approve button
        if btnapprove:
            print("🚀 Approve button found, proceeding with approval process...")

            # Upload file
            self.upload_file(
                (By.XPATH, "//input[@id='document']"),
                r"C:\Users\User\PycharmProjects\SmiligenceHrAdmin\data\demo_files\salary_history_Kavya (19).pdf"
            )

            # Click Approve button
            self.wait_and_click(self.decline_btn)
            self.pause(3)
        else:
            print("✅ Already approved")
            self.navigate_back()

    def implementing_ApprovingFlow_view_all(self):
        print("🔄 Starting loop to process table rows...")

        i = 1
        while True:
            rows = self.driver.find_elements(*self.allstatusvalues)
            rows_count = len(rows)
            if i > rows_count:
                break  # no more rows

            status_locator = (By.XPATH, f"//table[@class='table']//tbody//tr[{i}]/td[7]")
            view_locator = (By.XPATH, f"(//a[contains(@class,'btn-primary') and normalize-space(text())='View'])[{i}]")

            try:
                status_text = self.driver.find_element(*status_locator).text.strip()
                print(f"Row {i} → Status: {status_text}")

                if status_text.lower() == "pending":
                    print(f"⏳ Pending found at row {i} → Clicking 'View' button...")
                    self.scroll_and_find(view_locator[1], "xpath", "horizontal")
                    self.wait_and_click(view_locator)
                    self.pause(1)

                    # Approval flow
                    btnapprove = self.scroll_and_find(
                        "//button[normalize-space()='Approved']",
                        "xpath",
                        "vertical",
                        timeout=30
                    )

                    if btnapprove:
                        print("🚀 Approve button found, proceeding with approval process...")
                        self.upload_file(
                            (By.XPATH, "//input[@id='document']"),
                            r"C:\Users\User\PycharmProjects\SmiligenceHrAdmin\data\demo_files\salary_history_Kavya (19).pdf"
                        )
                        self.wait_and_click(self.Approve_btn)
                        self.pause(3)
                    else:
                        print("✅ Already approved")

                    self.navigate_back()
                    self.pause(2)
                    # Do NOT increment i here because the page reload may reorder rows

                else:
                    print(f"✅ Row {i} status is '{status_text}' → Skipping.")
                    i += 1  # Only increment for skipped rows

            except Exception as e:
                print(f"⚠️ Exception on row {i}: {e}")
                i += 1  # In case of error, skip to next row



