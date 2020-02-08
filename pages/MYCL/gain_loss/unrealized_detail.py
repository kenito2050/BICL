from selenium.webdriver.common.by import By
from config_globals import *

class gain_loss_unrealized_detail():

    def __init__(self, driver):
        self.driver = driver

    def Page_Elements(self):

        # Table Header
        self.table_header = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div/ui-view/div/div[2]/div[3]/div/table")

        # Table
        self.table = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div/ui-view/div/div[2]/div[4]/table/tbody")

        return self

    # Actions

    def verify_values_display_in_Price_Column(self, test_case_ID, browser, env, time_stamp):
        rows = gain_loss_unrealized_detail.Page_Elements(self).table.find_elements(By.TAG_NAME, "tr")
        values_filled = False
        for row in rows:
            cols = row.find_elements(By.TAG_NAME, "td")
            for col in cols:
                text_found = cols[7].text
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