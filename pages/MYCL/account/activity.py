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


class activity():

    def __init__(self, driver):
        self.driver = driver

    def Page_Elements(self):

        # Activity Table
        self.activity_table = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div/ui-view/div/div[2]/div[3]/div/table")

        # trailer column
        # self.trailer_column = self.driver.find_element(By.XPATH, "//*[contains(@text,'Trailer')]")

        return self

# Actions

    def count_assert_number_columns_on_account_balances_table(self, test_case_ID, browser, env, time_stamp):
        columns = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[3]/div/div/ui-view/div/div[2]/div[3]/div/table/thead/tr/th")
        number_columns = len(columns)
        print(number_columns)
        time.sleep(1)
        try:
            assert number_columns == 13
        except AssertionError:
            screenshot_name = "FAIL" + "_" + test_case_ID + "_" + browser + "_" + env + "_" + time_stamp + ".png"
            saved_screenshot_location = str(screenshot_directory / screenshot_name)
            self.driver.get_screenshot_as_file(saved_screenshot_location)
            raise


    def verify_Trailer_Column_Exists(self, test_case_ID, browser, env, time_stamp):
        columns = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[3]/div/div/ui-view/div/div[2]/div[3]/div/table/thead/tr/th")
        text_displays = False
        for item in columns:
            text = columns[12].text
            if ("Trailer" in text):
                text_displays =True
                break
            print(text)
        try:
            assert text_displays is True
        except AssertionError:
            screenshot_name = "FAIL" + "_" + test_case_ID + "_" + browser + "_" + env + "_" + time_stamp + ".png"
            saved_screenshot_location = str(screenshot_directory / screenshot_name)
            self.driver.get_screenshot_as_file(saved_screenshot_location)
            raise