from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from config_globals import *

class overview():

    def __init__(self, driver):
        self.driver = driver

    def Page_Elements(self):

        # Table
        self.summary_of_accounts_table = self.driver.find_element(By.XPATH,
                                              "/html/body/div[1]/div[3]/div/div/ui-view/div/div/div/div[3]/div[1]/div[2]/table/tbody")

        return self

    def verify_decimals_in_margin_balance_total(self, test_case_ID, browser, env, time_stamp):
        rows = overview.Page_Elements(self).summary_of_accounts_table.find_elements(By.TAG_NAME, "tr")
        is_decimal = False
        for row in rows:
            cols = row.find_elements(By.TAG_NAME, "td")
            for col in cols:
                text_found = cols[2].text
                num_decimal_places = text_found[::-1].find('.')
                if num_decimal_places == 2:
                    is_decimal = True
                    break

                try:
                    assert is_decimal is True
                except AssertionError:
                    screenshot_name = "FAIL" + "_" + test_case_ID + "_" + browser + "_" + env + "_" + time_stamp + ".png"
                    saved_screenshot_location = str(screenshot_directory / screenshot_name)
                    self.driver.get_screenshot_as_file(saved_screenshot_location)
                    raise

    def verify_decimals_in_net_market_value_total(self, test_case_ID, browser, env, time_stamp):
        rows = overview.Page_Elements(self).summary_of_accounts_table.find_elements(By.TAG_NAME, "tr")
        is_decimal = False
        for row in rows:
            cols = row.find_elements(By.TAG_NAME, "td")
            for col in cols:
                text_found = cols[4].text
                num_decimal_places = text_found[::-1].find('.')
                if num_decimal_places == 2:
                    is_decimal = True
                    break

                try:
                    assert is_decimal is True
                except AssertionError:
                    screenshot_name = "FAIL" + "_" + test_case_ID + "_" + browser + "_" + env + "_" + time_stamp + ".png"
                    saved_screenshot_location = str(screenshot_directory / screenshot_name)
                    self.driver.get_screenshot_as_file(saved_screenshot_location)
                    raise

    def verify_decimals_in_funds_available_total(self, test_case_ID, browser, env, time_stamp):
        rows = overview.Page_Elements(self).summary_of_accounts_table.find_elements(By.TAG_NAME, "tr")
        is_decimal = False
        for row in rows:
            cols = row.find_elements(By.TAG_NAME, "td")
            for col in cols:
                text_found = cols[6].text
                num_decimal_places = text_found[::-1].find('.')
                if num_decimal_places == 2:
                    is_decimal = True
                    break

                try:
                    assert is_decimal is True
                except AssertionError:
                    screenshot_name = "FAIL" + "_" + test_case_ID + "_" + browser + "_" + env + "_" + time_stamp + ".png"
                    saved_screenshot_location = str(screenshot_directory / screenshot_name)
                    self.driver.get_screenshot_as_file(saved_screenshot_location)
                    raise