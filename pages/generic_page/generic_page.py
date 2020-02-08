from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from config_globals import *

class generic_page():

    def __init__(self, driver):
        self.driver = driver

    def Page_Elements(self):

        self.body = self.driver.find_element(By.XPATH, "/html/body")

        self.panel_title = self.driver.find_element(By.XPATH, './/span[@class = "ws-main-header-title ng-binding"]')

        return self

    def scroll_up(self):
        # body = self.driver.find_element_by_xpath('/html/body')
        generic_page.Page_Elements(self).body.click()
        ActionChains(self.driver).send_keys(Keys.PAGE_UP).perform()

    def scroll_down(self):
        # body = self.driver.find_element_by_xpath('/html/body')
        generic_page.Page_Elements(self).body.click()
        ActionChains(self.driver).send_keys(Keys.PAGE_DOWN).perform()

    def verify_error_on_page(self, test_case_ID, browser, env, time_stamp):

        # If Error Button displays, mark errorDisplays "TRUE"
        # errorDisplays default is FALSE
        errorDisplays = False

        if len(self.driver.find_elements(By.XPATH, "/html/body/div[1]/div/div/div/button")) > 0:
            errorDisplays = True
        else:
            print("No Error")

        # Try / Except Block to test if errorDisplays False
        # If True, throw exception, take screenshot and FAIL test

        try:
            assert errorDisplays is False
        except AssertionError:
            screenshot_name = "FAIL" + "_" + test_case_ID + "_" + browser + "_" + env + "_" + time_stamp + ".png"
            saved_screenshot_location = str(screenshot_directory / screenshot_name)
            self.driver.get_screenshot_as_file(saved_screenshot_location)
            raise


    def confirm_test_data_not_in_text(self, test_data, test_case_ID, browser, env, time_stamp):
        parsed_text = generic_page.Page_Elements(self).body.text
        # print(parsed_text)
        if (test_data in parsed_text):
            values_filled = True

            try:
                assert values_filled is True
            except AssertionError:
                screenshot_name = "FAIL" + "_" + test_case_ID + "_" + browser + "_" + env + "_" + time_stamp + ".png"
                saved_screenshot_location = str(screenshot_directory / screenshot_name)
                self.driver.get_screenshot_as_file(saved_screenshot_location)
                raise

    def confirm_test_data_on_panel(self, test_data, test_case_ID, browser, env, time_stamp):
        parsed_text = generic_page.Page_Elements(self).body.text
        # print(parsed_text)
        if (test_data in parsed_text):
            values_filled = True

            try:
                assert values_filled is True
            except AssertionError:
                screenshot_name = "FAIL" + "_" + test_case_ID + "_" + browser + "_" + env + "_" + time_stamp + ".png"
                saved_screenshot_location = str(screenshot_directory / screenshot_name)
                self.driver.get_screenshot_as_file(saved_screenshot_location)
                raise


    def take_screenshot(self, test_case_ID, browser, control_point, screenshot_number, env, time_stamp):
        # Take screenshot save to utilities/test_results/screenshots
        screenshot = test_case_ID + "_" + browser + "_" + env + "_" + "screenshot_" + screenshot_number + "_" + control_point + "_" + time_stamp + ".png"
        saved_screenshot_location = str(screenshot_directory / screenshot)
        self.driver.get_screenshot_as_file(saved_screenshot_location)


    # Timeout method for page to load, timeout set to 30 seconds
    def verify_page_loads(self, test_case_ID, browser, env, time_stamp):
        try:
            self.driver.set_page_load_timeout(30)
        except:
            screenshot_name = "FAIL" + "_" + test_case_ID + "_" + browser + "_" + env + "_" + time_stamp + ".png"
            saved_screenshot_location = str(screenshot_directory / screenshot_name)
            self.driver.get_screenshot_as_file(saved_screenshot_location)
            raise

    # Validate that Correct Title Displays
    def validate_correct_text_displays(self, test_data, test_case_ID, browser, env, time_stamp):
        text_found = generic_page.Page_Elements(self).panel_title.get_attribute("innerHTML")
        print(text_found)
        try:
            assert test_data in text_found
        except AssertionError:
            screenshot_name = "FAIL" + "_" + test_case_ID + "_" + browser + "_" + env + "_" + time_stamp + ".png"
            saved_screenshot_location = str(screenshot_directory / screenshot_name)
            self.driver.get_screenshot_as_file(saved_screenshot_location)
            raise