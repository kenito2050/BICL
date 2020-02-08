from selenium.webdriver.common.by import By
import re
from config_globals import *

class order_inquiry():

    def __init__(self, driver):
        self.driver = driver

    def Page_Elements(self):

        # Order Inquiry Table
        self.order_inquiry_table = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div/ui-view/div/div[2]/div[2]/div/div[5]/table/tbody")

        return self

    def verify_thousands_in_quantity_column(self, test_case_ID, browser, env, time_stamp):
        rows = order_inquiry.Page_Elements(self).order_inquiry_table.find_elements(By.TAG_NAME, "tr")
        values_correct = False
        for row in rows:
            cols = row.find_elements(By.TAG_NAME, "td")
            for col in cols:
                text_found = cols[4].text
                if re.findall(r"^(?:[+-]|\()?\$?\d+(?:,\d+)*(?:\.\d+)?\)?$", text_found):
                    values_correct = True
                    break

        try:
            assert values_correct is True
        except AssertionError:
            screenshot_name = "FAIL" + "_" + test_case_ID + "_" + browser + "_" + env + "_" + time_stamp + ".png"
            saved_screenshot_location = str(screenshot_directory / screenshot_name)
            self.driver.get_screenshot_as_file(saved_screenshot_location)
            raise

    def verify_integers_in_leaves_column(self, test_case_ID, browser, env, time_stamp):
        rows = order_inquiry.Page_Elements(self).order_inquiry_table.find_elements(By.TAG_NAME, "tr")
        values_correct = False
        for row in rows:
            cols = row.find_elements(By.TAG_NAME, "td")
            for col in cols:
                text_found = cols[11].text
                if re.findall(r"^[-+]?[0-9]+$", text_found):
                    values_correct = True
                    break

        try:
            assert values_correct is True
        except AssertionError:
            screenshot_name = "FAIL" + "_" + test_case_ID + "_" + browser + "_" + env + "_" + time_stamp + ".png"
            saved_screenshot_location = str(screenshot_directory / screenshot_name)
            self.driver.get_screenshot_as_file(saved_screenshot_location)
            raise

    def verify_integers_in_T_column(self, test_case_ID, browser, env, time_stamp):
        rows = order_inquiry.Page_Elements(self).order_inquiry_table.find_elements(By.TAG_NAME, "tr")
        values_correct = False
        for row in rows:
            cols = row.find_elements(By.TAG_NAME, "td")
            for col in cols:
                text_found = cols[10].text
                if re.findall(r"^[-+]?[0-9]+$", text_found):
                    values_correct = True
                    break

        try:
            assert values_correct is True
        except AssertionError:
            screenshot_name = "FAIL" + "_" + test_case_ID + "_" + browser + "_" + env + "_" + time_stamp + ".png"
            saved_screenshot_location = str(screenshot_directory / screenshot_name)
            self.driver.get_screenshot_as_file(saved_screenshot_location)
            raise