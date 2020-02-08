import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
import csv
from config_globals import *
from pages.BICL.login.LoginPage import LoginPage
from pages.MYCL.default_page.MYCL_default_page import MYCL_default_page
from pages.MYCL.default_page.user_drop_down.MYCL_user_drop_down import MYCL_user_drop_down
from pages.MYCL.left_panel.left_panel import left_panel
from pages.MYCL.profile_preferences.user_preferences import user_preferences
from pages.MYCL.documents.documents import documents
from utilities.environments.environments_MYCL import Environments_MYCL
from utilities.date_time_generator.date_time_generator import date_time_generator
import pandas as pd

class Test_login_Chrome:

    @pytest.mark.regression
    @pytest.mark.mycl

    def test_login_chrome(self, browser, env):

        driver = browser

        # Create Time Stamp Variable (using Date Time Generator Class in utilities)
        dg = date_time_generator()
        time_stamp = dg.return_time_stamp()

        # This section reads in values from csv file using Pandas Library

        # Declare Test Case ID
        test_case_ID = 'QTML-T177'

        # Declare csv directory
        df = pd.read_csv(csv_directory)

        # print(df)

        # Select Row where "Test_Case_ID" Column Matches the test_case_ID declared above (Line 31)
        # This is the row that contains the data values for this test scenario
        test_case_row = df.loc[df.Test_Case_ID == test_case_ID]

        # print(test_case_row)

        # Read in Values from "test_case_row" object
        test_scenario = test_case_row['Test_Scenario'].values[0]
        username = test_case_row['User'].values[0]
        password = test_case_row['Password'].values[0]
        browser = test_case_row['Browser'].values[0]
        account_number = test_case_row['account_number'].values[0]
        rep_code = test_case_row['rep_code'].values[0]
        test_data1 = test_case_row['test_data1'].values[0]
        test_data2 = test_case_row['test_data_2'].values[0]
        control_point_1 = test_case_row['control_point_1'].values[0]
        control_point_2 = test_case_row['control_point_2'].values[0]
        control_point_3 = test_case_row['control_point_3'].values[0]
        control_point_4 = test_case_row['control_point_4'].values[0]

        # To DEBUG, Uncomment this NEXT line AND Comment lines 13, 15 and 18. Also, SHIFT + TAB lines 17 - 86 (This will remove indents)
        # driver = webdriver.Chrome(str(CONFIG_PATH / 'chromedriver.exe'))

        ## Select Appropriate URL based on the Environment Value (env)

        # env = "UAT"
        baseURL = Environments_MYCL.return_environments(env)
        # baseURL = "https://beta.bi.dev.wedbus.com"

        driver.get(baseURL)
        driver.maximize_window()

        time.sleep(5)

        # Login to Site
        lp = LoginPage(driver)

        # Verify if page loads (username_field should be clickable), if not, throw exception and take screenshot
        try:
            username_field = lp.Page_Elements().driver.find_element_by_id("UserName")
            username_field.click()
        except NoSuchElementException:
            screenshot_name = "FAIL" + "_" + test_case_ID + "_" + browser + "_" + env + "_" + time_stamp + ".png"
            saved_screenshot_location = str(screenshot_directory / screenshot_name)
            driver.get_screenshot_as_file(saved_screenshot_location)
            raise

        lp.login(username, password)
        lp.click_login_button()

        time.sleep(10)

        # Take screenshot, save to utilities/test_results/screenshots
        screenshot_1 = test_case_ID + "_" + browser + "_" + env + "_" + "screenshot_1" + "_" + control_point_1 + "_" + time_stamp + ".png"
        saved_screenshot_location_1 = str(screenshot_directory / screenshot_1)
        driver.get_screenshot_as_file(saved_screenshot_location_1)

        time.sleep(10)

        # Navigate to Profile /Preferences

        lfp = left_panel(driver)

        lfp.click_profile_preferences()

        # Profile /Preferences - User Preferences Displays

        time.sleep(5)

        up = user_preferences(driver)

        # Update Page Preferences
        # Change Default Login Start Page to "Documents"

        up.set_default_landing_page_to_documents()

        # Click Save

        up.click_save_default_landing_page()

        time.sleep(5)

        # Take screenshot, save to utilities/test_results/screenshots
        screenshot_2 = test_case_ID + "_" + browser + "_" + env + "_" + "screenshot_2" + "_" + control_point_2 + "_" + time_stamp + ".png"
        saved_screenshot_location_2 = str(screenshot_directory / screenshot_2)
        driver.get_screenshot_as_file(saved_screenshot_location_2)

        # Logout

        # Click User Drop Down (on MYCL Default Page)
        mdp = MYCL_default_page(driver)
        mdp.click_user_drop_down()

        time.sleep(2)

        # Click Logout
        mudd = MYCL_user_drop_down(driver)
        mudd.click_logout()

        # Login

        driver.get(baseURL)
        driver.maximize_window()

        time.sleep(5)

        # Login to Site
        lp = LoginPage(driver)

        lp.login(username, password)
        lp.click_login_button()

        time.sleep(20)

        # Documents page should display

        # Take screenshot, save to utilities/test_results/screenshots
        screenshot_3 = test_case_ID + "_" + browser + "_" + env + "_" + "screenshot_3" + "_" + control_point_3 + "_" + time_stamp + ".png"
        saved_screenshot_location_3 = str(screenshot_directory / screenshot_3)
        driver.get_screenshot_as_file(saved_screenshot_location_3)

        # Assert Statement to confirm that Documents page displays

        doc = documents(driver)

        doc.verify_monthly_statements_displays(test_case_ID, browser, env, time_stamp)

        # Set to 20 - 25
        time.sleep(25)

        # Navigate to User Preferences

        lfp.click_profile_preferences()

        time.sleep(1)

        # Update Page Preferences
        # Change Default Login Start Page to "Account"

        up.set_default_landing_page_to_account()

        # Click Save

        up.click_save_default_landing_page()

        time.sleep(10)

        # Take screenshot, save to utilities/test_results/screenshots
        screenshot_4 = test_case_ID + "_" + browser + "_" + env + "_" + "screenshot_4" + "_" + control_point_4 + "_" + time_stamp + ".png"
        saved_screenshot_location_4 = str(screenshot_directory / screenshot_4)
        driver.get_screenshot_as_file(saved_screenshot_location_4)

        # Logout

        # Click User Drop Down (on MYCL Default Page)
        mdp = MYCL_default_page(driver)
        mdp.click_user_drop_down()

        time.sleep(2)

        # Click Logout
        mudd = MYCL_user_drop_down(driver)
        mudd.click_logout()

        time.sleep(1)

        driver.quit()