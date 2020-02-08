from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
import time
from config_globals import *

class balances():

    def __init__(self, driver):
        self.driver = driver

    def Page_Elements(self):

        # Table
        self.market_value_summary_table = self.driver.find_element(By.XPATH,
                                              "/html/body/div[1]/div[3]/div/div/ui-view/div/div[3]/div[2]/div[1]/div[1]/div[2]/table/tbody")


        self.cash_flow_summary_table = self.driver.find_element(By.XPATH,
                                              "/html/body/div[1]/div[3]/div/div/ui-view/div/div[3]/div[2]/div[1]/div[2]/div[2]/table/tbody")

        self.value_equity_summary_table = self.driver.find_element(By.XPATH,
                                                                "/html/body/div[1]/div[3]/div/div/ui-view/div/div[3]/div[2]/div[2]/div/div[2]/table/tbody")


        return self

    def validate_pdf_button(self, test_case_ID, browser, env, time_stamp):
        pdf_button_displays = False
        # Check if PDF Button Displays
        if len(self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[3]/div/div/ui-view/div/div[2]/div[5]/button")) > 0:
            pdf_button_displays = True
        else:
            print("Button not Displayed")
        time.sleep(1)
        try:
            assert pdf_button_displays is True
        except AssertionError:
            screenshot_name = "FAIL" + "_" + test_case_ID + "_" + browser + "_" + env + "_" + time_stamp + ".png"
            saved_screenshot_location = str(screenshot_directory / screenshot_name)
            self.driver.get_screenshot_as_file(saved_screenshot_location)
            raise

    def verify_values_display_in_Cash_Flow_Summary(self, test_case_ID, browser, env, time_stamp):
        rows = balances.Page_Elements(self).cash_flow_summary_table.find_elements(By.TAG_NAME, "tr")
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


    def verify_values_display_in_Value_Equity_Summary(self, test_case_ID, browser, env, time_stamp):
        rows = balances.Page_Elements(self).value_equity_summary_table.find_elements(By.TAG_NAME, "tr")
        values_filled = False
        for row in rows:
            cols = row.find_elements(By.TAG_NAME, "td")
            for col in cols:
                text_found = cols[0].text
                if ("%" in text_found):
                    values_filled = True
                    break

        try:
            assert values_filled is True
        except AssertionError:
            screenshot_name = "FAIL" + "_" + test_case_ID + "_" + browser + "_" + env + "_" + time_stamp + ".png"
            saved_screenshot_location = str(screenshot_directory / screenshot_name)
            self.driver.get_screenshot_as_file(saved_screenshot_location)
            raise


    def verify_values_display_in_Balances_Column(self, test_case_ID, browser, env, time_stamp):
        rows = balances.Page_Elements(self).market_value_summary_table.find_elements(By.TAG_NAME, "tr")
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