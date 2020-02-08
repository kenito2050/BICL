from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from config_globals import *

class security_description_results():

    def __init__(self, driver):
        self.driver = driver

    def Page_Elements(self):

        # results_table
        self.results_table = self.driver.find_element(By.XPATH, "/html/body/div[21]/div[2]/div/div/div/div[2]/div/div/div/div[2]/table")

        # Prev. Close Price
        # self.prev_close_price = self.driver.find_element(By.XPATH, "/html/body/div[20]/div[2]/div/div/ul/li[1]/a")

        # Month End Price
        # self.month_end_price = self.driver.find_element(By.XPATH, "/html/body/div[21]/div[2]/div/div/ul/li[2]/a")

        return self

    # Actions

    def verify_text_displays(self, test_data, test_case_ID, browser, env, time_stamp):
        rows = security_description_results.Page_Elements(self).results_table.find_elements(By.TAG_NAME, "tr")
        values_filled = False
        for row in rows:
            cols = row.find_elements(By.TAG_NAME, "td")
            for col in cols:
                text_found = cols[0].text
                if (test_data in text_found):
                    values_filled = True
                    break

        try:
            assert values_filled is True
        except AssertionError:
            screenshot_name = "FAIL" + "_" + test_case_ID + "_" + browser + "_" + env + "_" + time_stamp + ".png"
            saved_screenshot_location = str(screenshot_directory / screenshot_name)
            self.driver.get_screenshot_as_file(saved_screenshot_location)
            raise
