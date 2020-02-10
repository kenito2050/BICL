from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import pytest
import time
import csv
from config_globals import *
from pages.ADMIN.admin import admin
from pages.BICL.login.LoginPage import LoginPage
from pages.BICL.default_page.user_drop_down.user_drop_down import user_drop_down
from pages.BICL.default_page.default_page import default_page
from pages.BICL.account_info.account_info import account_info
from pages.BICL.account_info.document_drop_down import document_drop_down
from utilities.environments.environments_ADMIN import Environments_ADMIN
from utilities.environments.environments_BICL import Environments_BICL
from utilities.date_time_generator.date_time_generator import date_time_generator
from utilities.date_validator.date_validator import date_validator
import pandas as pd
from urllib.parse import urlparse

class Test_login_Chrome:

    @pytest.mark.regression
    @pytest.mark.bicl

    def test_login_chrome(self, browser, env):

        driver = browser

        # Create Time Stamp Variable (using Date Time Generator Class in utilities)
        dg = date_time_generator()
        time_stamp = dg.return_time_stamp()

        # Create a valid date (1 month ago)
        date_previous_month = dg.return_date_one_month_ago()
        dv = date_validator()
        valid_date = dv.return_valid_date(date_previous_month).strftime("%m-%d-%Y")

        # This section reads in values from csv file using Pandas Library

        # Declare Test Case ID
        test_case_ID = 'QTML-T100'

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
        baseURL_Admin = Environments_ADMIN.return_environments(env)
        # baseURL = "https://beta.bi.dev.wedbus.com"

        # Assemble Admin URL String with User Creds
        parse_object = urlparse(baseURL_Admin)
        ffqdn = parse_object.netloc
        base_url = "https://" + username + ":" + password + "@" + fqdn

        # Navigate to Admin Page using Admin URL String
        driver.get(base_url)
        driver.maximize_window()

        # Workaround to Navigate to User Admin Screen
        current_url = driver.current_url
        slashparts = current_url.split('/')
        # Now join back the first three sections 'http:', '' and 'example.com'
        base_url = '/'.join(slashparts[:3]) + '/'
        manage_user_string = "ManageUser.aspx"
        manage_user_screen = base_url + manage_user_string

        # Navigate to Manage User Screen
        driver.get(manage_user_screen)

        time.sleep(5)

        adm = admin(driver)

        # search for user account
        adm.enter_user_account_click_search(username)

        time.sleep(5)

        adm.click_first_name_tab_3_times()

        time.sleep(5)

        # change to System Used to "P3"
        adm.change_system_used_P3()

        time.sleep(5)

        # click Save
        adm.click_save()

        time.sleep(5)

        # Launch BICL Site
        # env = "UAT"
        baseURL_BICL = Environments_BICL.return_environments(env)
        # baseURL = "https://beta.bi.dev.wedbus.com"

        time.sleep(5)

        # driver.get(baseURL_BICL)
        # driver.maximize_window()

        # Assemble Admin URL String with User Creds
        parse_object = urlparse(baseURL_Admin)
        fdqm = parse_object.netloc
        base_url = "https://" + username + ":" + password + "@" + fdqm

        # Navigate to Admin Page using Admin URL String
        driver.get(base_url)
        driver.maximize_window()

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

        # Take screenshot after login and save to utilities/test_results/screenshots
        screenshot_1 = test_case_ID + "_" + browser + "_" + env + "_" + "screenshot_1" + "_" + control_point_1 + "_" + time_stamp + ".png"
        saved_screenshot_location_1 = str(screenshot_directory / screenshot_1)
        driver.get_screenshot_as_file(saved_screenshot_location_1)

        dp = default_page(driver)

        # Timeout method for page to load, timeout set to 30 seconds
        try:
            driver.set_page_load_timeout(30)
        except:
            screenshot_name = "FAIL" + "_" + test_case_ID + "_" + browser + "_" + env + "_" + time_stamp + ".png"
            saved_screenshot_location = str(screenshot_directory / screenshot_name)
            driver.get_screenshot_as_file(saved_screenshot_location)
            raise

        time.sleep(10)

        # Enter Account Number and click Search
        dp.enter_account_number_search(account_number)

        time.sleep(5)

        # Confirm that No Content displays in the ACCOUNT INFO Screen
        # Click Account Info link

        dp.click_account_info_button()

        time.sleep(10)

        ai = account_info(driver)

        # Account Info Screen -- Should be BLANK

        # Take screenshot of ACCOUNT INFO and save to utilities/test_results/screenshots
        screenshot_2 = test_case_ID + "_" + browser + "_" + env + "_" + "screenshot_2" + "_" + control_point_2 + "_" + time_stamp + ".png"
        saved_screenshot_location_2 = str(screenshot_directory / screenshot_2)
        driver.get_screenshot_as_file(saved_screenshot_location_2)

        time.sleep(1)

        errorDisplays = False

        # Check if Error Modal Displays
        if len(driver.find_elements(By.XPATH, "/html/body/div[1]/div/div/div/button")) > 0:
            errorDisplays = True
        else:
            print("No Error")

        time.sleep(1)

        # Try / Except Block to test if errorDisplays False
        # If True, throw exception, take screenshot and FAIL test

        try:
            assert errorDisplays is False
        except AssertionError:
            screenshot_name = "FAIL" + "_" + test_case_ID + "_" + browser + "_" + env + "_" + time_stamp + ".png"
            saved_screenshot_location = str(screenshot_directory / screenshot_name)
            driver.get_screenshot_as_file(saved_screenshot_location)
            raise

        time.sleep(1)

        # LOGOUT Section
        # TODO: Move Logout methods to Logout Class

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

        # Launch Admin Site
        driver.get(baseURL_Admin)
        driver.maximize_window()

        # Workaround to Navigate to User Admin Screen
        current_url = driver.current_url
        slashparts = current_url.split('/')
        # Now join back the first three sections 'http:', '' and 'example.com'
        base_url = '/'.join(slashparts[:3]) + '/'
        manage_user_string = "ManageUser.aspx"
        manage_user_screen = base_url + manage_user_string

        # Navigate to Manage User Screen
        driver.get(manage_user_screen)

        time.sleep(5)

        # search for user account
        adm.enter_user_account_click_search(username)

        time.sleep(5)

        adm.click_first_name_tab_3_times()

        time.sleep(5)

        # change to System Used to "BETA"
        adm.change_system_used_BETA()

        time.sleep(5)

        # click Save
        adm.click_save()

        time.sleep(5)

        # Launch BICL Site
        driver.get(baseURL_BICL)
        driver.maximize_window()

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

        # Take screenshot after login and save to utilities/test_results/screenshots
        screenshot_3 = test_case_ID + "_" + browser + "_" + env + "_" + "screenshot_3" + "_" + control_point_3 + "_" + time_stamp + ".png"
        saved_screenshot_location_3 = str(screenshot_directory / screenshot_3)
        driver.get_screenshot_as_file(saved_screenshot_location_3)

        time.sleep(5)

        dp = default_page(driver)

        time.sleep(10)

        # Enter Account Number and click Search
        dp.enter_account_number_search(account_number)

        dp.click_account_info_button()

        time.sleep(10)

        ai = account_info(driver)

        # Account Info Screen

        # Select "Documents" from VIEW Drop Down
        ai.select_documents()

        time.sleep(30)

        ddd = document_drop_down(driver)

        # Select MONTHLY STATEMENTS
        ddd.select_monthly_statements()

        time.sleep(20)

        # Take screenshot of ACCOUNT INFO and save to utilities/test_results/screenshots
        screenshot_4 = test_case_ID + "_" + browser + "_" + env + "_" + "screenshot_4" + "_" + control_point_4 + "_" + time_stamp + ".png"
        saved_screenshot_location_4 = str(screenshot_directory / screenshot_4)
        driver.get_screenshot_as_file(saved_screenshot_location_4)

        # LOGOUT Section

        # Click User Drop Down (on BICL Default Page)
        dp.click_user_drop_down()

        time.sleep(2)

        # Click Logout
        udd = user_drop_down(driver)
        udd.click_logout()

        # Close Browser
        driver.quit()