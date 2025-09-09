import json
import time
import uuid

import pandas as pd
from selenium.common import TimeoutException, ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class EmployeeCreationPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        self.employee_maintenance_DD = (
            By.XPATH,
            "//div[@data-i18n='Employee Maintenance']"
        )

        self.employee_list = (
            By.XPATH,
            "//div[@data-i18n='Employee List']"
        )

        self.create_btn =(
            By.XPATH,
            "//a[normalize-space()='Create']"
        )

        self.employee_name=(By.XPATH,'//*[@id="username"]')
        self.gender_dropdown=(By.XPATH,"/html/body/div/div[1]/div[3]/div/div/div/div[2]/form/div/div[2]/select")
        self.role_dropdown=(By.XPATH,'//*[@id="role"]')
        self.officialmail = (By.XPATH,'//*[@id="email"  and @placeholder="john.doe@example.com"]')
        self.personalmail = (By.XPATH,"//input[@id='personal_email']")
        self.emp_type_dropdown = (By.XPATH,'//*[@id="emptype"]')
        self.emp_desig_dropdown = (By.XPATH,'//*[@id="designation"]')
        self.emp_exp_dropdown = (By.XPATH,'//*[@id="emp_experience"]')
        self.joining_date = (By.XPATH,"//input[@id='joining_date']")
        self.DOBdate = (By.XPATH,"//input[@id='date_of_birth']")
        self.phone_number = (By.XPATH,"//input[@id='phoneNumber']")
        self.password_input = (By.XPATH,"//input[@id='password']")
        self.aadhar = (By.XPATH,"//input[@id='aadhar']")
        self.bloodgroupselect = (By.XPATH,"//select[@id='blood_group']")
        self.address = (By.XPATH,"//textarea[@id='address']")
        self.submitbtn = (By.XPATH,"//span[normalize-space()='Submit']")
        self.pftypeselect = (By.XPATH,"//select[@id='salary_type']")
        self.basic_salary_input = (By.XPATH,"//input[@id='total']")

    #     salary info box
        self.salary_info_box = (By.XPATH,"//button[normalize-space()='Salary Information']")

    #     validate employee creation



    def navigating_employee_list(self):
        self.wait_and_click(self.employee_maintenance_DD)
        self.wait_and_click(self.employee_list)
        time.sleep(1)
        self.wait_and_click(self.create_btn)

    def fill_basic_fields(self):
        print("🧪 Step 1: Typing employee name...")
        self.slow_typing(self.employee_name, "Sunil")

        print("🧪 Step 2: Selecting gender...")
        gender_dropdown_element = self.find_element(self.gender_dropdown)
        gender_dropdown = Select(gender_dropdown_element)
        gender_dropdown.select_by_visible_text("Male")
        time.sleep(1)

        print("🧪 Step 3: Selecting role...")
        role_dropdown_element = self.find_element(self.role_dropdown)
        role_dropdown = Select(role_dropdown_element)
        role_dropdown.select_by_visible_text("Employee")
        time.sleep(1)

        print("🧪 Step 4: Selecting employee type...")
        emp_type_element = self.find_element(self.emp_type_dropdown)
        emp_dropdown = Select(emp_type_element)
        emp_dropdown.select_by_visible_text("Permanent")
        time.sleep(1)

        print("🧪 Step 5: Selecting employee designation...")
        emp_desig_element = self.find_element(self.emp_desig_dropdown)
        emp_desig_DD = Select(emp_desig_element)
        emp_desig_DD.select_by_visible_text("Software Engineer")
        time.sleep(1)

        print("🧪 Step 6: Selecting employee experience...")
        emp_exp_element = self.find_element(self.emp_exp_dropdown)
        emp_exp_DD = Select(emp_exp_element)
        emp_exp_DD.select_by_visible_text("Fresher")
        time.sleep(1)

        print("🧪 Step 7: Typing official email...")
        self.enter_text(self.officialmail, "abc@gmail.com")

        print("🧪 Step 8: Typing personal email...")
        self.enter_text(self.personalmail, "def@gmail.com")

        print("🧪 Step 9: picking a data for joining date...")
        joiningdate_element = self.find_element(self.joining_date)
        joiningdate_element.send_keys("07-28-2025")
        time.sleep(2)

        print("🧪 Step 10: picking a data for DOB date...")
        joiningdate_element = self.find_element(self.DOBdate)
        joiningdate_element.send_keys("09-08-2000")
        time.sleep(2)

        print("🧪 Step 11: Entering a Phone number...")
        phone_number_element = self.find_element(self.phone_number)
        self.enter_text(phone_number_element,"8989898989")
        time.sleep(2)

        print("🧪 Step 12: Entering a Phone number...")
        password_element = self.find_element(self.password_input)
        self.enter_text(password_element,"Welcome@l1")
        time.sleep(2)


        print("🧪 Step 13: Entering a addhar number...")
        phone_number_element = self.find_element(self.aadhar)
        phone_number_element.send_keys("1234 5678 2345")
        time.sleep(2)

        print("🧪 Step 14: Selecting a blood group...")
        blood_grp_element = self.find_element(self.bloodgroupselect)
        blood_grp_DD = Select(blood_grp_element)
        blood_grp_DD.select_by_visible_text("A+")
        time.sleep(1)

        print("🧪 Step 15: Entering a  address...")
        address_element = self.find_element(self.address)
        address_element.send_keys(" test near test-nagar test")
        time.sleep(2)

        print("🧪 Step 15: submit without salary details to check validation...")
        submit_element = self.find_element(self.submitbtn)
        submit_element.click()
        time.sleep(2)

    def salary_info_field(self):
        print("Clicking salary info field...")
        self.salary_info_element = self.find_element(self.salary_info_box)
        self.salary_info_element.click()
        time.sleep(1)

        selectpf_element = self.find_element(self.pftypeselect)
        selectpf_DD = Select(selectpf_element)
        selectpf_DD.select_by_visible_text("PF not Applicable")

        print("entering a exact salary in salary details field...")
        basic_salary_ele =self.find_element(self.basic_salary_input)
        self.enter_text(basic_salary_ele , "19000")
        time.sleep(1)

        print("Clicking submit button...")
        submit_element = self.find_element(self.submitbtn)
        submit_element.click()
        time.sleep(10)

    def fill_basic_details_from_json(self):
        json_path = r"data/employee_data.json"

        # Read employee data from json file
        with open(json_path, "r", encoding="utf-8") as f:
            employee_data_list = json.load(f)

        def select_option_with_fallback(select_element, visible_text):
            """Select by visible text if available else select option at index 1"""
            select_obj = Select(select_element)
            options = [opt.text.strip() for opt in select_obj.options]
            if visible_text in options:
                select_obj.select_by_visible_text(visible_text)
            elif len(options) > 1:
                select_obj.select_by_index(1)  # second option as fallback
            else:
                # if only one or no options, select the first if possible
                select_obj.select_by_index(0)

        for index, employee_data in enumerate(employee_data_list):
            print(f"\n🔁 Processing Employee Row {index + 1}: {employee_data.get('Name', 'Unnamed')}")

            print("🧪 Step 1: Typing employee name...")
            self.slow_typing(self.employee_name, employee_data["Name"])

            print("🧪 Step 2: Selecting gender...")
            gender_dropdown_ele = self.find_element(self.gender_dropdown)
            select_option_with_fallback(gender_dropdown_ele, employee_data["Gender"])
            time.sleep(1)

            print("🧪 Step 3: Selecting role...")
            role_dropdown_ele = self.find_element(self.role_dropdown)
            select_option_with_fallback(role_dropdown_ele, employee_data["Role"])
            time.sleep(1)

            print("🧪 Step 4: Selecting employee type...")
            emp_type_dropdown_ele = self.find_element(self.emp_type_dropdown)
            select_option_with_fallback(emp_type_dropdown_ele, employee_data["Type"])
            time.sleep(1)

            print("🧪 Step 5: Selecting employee designation...")
            emp_desig_dropdown_ele = self.find_element(self.emp_desig_dropdown)
            select_option_with_fallback(emp_desig_dropdown_ele, employee_data["Designation"])
            time.sleep(1)

            print("🧪 Step 6: Selecting employee experience...")
            emp_exp_dropdown_ele = self.find_element(self.emp_exp_dropdown)
            select_option_with_fallback(emp_exp_dropdown_ele, employee_data["Experience"])
            time.sleep(1)

            print("🧪 Step 7: Typing official email...")
            self.enter_text(self.officialmail, employee_data["Official Email"])

            print("🧪 Step 8: Typing personal email...")
            self.enter_text(self.personalmail, employee_data["Personal Email"])

            print("🧪 Step 9: Typing joining date...")
            self.find_element(self.joining_date).send_keys(str(employee_data["Joining Date"]))
            time.sleep(1)

            print("🧪 Step 10: Typing DOB...")
            self.find_element(self.DOBdate).send_keys(str(employee_data["DOB"]))
            time.sleep(1)

            print("🧪 Step 11: Typing phone number...")
            self.enter_text(self.find_element(self.phone_number), str(employee_data["Phone"]))

            print("🧪 Step 12: Typing password...")
            self.enter_text(self.find_element(self.password_input), employee_data["Password"])

            print("🧪 Step 13: Typing Aadhar number...")
            self.find_element(self.aadhar).send_keys(employee_data["Aadhar Number"])
            time.sleep(1)

            print("🧪 Step 14: Selecting blood group...")
            bloodgroupselect_ele = self.find_element(self.bloodgroupselect)
            select_option_with_fallback(bloodgroupselect_ele, employee_data["Blood Group"])
            time.sleep(1)

            print("🧪 Step 15: Typing address...")
            self.find_element(self.address).send_keys(employee_data["Address"])
            time.sleep(1)

            # print("🧪 Step 16: Submit without salary info (validation check)...")
            # self.find_element(self.submitbtn).click()
            # time.sleep(2)

            # ➕ Call salary method per row
            self.salary_info_field_excel(employee_data)

    def fill_basic_details_from_excel(self):
        excel_path = r"data/Exceldatas/employee_creation.xlsx"

        try:
            # Read employee data from Excel file
            df = pd.read_excel(excel_path)
            # Ensure Result column exists
            if 'Result' not in df.columns:
                df['Result'] = ''

            def select_option_with_fallback(select_element, visible_text):
                """Select by visible text if available else select option at index 1"""
                select_obj = Select(select_element)
                options = [opt.text.strip() for opt in select_obj.options]
                if visible_text in options:
                    select_obj.select_by_visible_text(visible_text)
                elif len(options) > 1:
                    select_obj.select_by_index(1)  # second option as fallback
                else:
                    select_obj.select_by_index(0)

            # Convert date columns to datetime with explicit format
            df['Joining Date'] = pd.to_datetime(df['Joining Date'], format='%d-%m-%Y', errors='coerce')
            df['DOB'] = pd.to_datetime(df['DOB'], format='%d-%m-%Y', errors='coerce')

            wait = WebDriverWait(self.driver, 10)  # Add WebDriverWait for better element handling

            for index, employee_data in df.iterrows():
                print(f"\n🔁 Processing Employee Row {index + 1}: {employee_data.get('Name', 'Unnamed')}")
                row_failed = False  # Track if any field fails for this employee

                try:
                    # Generate unique EmpID if not present or duplicate
                    if pd.isna(employee_data.get('EmpID')) or employee_data.get('EmpID') in df['EmpID'].iloc[
                        :index].values:
                        df.at[index, 'EmpID'] = f"EMP{uuid.uuid4().hex[:6].upper()}"

                    print("🧪 Step 1: Typing employee name...")
                    self.slow_typing(self.employee_name, str(employee_data["Name"]))

                    print("🧪 Step 2: Selecting gender...")
                    gender_dropdown_ele = wait.until(EC.element_to_be_clickable(self.gender_dropdown))
                    select_option_with_fallback(gender_dropdown_ele, str(employee_data["Gender"]))
                    time.sleep(1)

                    print("🧪 Step 3: Selecting role...")
                    role_dropdown_ele = wait.until(EC.element_to_be_clickable(self.role_dropdown))
                    select_option_with_fallback(role_dropdown_ele, str(employee_data["Role"]))
                    time.sleep(1)

                    print("🧪 Step 4: Selecting employee type...")
                    emp_type_dropdown_ele = wait.until(EC.element_to_be_clickable(self.emp_type_dropdown))
                    select_option_with_fallback(emp_type_dropdown_ele, str(employee_data["Type"]))
                    time.sleep(1)

                    print("🧪 Step 5: Selecting employee designation...")
                    emp_desig_dropdown_ele = wait.until(EC.element_to_be_clickable(self.emp_desig_dropdown))
                    select_option_with_fallback(emp_desig_dropdown_ele, str(employee_data["Designation"]))
                    time.sleep(1)

                    print("🧪 Step 6: Selecting employee experience...")
                    emp_exp_dropdown_ele = wait.until(EC.element_to_be_clickable(self.emp_exp_dropdown))
                    select_option_with_fallback(emp_exp_dropdown_ele, str(employee_data["Experience"]))
                    time.sleep(1)

                    print("🧪 Step 7: Typing official email...")
                    self.enter_text(self.officialmail, str(employee_data["Official Email"]))

                    print("🧪 Step 8: Typing personal email...")
                    personal_email_field = wait.until(
                        EC.element_to_be_clickable((By.XPATH, "//input[@id='personal_email']")))
                    personal_email_field.clear()  # Clear previous value to avoid overwrite
                    self.enter_text(personal_email_field, str(employee_data["Personal Email"]))

                    print("🧪 Step 9: Typing joining date...")
                    joining_date_field = wait.until(EC.element_to_be_clickable(self.joining_date))
                    joining_date_field.clear()
                    joining_date = employee_data["Joining Date"]
                    if pd.notna(joining_date):
                        formatted_joining_date = joining_date.strftime('%d-%m-%Y')
                        print(f"Debug: Sending Joining Date: {formatted_joining_date}")
                        joining_date_field.send_keys(formatted_joining_date)
                    else:
                        print("⚠️ Warning: Joining Date is missing or invalid, skipping...")
                    time.sleep(1)

                    print("🧪 Step 10: Typing DOB...")
                    dob_field = wait.until(EC.element_to_be_clickable(self.DOBdate))
                    dob_field.clear()
                    dob = employee_data["DOB"]
                    if pd.notna(dob):
                        formatted_dob = dob.strftime('%d-%m-%Y')
                        print(f"Debug: Sending DOB: {formatted_dob}")
                        dob_field.send_keys(formatted_dob)
                    else:
                        print("⚠️ Warning: DOB is missing or invalid, skipping...")
                    time.sleep(1)
                    print("🧪 Step 11: Typing phone number...")
                    self.enter_text(self.find_element(self.phone_number), str(employee_data["Phone"]))

                    print("🧪 Step 12: Typing password...")
                    self.enter_text(self.find_element(self.password_input), str(employee_data["Password"]))

                    print("🧪 Step 13: Typing Aadhar number...")
                    aadhar_field = wait.until(EC.element_to_be_clickable(self.aadhar))
                    aadhar_field.clear()
                    aadhar_field.send_keys(str(employee_data["Aadhar Number"]))
                    print(f"✅ Successfully entered Aadhar: {employee_data['Aadhar Number']}")

                    print("🧪 Step 14: Selecting blood group...")
                    bloodgroupselect_ele = wait.until(EC.element_to_be_clickable(self.bloodgroupselect))
                    select_option_with_fallback(bloodgroupselect_ele, str(employee_data["Blood Group"]))
                    time.sleep(1)

                    print("🧪 Step 15: Typing address...")
                    self.find_element(self.address).send_keys(str(employee_data["Address"]))
                    time.sleep(1)

                    # Integrated salary information handling
                    print("📥 Reading salary info from passed data...")
                    salary_box_element = wait.until(EC.element_to_be_clickable(self.salary_info_box))
                    self.driver.execute_script("arguments[0].scrollIntoView(true);", salary_box_element)
                    try:
                        salary_box_element.click()
                        print("💰 Clicking salary info field...")
                    except  ElementClickInterceptedException:
                        self.driver.switch_to.frame(self.driver.find_element(By.TAG_NAME, "iframe"))
                        salary_box_element = wait.until(EC.element_to_be_clickable(self.salary_info_box))
                        self.driver.execute_script("arguments[0].scrollIntoView(true);", salary_box_element)
                        salary_box_element.click()
                        self.driver.switch_to.default_content()
                        print("💰 Clicking salary info field... (handled iframe)")
                    time.sleep(1)

                    print("💰 Selecting PF Type...")
                    selectpf_element = wait.until(EC.element_to_be_clickable(self.pftypeselect))
                    select_option_with_fallback(selectpf_element, employee_data.get("PF Type", "Yes"))

                    print("💰 Entering basic salary...")
                    basic_salary_ele = wait.until(EC.element_to_be_clickable(self.basic_salary_input))
                    basic_salary_ele.clear()
                    self.enter_text(basic_salary_ele, str(employee_data.get("Basic Salary", "25000")))
                    print(f"✅ Successfully entered basic salary: {employee_data.get('Basic Salary', '25000')}")
                    time.sleep(1)

                    print("💾 Clicking submit button...")
                    submit_element = wait.until(EC.element_to_be_clickable(self.submitbtn))
                    submit_element.click()
                    time.sleep(10)  # Wait for page to process submission

                    # Check if employee creation was successful
                    if self.driver.current_url == "https://smiligencehr.itsfortesza.com/user":
                        print("✅ Employee created successfully!")
                        df.at[index, 'Result'] = 'Pass'
                        print("\n✅ Successfully processed employee data (Pass):")
                        print("----------------------------------------")
                        for column in df.columns:
                            if column != 'Result':
                                print(f"{column}: {employee_data[column]}")
                        print("----------------------------------------")
                        self.wait_and_click(self.create_btn)  # Move to create new employee
                    else:
                        print("⚠️ Stuck in the same page - unexpected error or validation issue.")
                        df.at[index, 'Result'] = 'Fail'
                        self.driver.back()
                        self.wait_and_click(self.create_btn)

                    # Mark as Fail if row_failed is True, otherwise rely on submission check
                    if row_failed and df.at[index, 'Result'] != 'Pass':
                        df.at[index, 'Result'] = 'Fail'

                except Exception as e:
                    print(f"❌ Error processing employee {employee_data.get('Name', 'Unnamed')}: {str(e)}")
                    df.at[index, 'Result'] = 'Fail'

                finally:
                    # Save the updated DataFrame with results back to Excel
                    output_path = r"data/employee_data_with_results.xlsx"
                    df.to_excel(output_path, index=False)
                    print(f"📊 Results saved to {output_path}")

        except FileNotFoundError:
            print(f"❌ Excel file not found at {excel_path}")
        except Exception as e:
            print(f"❌ Error reading Excel file: {str(e)}")






































