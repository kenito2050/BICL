from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from config_globals import *

class account_transfer():

    def __init__(self, driver):
        self.driver = driver

    def Page_Elements(self):

        self.panel_title = self.driver.find_element(By.XPATH, './/span[@class = "ws-main-header-title ng-binding"]')

        return self

    # Validate that Correct Title Displays
    def validate_correct_text_displays(self, test_data, test_case_ID, browser, env, time_stamp):
        text_found = account_transfer.Page_Elements(self).panel_title.get_attribute("innerHTML")
        print(text_found)
        try:
            assert test_data in text_found
        except AssertionError:
            screenshot_name = "FAIL" + "_" + test_case_ID + "_" + browser + "_" + env + "_" + time_stamp + ".png"
            saved_screenshot_location = str(screenshot_directory / screenshot_name)
            self.driver.get_screenshot_as_file(saved_screenshot_location)
            raise