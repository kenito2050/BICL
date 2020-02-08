from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
import re
import textparser
from config_globals import *

class account_search_modal():

    def __init__(self, driver):
        self.driver = driver

    def Page_Elements(self):

        # Account Search Tab
        # self.account_search_tab = self.driver.find_element(By.XPATH, "/html/body/div[20]/div[2]/div/div/ul/li[1]/a")

        # Security Description Tab
        # self.security_description_tab = self.driver.find_element(By.XPATH, "/html/body/div[21]/div[2]/div/div/ul/li[2]/a")

        return self

    # Actions

    def click_account_search_tab(self):
        account_search_tab = self.driver.find_element(By.XPATH, "/html/body/div[21]/div[2]/div/div/ul/li[1]/a")
        account_search_tab.click()

    def click_security_description_tab(self):
        security_description_tab = self.driver.find_element(By.XPATH, "/html/body/div[21]/div[2]/div/div/ul/li[2]/a")
        security_description_tab.click()

    def input_security(self, security_text):
        security_field = self.driver.find_element(By.XPATH, "/html/body/div[21]/div[2]/div/div/div/div[2]/div/form/div/input")
        security_field.click()
        security_field.send_keys(security_text)

    def click_go_button(self):
        go_button = self.driver.find_element(By.XPATH, "/html/body/div[21]/div[2]/div/div/div/div[2]/div/form/div/button")
        go_button.click()

    def click_account_search_go_button(self):
        go_button = self.driver.find_element(By.XPATH, "/html/body/div[21]/div[2]/div/div/div/div[1]/div/form/div/button")
        go_button.click()

    def close_account_search_modal(self):
        account_search_modal_close_button = self.driver.find_element(By.XPATH, "/html/body/div[21]/div[1]/div/a[2]/span")
        account_search_modal_close_button.click()

    def input_value_in_name_field(self, test_data):
        name_field = self.driver.find_element(By.ID, "accountSearchName")
        name_field.click()
        name_field.clear()
        name_field.send_keys(test_data)

    def input_NULL_value_in_name_field(self):
        name_field = self.driver.find_element(By.ID, "accountSearchName")
        name_field.click()
        name_field.clear()

    def input_value_in_ssn_field(self, test_data):
        ssn_field = self.driver.find_element(By.XPATH, "/html/body/div[21]/div[2]/div/div/div/div[1]/div/form/div/span[1]/input")
        ssn_field.click()
        ssn_field.send_keys(test_data)

    def clear_value_in_rep_code_field(self):
        rep_code_field = self.driver.find_element(By.XPATH, "/html/body/div[21]/div[2]/div/div/div/div[1]/div/form/div/span[2]/span/input")
        rep_code_field.click()
        rep_code_field.clear()

    def input_value_in_rep_code_field(self, test_data):
        rep_code_field = self.driver.find_element(By.XPATH, "/html/body/div[21]/div[2]/div/div/div/div[1]/div/form/div/span[2]/span/input")
        rep_code_field.click()
        rep_code_field.send_keys(test_data)

    def verify_fields_blank_name(self, test_case_ID, browser, env, time_stamp):
        name_field_value = self.driver.find_element(By.ID, "accountSearchName").get_attribute("value")
        field_filled = True
        if name_field_value == '':
            field_filled = False

        try:
            assert field_filled is False
        except AssertionError:
            screenshot_name = "FAIL" + "_" + test_case_ID + "_" + browser + "_" + env + "_" + time_stamp + ".png"
            saved_screenshot_location = str(screenshot_directory / screenshot_name)
            self.driver.get_screenshot_as_file(saved_screenshot_location)
            raise


    def verify_ssn_field_blank(self, test_case_ID, browser, env, time_stamp):
        ssn_field_value = self.driver.find_element(By.XPATH, "/html/body/div[21]/div[2]/div/div/div/div[1]/div/form/div/span[1]/input").get_attribute("value")
        field_filled = True
        if ssn_field_value == '':
            field_filled = False

        try:
            assert field_filled is False
        except AssertionError:
            screenshot_name = "FAIL" + "_" + test_case_ID + "_" + browser + "_" + env + "_" + time_stamp + ".png"
            saved_screenshot_location = str(screenshot_directory / screenshot_name)
            self.driver.get_screenshot_as_file(saved_screenshot_location)
            raise

    def verify_rep_code_field_blank(self, test_case_ID, browser, env, time_stamp):
        rep_code_field_value = self.driver.find_element(By.XPATH, "/html/body/div[21]/div[2]/div/div/div/div[1]/div/form/div/span[2]/span/input").get_attribute("value")
        field_filled = True
        if rep_code_field_value == '':
            field_filled = False

        try:
            assert field_filled is False
        except AssertionError:
            screenshot_name = "FAIL" + "_" + test_case_ID + "_" + browser + "_" + env + "_" + time_stamp + ".png"
            saved_screenshot_location = str(screenshot_directory / screenshot_name)
            self.driver.get_screenshot_as_file(saved_screenshot_location)
            raise

    def locate_click_account(self):
        regex = re.compile(r'\d\d\d\d\d\d\d\d')
        table = self.driver.find_element(By.XPATH, "/html/body/div[21]/div[2]/div/div/div/div[1]/div/div[1]/div/div[3]/table/tbody")
        rows = table.find_elements(By.TAG_NAME, "tr")
        for row in rows:
            cols = row.find_elements(By.TAG_NAME, "td")
            for col in cols:
                text_found = str(cols[0].text)
                account_number_string = str(regex.findall(text_found))
                print(account_number_string)
                account_number_to_click = account_number_string[2:10]
                print(account_number_to_click)
                if account_number_to_click in text_found:
                    acct_to_click = self.driver.find_element(By.LINK_TEXT, str(account_number_to_click))
                    acct_to_click.click()
                    break
                break
            break
        print("loop ended")