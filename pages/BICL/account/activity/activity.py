from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
import time
from config_globals import *

class activity():

    def __init__(self, driver):
        self.driver = driver

    def Page_Elements(self):

        self.activity_table = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div/ui-view/div/div[2]/div[4]/table/tbody")

        return self


    def verify_SEC_NO_Column_Exists(self, test_case_ID, browser, env, time_stamp):
        columns = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[3]/div/div/ui-view/div/div[2]/div[3]/div/table/thead/tr/th")
        text_displays = False
        for item in columns:
            text = columns[10].text
            if ("Sec No" in text):
                text_displays =True
                break
            print(text)
        try:
            assert text_displays is True
        except AssertionError:
            screenshot_name = "FAIL" + "_" + test_case_ID + "_" + browser + "_" + env + "_" + time_stamp + ".png"
            saved_screenshot_location = str(screenshot_directory / screenshot_name)
            self.driver.get_screenshot_as_file(saved_screenshot_location)
            raise

    def verify_SEC_NO_Column_Not_Displayed(self, test_case_ID, browser, env, time_stamp):
        # If SEC NO Column displays, mark errorDisplays "TRUE"
        # errorDisplays default is FALSE
        columns = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[3]/div/div/ui-view/div/div[2]/div[3]/div/table/tbody")
        columnDisplays = False

        for item in columns:
            text = columns[10].text
            if ("Sec No" in text):
                columnDisplays =True
                break
            print(text)

        try:
            assert columnDisplays is False
        except AssertionError:
            screenshot_name = "FAIL" + "_" + test_case_ID + "_" + browser + "_" + env + "_" + time_stamp + ".png"
            saved_screenshot_location = str(screenshot_directory / screenshot_name)
            self.driver.get_screenshot_as_file(saved_screenshot_location)
            raise

    def verify_data_formatting_correct(self, test_case_ID, browser, env, time_stamp):
        rows = activity.Page_Elements(self).activity_table.find_elements(By.TAG_NAME, "tr")
        values_filled = False
        for row in rows:
            cols = row.find_elements(By.TAG_NAME, "td")
            for col in cols:
                text_found = cols[4].text
                if ("SCE.B" in text_found):
                    values_filled = True
                    break

        try:
            assert values_filled is True
        except AssertionError:
            screenshot_name = "FAIL" + "_" + test_case_ID + "_" + browser + "_" + env + "_" + time_stamp + ".png"
            saved_screenshot_location = str(screenshot_directory / screenshot_name)
            self.driver.get_screenshot_as_file(saved_screenshot_location)
            raise