from selenium import webdriver
import pytest
import time
from config_globals import *
from pages.generic_page.generic_page import generic_page
from pages.ADMIN.admin import admin
from pages.ADMIN.navigation.Screens import Screens
from utilities.environments.environments_ADMIN import Environments_ADMIN
from utilities.date_time_generator.date_time_generator import date_time_generator
import pandas as pd
from urllib.parse import urlparse

class Test_login_Chrome:

    @pytest.mark.regression
    @pytest.mark.bicl

    def test_bICL_ADMIN_TOOL_ROLE_TEMPLATES_Confirm_text_does_not_display(self, browser, env):
        driver = browser

        # Create Time Stamp Variable (using Date Time Generator Class in utilities)
        dg = date_time_generator()
        time_stamp = dg.return_time_stamp()

        # This section reads in values from csv file using Pandas Library

        # Declare Test Case ID
        test_case_ID = 'QTML-T329'

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

        # env = "DEV"
        baseURL_Admin = Environments_ADMIN.return_environments(env)

        time.sleep(1)

        # Assemble Admin URL String with User Creds
        parse_object = urlparse(baseURL_Admin)
        fdqm = parse_object.netloc
        base_url = "https://" + username + ":" + password + "@" + fdqm

        # Navigate to Admin Page using Admin URL String
        driver.get(base_url)
        driver.maximize_window()

        # Navigate to Users
        screen_to_navigate_to_1 = "Users"
        screen_1 = Screens.return_screens(screen_to_navigate_to_1)
        # Get Current URL
        current_url = driver.current_url
        # Concatenate current URL with Screen to Navigate to
        nav_string_1 = current_url + screen_1
        # Go to Location
        driver.get(nav_string_1)

        adm = admin(driver)

        time.sleep(3)

        # search for user account
        adm.enter_user_account_click_search(test_data1)

        time.sleep(3)

        # Scroll Down Page
        gp = generic_page(driver)

        gp.scroll_down()

        time.sleep(3)

        adm.check_uncheck_site_status()

        adm.check_uncheck_replay()

        # Save
        adm.click_save()

        # Set to 10 Or Greater
        time.sleep(20)

        # Take Screenshot 1
        screenshot_number = "1"
        time_stamp_1 = dg.return_time_stamp()
        gp.take_screenshot(test_case_ID, browser, control_point_1, screenshot_number, env, time_stamp_1)

        time.sleep(3)

        # Navigate to Role Templates
        screen_to_navigate_to_2 = "Role_Templates"
        screen_2 = Screens.return_screens(screen_to_navigate_to_2)
        # Get Current URL
        current_url = driver.current_url
        # Concatenate current URL with Screen to Navigate to
        nav_string_2 = current_url + screen_2
        # Go to Location
        driver.get(nav_string_2)

        time.sleep(5)

        # Navigate back to Users; Confirm Site Status & Replay Display
        driver.get(nav_string_1)

        time.sleep(3)

        # search for user account
        adm.enter_user_account_click_search(test_data1)

        # Set to 10 Or Greater
        time.sleep(20)

        # Attempt to Click "Replay Feature" Link
        adm.validate_replay_link_displays(test_case_ID, browser, env, time_stamp)

        time.sleep(5)

        # Take Screenshot 2
        screenshot_number = "2"
        time_stamp_2 = dg.return_time_stamp()
        gp.take_screenshot(test_case_ID, browser, control_point_2, screenshot_number, env, time_stamp_2)

        time.sleep(5)

        # Navigate back to Users; Confirm Site Status & Replay Display
        driver.get(nav_string_1)

        time.sleep(5)

        # Reset User Configuration to Original Setting

        # search for user account
        adm.enter_user_account_click_search(test_data1)

        time.sleep(3)

        gp.scroll_down()

        time.sleep(3)

        adm.check_uncheck_site_status()

        adm.check_uncheck_replay()

        # Save
        adm.click_save()

        time.sleep(20)

        # Take Screenshot 3
        screenshot_number = "3"
        time_stamp_3 = dg.return_time_stamp()
        gp.take_screenshot(test_case_ID, browser, control_point_3, screenshot_number, env, time_stamp_3)

        # Close Browser
        driver.quit()