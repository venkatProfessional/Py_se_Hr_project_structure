from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CMS_page(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    cms_xpath = (By.XPATH,"//div[@data-i18n='CMS Pages']")
    page_title = (By.XPATH,"//input[@id='pageTitle']")
    page_slug = (By.XPATH,"//input[@id='pageSlug']")
    page_content = (By.XPATH,"//div[@aria-label='Editor editing area: main']//p")
    select_visible_on = (By.XPATH,"//select[@name='visible_on']")
    select_status = (By.XPATH,"//select[@name='status']")

    create_cms_page = (By.XPATH,"//a[normalize-space()='Create CMS Page']")
    page_title =(By.XPATH,"//input[@id='pageTitle']")

    cms_submit_btn =(By.XPATH,"//span[normalize-space()='Submit']")


    def navigate_to_cms_page(self):
        print("navigating to cms page")
        self.scroll_to_element(self.cms_xpath)
        self.wait_and_click(self.cms_xpath)

    def implementing_cms_create(self):
        print("implementing cms create")
        self.wait_and_click(self.create_cms_page)
        self.enter_text(self.page_title,"test")
        self.enter_text(self.page_content,"test")
        self.robust_select_dropdown_option(self.select_visible_on,"Web",2,1)
        self.robust_select_dropdown_option(self.select_status,"Active",2,1)
        self.scroll_to_element(self.cms_submit_btn)
        self.wait_and_click(self.cms_submit_btn)



