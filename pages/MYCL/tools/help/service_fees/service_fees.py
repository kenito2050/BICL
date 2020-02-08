from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import re
from config_globals import *

class service_fees():

    def __init__(self, driver):
        self.driver = driver

    def Page_Elements(self):

        # Wedbush Research

        # Quotes & Charts

        # Calculators

        # Help

        return self

    # Actions

    def verify_values_in_fee_column_first_section(self, test_case_ID, browser, env, time_stamp):
        table = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div/ui-view/div/div[2]/div[2]/div[2]/div[4]/div[2]/table[1]/tbody")
        rows = table.find_elements(By.TAG_NAME, "tr")
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

    def verify_values_in_fee_column_second_section(self, test_case_ID, browser, env, time_stamp):
        table = self.driver.find_element(By.XPATH,
                                         "/html/body/div[1]/div[3]/div/div/ui-view/div/div[2]/div[2]/div[2]/div[4]/div[2]/table[2]/tbody")
        rows = table.find_elements(By.TAG_NAME, "tr")
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

    def verify_values_in_fee_column_third_section(self, test_case_ID, browser, env, time_stamp):
        table = self.driver.find_element(By.XPATH,
                                         "/html/body/div[1]/div[3]/div/div/ui-view/div/div[2]/div[2]/div[2]/div[4]/div[2]/table[3]/tbody")
        rows = table.find_elements(By.TAG_NAME, "tr")
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