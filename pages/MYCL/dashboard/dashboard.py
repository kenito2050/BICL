import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
import csv
from config_globals import *


class dashboard():

    def __init__(self, driver):
        self.driver = driver

    def Page_Elements(self):

        # Account Balances Table
        self.account_balances_table = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div/ui-view/div/div/div/div[4]/div[1]/table")

        # Account Balances Table - Rows

        # Account Balances Table - Columns

        # Account Balances Table Data
        self.account_balances_data = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[3]/div/div/ui-view/div/div/div/div[4]/div[1]/table")

        # Total Value Field
        self.total_value_field = self.driver.find_element(By.XPATH, "//div[@id='idForJS']/div[1]/span[3]/strong[1]/span")

        # Financial Advisor Field
        self.financial_advisor_field = self.driver.find_element(By.XPATH, "//div[@id='idForJS']/div[1]/span[3]/strong[2]/span")

        return self

    # Actions

    def verify_text_exists_in_Today_Column_old(self):
        account_balances_table = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div/ui-view/div/div/div/div[4]/div[1]/table")
        rows = account_balances_table.find_elements(By.TAG_NAME, "tr")
        for row in rows:
            cols = row.find_elements(By.TAG_NAME, "td")
            for col in cols:
                text_found = cols[1].text
                if ("." in text_found):
                    values_filled = True
                else:
                    values_filled = False
                print(values_filled)

    def count_assert_number_rows_on_account_balances_table(self, test_case_ID, browser, env, time_stamp):
        rows = dashboard.Page_Elements(self).account_balances_table.find_elements(By.TAG_NAME, "tr")
        number_rows = (len(rows))
        print(number_rows)
        time.sleep(1)
        try:
            assert number_rows == 10
        except AssertionError:
            screenshot_name = "FAIL" + "_" + test_case_ID + "_" + browser + "_" + env + "_" + time_stamp + ".png"
            saved_screenshot_location = str(screenshot_directory / screenshot_name)
            self.driver.get_screenshot_as_file(saved_screenshot_location)
            raise

    def count_assert_number_columns_on_account_balances_table(self, test_case_ID, browser, env, time_stamp):
        columns = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[3]/div/div/ui-view/div/div/div/div[4]/div[1]/table/thead/tr/th")
        number_columns = len(columns)
        print(number_columns)
        time.sleep(1)
        try:
            assert number_columns == 3
        except AssertionError:
            screenshot_name = "FAIL" + "_" + test_case_ID + "_" + browser + "_" + env + "_" + time_stamp + ".png"
            saved_screenshot_location = str(screenshot_directory / screenshot_name)
            self.driver.get_screenshot_as_file(saved_screenshot_location)
            raise

    def verify_text_exists_in_AS_OF_Column(self, test_case_ID, browser, env, time_stamp):
        rows = dashboard.Page_Elements(self).account_balances_table.find_elements(By.TAG_NAME, "tr")
        values_filled = False
        for row in rows:
            cols = row.find_elements(By.TAG_NAME, "td")
            for col in cols:
                text_found = cols[0].text
                if ("." in text_found):
                    values_filled = True
                    break

        try:
            assert values_filled is True
        except AssertionError:
            screenshot_name = "FAIL" + "_" + test_case_ID + "_" + browser + "_" + env + "_" + time_stamp + ".png"
            saved_screenshot_location = str(screenshot_directory / screenshot_name)
            self.driver.get_screenshot_as_file(saved_screenshot_location)
            raise

    def verify_text_exists_in_Today_Column(self, test_case_ID, browser, env, time_stamp):
        rows = dashboard.Page_Elements(self).account_balances_table.find_elements(By.TAG_NAME, "tr")
        values_filled = False
        for row in rows:
            cols = row.find_elements(By.TAG_NAME, "td")
            for col in cols:
                text_found = cols[1].text
                if ("." in text_found):
                    values_filled = True
                    break

        try:
            assert values_filled is True
        except AssertionError:
            screenshot_name = "FAIL" + "_" + test_case_ID + "_" + browser + "_" + env + "_" + time_stamp + ".png"
            saved_screenshot_location = str(screenshot_directory / screenshot_name)
            self.driver.get_screenshot_as_file(saved_screenshot_location)
            raise

    def verify_total_value_field_exists(self, test_case_ID, browser, env, time_stamp):
        try:
            self.total_value_field = self.driver.find_element(By.XPATH, "//div[@id='idForJS']/div[1]/span[3]/strong[1]/span")
        except NoSuchElementException:
            screenshot_name = "FAIL" + "_" + test_case_ID + "_" + browser + "_" + env + "_" + time_stamp + ".png"
            saved_screenshot_location = str(screenshot_directory / screenshot_name)
            self.driver.get_screenshot_as_file(saved_screenshot_location)
            return False
        return True

    def verify_financial_advisor_field_exists(self, test_case_ID, browser, env, time_stamp):
        try:
            self.financial_advisor_field = self.driver.find_element(By.XPATH, "//div[@id='idForJS']/div[1]/span[3]/strong[2]/span")
        except NoSuchElementException:
            screenshot_name = "FAIL" + "_" + test_case_ID + "_" + browser + "_" + env + "_" + time_stamp + ".png"
            saved_screenshot_location = str(screenshot_directory / screenshot_name)
            self.driver.get_screenshot_as_file(saved_screenshot_location)
            return False
        return True

