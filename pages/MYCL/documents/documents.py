from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from config_globals import *

class documents():

    def __init__(self, driver):
        self.driver = driver

    def Page_Elements(self):

        # Monthly Statements
        self.monthly_statements = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/ul/li[1]/a")

        # Confirms
        self.confirms = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/ul/li[2]/a")

        # Tax Statements
        self.tax_statements = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/ul/li[3]/a")

        # Shareholder Materials
        self.shareholder_materials = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/ul/li[4]/a")

        return self

    # Actions

    def click_confirms(self):
        documents.Page_Elements(self).confirms.click()

    def click_tax_statements(self):
        documents.Page_Elements(self).tax_statements.click()

    def click_shareholder_materials(self):
        documents.Page_Elements(self).shareholder_materials.click()

    def click_monthly_statements(self):
        documents.Page_Elements(self).monthly_statements.click()

    def verify_monthly_statements_displays(self, test_case_ID, browser, env, time_stamp):
        try:
            documents.Page_Elements(self).monthly_statements.click()
        except NoSuchElementException:
            screenshot_name = "FAIL" + "_" + test_case_ID + "_" + browser + "_" + env + "_" + time_stamp + ".png"
            saved_screenshot_location = str(screenshot_directory / screenshot_name)
            self.driver.get_screenshot_as_file(saved_screenshot_location)
            raise