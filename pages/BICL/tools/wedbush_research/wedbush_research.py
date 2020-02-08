from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import re
from config_globals import *

class wedbush_research():

    def __init__(self, driver):
        self.driver = driver

    def Page_Elements(self):

        return self

    # Actions

    def validate_hamburger_menu_clickable(self, test_case_ID, browser, env, time_stamp):
        hamburger_menu = self.driver.find_element(By.ID, "hide-menu")
        try:
            actions = ActionChains(self.driver)
            actions.move_to_element(hamburger_menu).click().perform()
        except AssertionError:
            screenshot_name = "FAIL" + "_" + test_case_ID + "_" + browser + "_" + env + "_" + time_stamp + ".png"
            saved_screenshot_location = str(screenshot_directory / screenshot_name)
            self.driver.get_screenshot_as_file(saved_screenshot_location)
            raise