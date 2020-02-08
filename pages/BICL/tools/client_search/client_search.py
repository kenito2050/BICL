from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import re
from config_globals import *

class client_search():

    def __init__(self, driver):
        self.driver = driver

    def Page_Elements(self):

        # Rep Code
        self.rep_code_text_field = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div/ui-view/div/div[2]/form/div[1]/span/span/input")

        # Rep Code Drop Down
        self.rep_code_drop_down = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div/ui-view/div/div[2]/form/div[1]/span/span")

        # Criteria Drop Down
        self.criteria_drop_down = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div/ui-view/div/div[2]/form/div[2]/select")

        # greater than, less than, equal to
        # self.greater_than_less_than_or_equal  = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div/ui-view/div/div[2]/form/div[4]/select")

        # number
        # self.greater_than_less_than_or_equal = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div/ui-view/div/div[2]/form/div[4]/input")

        # Go button
        # self.greater_than_less_than_or_equal = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div/ui-view/div/div[2]/form/button")

        # self.regex = "(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})"

        return self

    # Actions

    def input_rep_code(self, rep_code):
        client_search.Page_Elements(self).rep_code_text_field.clear()
        client_search.Page_Elements(self).rep_code_text_field.click()
        client_search.Page_Elements(self).rep_code_text_field.send_keys(rep_code)

    def click_rep_code_field(self):
        client_search.Page_Elements(self).rep_code_text_field.click()

    def select_value_from_criteria_column(self):
        actions = ActionChains(self.driver)
        client_search.Page_Elements(self).criteria_drop_down.click()
        client_search.Page_Elements(self).criteria_drop_down.send_keys("Total Value")
        actions.send_keys(Keys.ENTER)
        actions.perform()

    def select_from_greater_than_less_than_equal(self):
        actions = ActionChains(self.driver)
        actions.move_to_element(self.driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div/ui-view/div/div[2]/form/div[4]/select")).click().perform()
        actions.send_keys(Keys.ARROW_DOWN)
        actions.send_keys(Keys.TAB)
        actions.perform()

    def input_number_value(self):
        number_field = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div/ui-view/div/div[2]/form/div[4]/input")
        number_field.click()
        number_field.send_keys("0")

    def click_go_button(self):
        go_button = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div/ui-view/div/div[2]/form/button")
        go_button.click()


    def verify_values_in_phone_column(self, test_case_ID, browser, env, time_stamp):
        table = self.driver.find_element(By.XPATH, "//div[@id='clientSearchGrid']/div[4]/table/tbody")
        rows = table.find_elements(By.TAG_NAME, "tr")
        values_filled = False
        for row in rows:
            cols = row.find_elements(By.TAG_NAME, "td")
            for col in cols:
                text_found = cols[3].text
                if ("-" in text_found):
                    values_filled = True
                    break

        try:
            assert values_filled is True
        except AssertionError:
            screenshot_name = "FAIL" + "_" + test_case_ID + "_" + browser + "_" + env + "_" + time_stamp + ".png"
            saved_screenshot_location = str(screenshot_directory / screenshot_name)
            self.driver.get_screenshot_as_file(saved_screenshot_location)
            raise

    def verify_values_in_bus_phone_column(self, test_case_ID, browser, env, time_stamp):
        table = self.driver.find_element(By.XPATH, "//div[@id='clientSearchGrid']/div[4]/table/tbody")
        rows = table.find_elements(By.TAG_NAME, "tr")
        values_filled = False
        for row in rows:
            cols = row.find_elements(By.TAG_NAME, "td")
            for col in cols:
                text_found = cols[4].text
                if ("-" in text_found):
                    values_filled = True
                    break

        try:
            assert values_filled is True
        except AssertionError:
            screenshot_name = "FAIL" + "_" + test_case_ID + "_" + browser + "_" + env + "_" + time_stamp + ".png"
            saved_screenshot_location = str(screenshot_directory / screenshot_name)
            self.driver.get_screenshot_as_file(saved_screenshot_location)
            raise

    def verify_values_in_account_number_column(self, test_case_ID, browser, env, time_stamp):
        table = self.driver.find_element(By.XPATH, "//div[@id='clientSearchGrid']/div[4]/table/tbody")
        rows = table.find_elements(By.TAG_NAME, "tr")
        values_filled = False
        for row in rows:
            cols = row.find_elements(By.TAG_NAME, "td")
            for col in cols:
                text_found = cols[0].text
                if re.findall(r"^\w+", text_found):
                    values_filled = True
                    break

        try:
            assert values_filled is True
        except AssertionError:
            screenshot_name = "FAIL" + "_" + test_case_ID + "_" + browser + "_" + env + "_" + time_stamp + ".png"
            saved_screenshot_location = str(screenshot_directory / screenshot_name)
            self.driver.get_screenshot_as_file(saved_screenshot_location)
            raise

    def verify_values_in_name_column(self, test_case_ID, browser, env, time_stamp):
        table = self.driver.find_element(By.XPATH, "//div[@id='clientSearchGrid']/div[4]/table/tbody")
        rows = table.find_elements(By.TAG_NAME, "tr")
        values_filled = False
        for row in rows:
            cols = row.find_elements(By.TAG_NAME, "td")
            for col in cols:
                text_found = cols[1].text
                if re.findall(r"^\w+", text_found):
                    values_filled = True
                    break

        try:
            assert values_filled is True
        except AssertionError:
            screenshot_name = "FAIL" + "_" + test_case_ID + "_" + browser + "_" + env + "_" + time_stamp + ".png"
            saved_screenshot_location = str(screenshot_directory / screenshot_name)
            self.driver.get_screenshot_as_file(saved_screenshot_location)
            raise

    def verify_values_in_total_column(self, test_case_ID, browser, env, time_stamp):
        table = self.driver.find_element(By.XPATH, "//div[@id='clientSearchGrid']/div[4]/table/tbody")
        rows = table.find_elements(By.TAG_NAME, "tr")
        values_filled = False
        for row in rows:
            cols = row.find_elements(By.TAG_NAME, "td")
            for col in cols:
                text_found = cols[2].text
                if re.findall(r"^\w+", text_found):
                    values_filled = True
                    break

        try:
            assert values_filled is True
        except AssertionError:
            screenshot_name = "FAIL" + "_" + test_case_ID + "_" + browser + "_" + env + "_" + time_stamp + ".png"
            saved_screenshot_location = str(screenshot_directory / screenshot_name)
            self.driver.get_screenshot_as_file(saved_screenshot_location)
            raise

    def verify_values_in_rep_code_column(self, test_case_ID, browser, env, time_stamp):
        table = self.driver.find_element(By.XPATH, "//div[@id='clientSearchGrid']/div[4]/table/tbody")
        rows = table.find_elements(By.TAG_NAME, "tr")
        values_filled = False
        for row in rows:
            cols = row.find_elements(By.TAG_NAME, "td")
            for col in cols:
                text_found = cols[5].text
                if re.findall(r"^\w+", text_found):
                    values_filled = True
                    break

        try:
            assert values_filled is True
        except AssertionError:
            screenshot_name = "FAIL" + "_" + test_case_ID + "_" + browser + "_" + env + "_" + time_stamp + ".png"
            saved_screenshot_location = str(screenshot_directory / screenshot_name)
            self.driver.get_screenshot_as_file(saved_screenshot_location)
            raise