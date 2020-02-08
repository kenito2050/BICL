import pytest
from selenium import webdriver
import time
from config_globals import *
from pages.generic_page.generic_page import generic_page
from pages.BICL.login.LoginPage import LoginPage
from pages.BICL.default_page.user_drop_down.user_drop_down import user_drop_down
from pages.BICL.default_page.default_page import default_page
from pages.BICL.account_search_modal.account_search_modal import account_search_modal
from utilities.environments.environments_BICL import Environments_BICL
from utilities.date_time_generator.date_time_generator import date_time_generator
from pages.BICL.navigation.Screens import Screens
import pandas as pd

class Test_login_Chrome:

    @pytest.mark.regression
    @pytest.mark.bicl

    def test_login_chrome(self, browser, env):

        driver = browser

        # Create Time Stamp Variable (using Date Time Generator Class in utilities)
        dg = date_time_generator()
        time_stamp = dg.return_time_stamp()

        # This section reads in values from csv file using Pandas Library

        # Declare Test Case ID
        test_case_ID = 'QTML-T323'

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
        baseURL = Environments_BICL.return_environments(env)
        # baseURL = "https://beta.bi.dev.wedbus.com"

        driver.get(baseURL)
        driver.maximize_window()

        # Search for User Account

        time.sleep(5)

        # Login to Site
        lp = LoginPage(driver)

        gp = generic_page(driver)

        # Timeout method for page to load, timeout set to 30 seconds
        gp.verify_page_loads(test_case_ID, browser, env, time_stamp)

        lp.login(username, password)
        lp.click_login_button()

        time.sleep(10)

        # Take Screenshot 1
        screenshot_number = "1"
        time_stamp_1 = dg.return_time_stamp()
        gp.take_screenshot(test_case_ID, browser, control_point_1, screenshot_number, env, time_stamp_1)

        dp = default_page(driver)

        time.sleep(5)

        # Click Account Search Button
        dp.click_account_search_button()

        time.sleep(5)

        # Take Screenshot 2
        screenshot_number = "2"
        time_stamp_2 = dg.return_time_stamp()
        gp.take_screenshot(test_case_ID, browser, control_point_2, screenshot_number, env, time_stamp_2)

        time.sleep(5)

        asm = account_search_modal(driver)

        # input value in NAME field
        asm.input_value_in_name_field(test_data1)

        # input value in SSN Field
        # asm.input_value_in_ssn_field(test_data2)

        # input value in Rep Code
        asm.clear_value_in_rep_code_field()

        # Click GO (Search) Button
        asm.click_account_search_go_button()

        # set to 10 - 15
        time.sleep(15)

        asm.locate_click_account()

        # Take Screenshot 3
        screenshot_number = "3"
        time_stamp_3 = dg.return_time_stamp()
        gp.take_screenshot(test_case_ID, browser, control_point_3, screenshot_number, env, time_stamp_3)

        time.sleep(1)

        # Search for a previously searched for account
        dp.search_for_previously_searched_for_account()

        time.sleep(10)

        # Click GAIN & LOSS Icon
        dp.click_gain_loss_icon()

        time.sleep(5)

        # Enter "TEST" in NAME field of ACCOUNT SEARCH window
        asm.input_value_in_name_field(test_data2)

        # Click GO (Search) Button
        asm.click_account_search_go_button()

        time.sleep(15)

        # close account_search_modal
        asm.close_account_search_modal()

        time.sleep(5)

        # Open Account Search Modal, Perform Search with "TEST" in Name field
        dp.click_account_search_button_after_close()

        time.sleep(5)

        # Take Screenshot 4
        screenshot_number = "4"
        time_stamp_4 = dg.return_time_stamp()
        gp.take_screenshot(test_case_ID, browser, control_point_4, screenshot_number, env, time_stamp_4)

        time.sleep(5)

        # Confirm that fields blank in Account Search Modal

        asm.verify_fields_blank_name(test_case_ID, browser, env, time_stamp)

        time.sleep(5)

        asm.verify_ssn_field_blank(test_case_ID, browser, env, time_stamp)

        time.sleep(5)

        asm.verify_rep_code_field_blank(test_case_ID, browser, env, time_stamp)

        time.sleep(5)

        # input TEST in NAME field
        asm.input_value_in_name_field(test_data2)

        time.sleep(1)

        # Click GO (Search) Button
        asm.click_account_search_go_button()

        # Set to 15
        time.sleep(10)

        # close account_search_modal
        asm.close_account_search_modal()

        # LOGOUT Section

        # Click User Drop Down (on BICL Default Page)
        # dp.click_user_drop_down()
        #
        # time.sleep(2)

        # Click Logout
        # udd = user_drop_down(driver)
        # udd.click_logout()

        time.sleep(5)

        # Force Logout
        # Logout Workaround
        # Get current URL string, find base URL
        # Add logout_string to base_url to force logout
        current_url = driver.current_url
        slashparts = current_url.split('/')
        # Now join back the first three sections 'http:', '' and 'example.com'
        base_url = '/'.join(slashparts[:3]) + '/'

        logout_string = "user/login?logout=1"
        logout_screen = base_url + logout_string

        # Navigate to Logout Screen
        driver.get(logout_screen)

        # Close Browser
        driver.quit()