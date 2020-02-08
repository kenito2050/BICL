from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from config_globals import *

class validate_decimal():

    def __init__(self, driver):
        self.driver = driver

    def Page_Elements(self):

        return self


def verify_decimal(self, test_data, test_case_ID, browser, env, time_stamp):

    num_decimal_places = test_data[::-1].find('.')
    if num_decimal_places == 2:
        is_decimal = True
    else:
        is_decimal = False
    try:
        assert is_decimal is True
    except AssertionError:
        screenshot_name = "FAIL" + "_" + test_case_ID + "_" + browser + "_" + env + "_" + time_stamp + ".png"
        saved_screenshot_location = str(screenshot_directory / screenshot_name)
        self.driver.get_screenshot_as_file(saved_screenshot_location)
        raise