import pytest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
import csv
from config_globals import *
from pages.generic_page.generic_page import generic_page
from pages.ADMIN.admin import admin
from pages.ADMIN.password_reset_modal_before import password_reset_modal_before
from pages.ADMIN.password_reset_modal_after import password_reset_modal_after
from pages.BICL.change_password_modal.change_password_modal import change_password_modal
from pages.BICL.login.LoginPage import LoginPage
from pages.BICL.default_page.user_drop_down.user_drop_down import user_drop_down
from pages.BICL.default_page.default_page import default_page
from utilities.environments.environments_ADMIN import Environments_ADMIN
from utilities.environments.environments_BICL import Environments_BICL
from utilities.date_time_generator.date_time_generator import date_time_generator
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

        # This section reads in values from csv file using Pandas Library

        # Declare Test Case ID
        test_case_ID = 'QTML-T193'

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
        # baseURL = "https://beta.bi.dev.wedbus.com"

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

        gp = generic_page(driver)

        gp.scroll_down()

        time.sleep(5)

        adm.click_password_reset_button()

        # Change focus to Modal

        time.sleep(1)

        # switch focus to modal
        driver.switch_to.window(driver.window_handles[1])

        time.sleep(1)

        prm_before = password_reset_modal_before(driver)

        # Click Reset Password

        prm_before.click_reset_password()

        time.sleep(1)

        # Parse and Save Password String

        prm_after = password_reset_modal_after(driver)

        updated_password = prm_after.return_new_password()

        # time.sleep(1)
        # print(updated_password)
        # time.sleep(1)

        # Take screenshot after login and save to utilities/test_results/screenshots
        screenshot_1 = test_case_ID + "_" + browser + "_" + env + "_" + "screenshot_1" + "_" + control_point_1 + "_" + time_stamp + ".png"
        saved_screenshot_location_1 = str(screenshot_directory / screenshot_1)
        driver.get_screenshot_as_file(saved_screenshot_location_1)

        # Close password reset modal

        prm_after.click_close()

        time.sleep(1)

        # switch focus to parent window
        driver.switch_to.window(driver.window_handles[0])

        time.sleep(1)

        # Launch BICL Site & login
        # env = "DEV"
        baseURL_BICL = Environments_BICL.return_environments(env)
        # baseURL = "https://beta.bi.dev.wedbus.com"

        time.sleep(5)

        driver.get(baseURL_BICL)
        driver.maximize_window()

        time.sleep(1)

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

        lp.login(username, updated_password)
        lp.click_login_button()

        time.sleep(10)

        # Set Password back to original

        cpm = change_password_modal(driver)

        # input password into required fields
        cpm.input_new_password(password)

        # confirm password
        # cpm.confirm_new_password(password)

        # Take screenshot after login and save to utilities/test_results/screenshots
        screenshot_2 = test_case_ID + "_" + browser + "_" + env + "_" + "screenshot_2" + "_" + control_point_2 + "_" + time_stamp + ".png"
        saved_screenshot_location_2 = str(screenshot_directory / screenshot_2)
        driver.get_screenshot_as_file(saved_screenshot_location_2)

        # Click Submit
        cpm.click_submit_button()

        time.sleep(1)

        # Close "Change Password" Modal
        cpm.close_change_password_modal()

        time.sleep(1)

        dp = default_page(driver)

        # Timeout method for page to load, timeout set to 30 seconds
        try:
            driver.set_page_load_timeout(30)
        except:
            screenshot_name = "FAIL" + "_" + test_case_ID + "_" + browser + "_" + env + "_" + time_stamp + ".png"
            saved_screenshot_location = str(screenshot_directory / screenshot_name)
            driver.get_screenshot_as_file(saved_screenshot_location)
            raise

        time.sleep(5)

        # LOGOUT Section

        # Click User Drop Down (on BICL Default Page)
        dp.click_user_drop_down()

        time.sleep(2)

        # Click Logout
        udd = user_drop_down(driver)
        udd.click_logout()

        # Launch BICL Site
        driver.get(baseURL_BICL)
        driver.maximize_window()

        # Login to Site
        lp = LoginPage(driver)

        # Take screenshot after login and save to utilities/test_results/screenshots
        screenshot_3 = test_case_ID + "_" + browser + "_" + env + "_" + "screenshot_2" + "_" + control_point_3 + "_" + time_stamp + ".png"
        saved_screenshot_location_3 = str(screenshot_directory / screenshot_3)
        driver.get_screenshot_as_file(saved_screenshot_location_3)

        lp.login(username, password)
        lp.click_login_button()

        time.sleep(5)

        dp = default_page(driver)

        time.sleep(10)

        # Take screenshot after login and save to utilities/test_results/screenshots
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