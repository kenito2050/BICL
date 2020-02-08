from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import re
from config_globals import *

class acats():

    def __init__(self, driver):
        self.driver = driver

    def Page_Elements(self):

        return self

    # Actions

    def validate_go_button_clickable(self, test_case_ID, browser, env, time_stamp):
        go_button = self.driver.find_element(By.ID, "cmdGo")
        try:
            go_button.click()
        except AssertionError:
            screenshot_name = "FAIL" + "_" + test_case_ID + "_" + browser + "_" + env + "_" + time_stamp + ".png"
            saved_screenshot_location = str(screenshot_directory / screenshot_name)
            self.driver.get_screenshot_as_file(saved_screenshot_location)
            raise