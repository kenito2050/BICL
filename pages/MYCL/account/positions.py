from selenium.webdriver.common.by import By
from config_globals import *

class positions():

    def __init__(self, driver):
        self.driver = driver

    def Page_Elements(self):

        # Table Header
        self.table_header = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div/ui-view/div/div/div[2]/div[3]/div/table")

        # Table
        self.table = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div/ui-view/div/div/div[2]/div[4]/table/tbody")

        # Price Column
        self.price_column = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div/ui-view/div/div/div[2]/div[4]/table/tbody/tr[1]/td[8]")

        return self

    # Actions

    def verify_values_display_in_Price_Column(self, test_case_ID, browser, env, time_stamp):
        rows = positions.Page_Elements(self).table.find_elements(By.TAG_NAME, "tr")
        values_filled = False
        for row in rows:
            cols = row.find_elements(By.TAG_NAME, "td")
            for col in cols:
                text_found = cols[8].text
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

    def verify_values_display_in_Change_Column(self, test_case_ID, browser, env, time_stamp):
        rows = positions.Page_Elements(self).table.find_elements(By.TAG_NAME, "tr")
        values_filled = False
        for row in rows:
            cols = row.find_elements(By.TAG_NAME, "td")
            for col in cols:
                text_found = cols[9].text
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

    def verify_Close_Price_Column_Displays(self, test_case_ID, browser, env, time_stamp):
        columns = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[3]/div/div/ui-view/div/div/div[2]/div[3]/div/table/thead/tr/th")
        text_displays = False
        for item in columns:
            text = columns[8].text
            if ("Close" in text):
                text_displays =True
                break
        try:
            assert text_displays is True
        except AssertionError:
            screenshot_name = "FAIL" + "_" + test_case_ID + "_" + browser + "_" + env + "_" + time_stamp + ".png"
            saved_screenshot_location = str(screenshot_directory / screenshot_name)
            self.driver.get_screenshot_as_file(saved_screenshot_location)
            raise