from selenium import webdriver
import pytest
import time
import csv
from config_globals import *
from pages.generic_page.generic_page import generic_page
from pages.ADMIN.admin import admin
from pages.ADMIN.role_templates.role_templates import role_templates
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
        test_case_ID = 'QTML-T197'

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

        # Launch Admin Site
        # driver.get(baseURL_Admin)
        # driver.maximize_window()

        # Assemble Admin URL String with User Creds
        parse_object = urlparse(baseURL_Admin)
        fdqm = parse_object.netloc
        base_url = "https://" + username + ":" + password + "@" + fdqm

        # Navigate to Admin Page using Admin URL String
        driver.get(base_url)
        driver.maximize_window()

        time.sleep(1)

        # Navigate to Role Templates
        current_url = driver.current_url
        slashparts = current_url.split('/')
        base_url = '/'.join(slashparts[:3]) + '/'

        time.sleep(1)

        screen_to_navigate_to_1 = "Role_Templates"
        screen_1 = Screens.return_screens(screen_to_navigate_to_1)
        nav_string_1 = base_url + screen_1

        driver.get(nav_string_1)

        time.sleep(10)

        rt = role_templates(driver)

        # Select Developer
        rt.change_role_to_developer()

        # Scroll Down Page
        gp = generic_page(driver)

        gp.scroll_down()

        # Take screenshot and save to utilities/test_results/screenshots
        screenshot_1 = test_case_ID + "_" + browser + "_" + env + "_" + "screenshot_1" + "_" + control_point_1 + "_" + time_stamp + ".png"
        saved_screenshot_location_1 = str(screenshot_directory / screenshot_1)
        driver.get_screenshot_as_file(saved_screenshot_location_1)

        time.sleep(3)

        # Checkmark "X" and Save
        rt.checkmark_x_label()

        rt.click_update_button()

        time.sleep(1)

        # Navigate to Admin
        current_url_2 = driver.current_url
        slashparts_2 = current_url_2.split('/')
        base_url_2 = '/'.join(slashparts_2[:3]) + '/'

        screen_to_navigate_to_2 = "Users"
        screen_2 = Screens.return_screens(screen_to_navigate_to_2)
        nav_string_2 = base_url_2 + screen_2

        driver.get(nav_string_2)

        time.sleep(5)

        # Navigate to Role Templates
        driver.get(nav_string_1)

        time.sleep(5)

        # Select Developer
        rt.change_role_to_developer()

        gp.scroll_down()

        # Verify that checkmark persists
        rt.verify_x_label_checked(test_case_ID, browser, env, time_stamp)

        time.sleep(1)

        # Take screenshot save to utilities/test_results/screenshots
        screenshot_2 = test_case_ID + "_" + browser + "_" + env + "_" + "screenshot_2" + "_" + control_point_2 + "_" + time_stamp + ".png"
        saved_screenshot_location_2 = str(screenshot_directory / screenshot_2)
        driver.get_screenshot_as_file(saved_screenshot_location_2)

        time.sleep(5)

        # Reset Condition
        # Uncheck Checkmark and Save

        # Checkmark "X" and Save
        rt.checkmark_x_label()

        rt.click_update_button()

        time.sleep(5)

        # Take screenshot save to utilities/test_results/screenshots
        screenshot_3 = test_case_ID + "_" + browser + "_" + env + "_" + "screenshot_3" + "_" + control_point_3 + "_" + time_stamp + ".png"
        saved_screenshot_location_3 = str(screenshot_directory / screenshot_3)
        driver.get_screenshot_as_file(saved_screenshot_location_3)

        # Close Browser
        driver.quit()