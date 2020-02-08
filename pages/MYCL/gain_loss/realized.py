from selenium.webdriver.common.by import By
from config_globals import *

class realized():

    def __init__(self, driver):
        self.driver = driver

    def Page_Elements(self):

        # Table Header
        self.table_header = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div/ui-view/div/div[2]/div[3]/div/table")

        # Table
        self.table = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div/ui-view/div/div[2]/div[3]/div/table/tbody")

        return self

    # Actions

    def verify_Total_Displays(self, test_case_ID, browser, env, time_stamp):
        columns = self.driver.find_elements(By.XPATH,
                                            "/html/body/div[1]/div[3]/div/div/ui-view/div/div[2]/div[5]/div/table/tbody")
        text_displays = False
        for item in columns:
            text = columns[0].text
            if ("Total" in text):
                text_displays = True
                break
            break
        try:
            assert text_displays is True
        except AssertionError:
            screenshot_name = "FAIL" + "_" + test_case_ID + "_" + browser + "_" + env + "_" + time_stamp + ".png"
            saved_screenshot_location = str(screenshot_directory / screenshot_name)
            self.driver.get_screenshot_as_file(saved_screenshot_location)
            raise