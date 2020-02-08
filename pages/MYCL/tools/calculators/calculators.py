from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from config_globals import *

class calculators():

    def __init__(self, driver):
        self.driver = driver

    def Page_Elements(self):

        return self

    # Actions

    def verify_text(self, test_data, test_case_ID, browser, env, time_stamp):
        text_found = False
        text_on_page = self.driver.find_element_by_tag_name('body').text
        # text_to_check = "Financial Calculators"
        if test_data in text_on_page:
            text_found = True
        else:
            print("Text Not Found")

        try:
            assert text_found is True
        except AssertionError:
            screenshot_name = "FAIL" + "_" + test_case_ID + "_" + browser + "_" + env + "_" + time_stamp + ".png"
            saved_screenshot_location = str(screenshot_directory / screenshot_name)
            self.driver.get_screenshot_as_file(saved_screenshot_location)
            raise