import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
import csv
from config_globals import *
from pages.BICL.login.LoginPage import LoginPage
from pages.BICL.default_page.default_page import default_page
from pages.BICL.default_page.user_drop_down.user_drop_down import user_drop_down
from pages.MYCL.default_page.MYCL_default_page import MYCL_default_page
from pages.MYCL.default_page.hamburger_menu.hamburger_menu import hamburger_menu
from pages.MYCL.default_page.user_drop_down.MYCL_user_drop_down import MYCL_user_drop_down
from pages.MYCL.gain_loss.unrealized_summary import gain_loss_unrealized_summary
from pages.MYCL.gain_loss.unrealized_detail import gain_loss_unrealized_detail
from pages.MYCL.account.positions import positions
from pages.MYCL.navigation.build_base_url import build_base_url
from pages.MYCL.navigation.navigation import navigation
from pages.MYCL.navigation.Screens import Screens
from utilities.environments.environments_BICL import Environments_BICL
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
        test_case_ID = 'QTML-T194'

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

        driver.get(baseURL)
        driver.maximize_window()

        # Search for User Account

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

        time.sleep(1)

        # Take screenshot, save to utilities/test_results/screenshots
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

        time.sleep(1)

        # Enter Account Number and click Search
        dp.enter_account_number_search(account_number)

        # increase timeout to 15
        time.sleep(20)

        mdp = MYCL_default_page(driver)

        # Click User Drop Down / Client Link, Redirect to Client Link Site
        # Click Menu Hamburger
        mdp.click_hamburger_menu()

        time.sleep(5)

        hm = hamburger_menu(driver)

        hm.click_client_link()

        # set to 10 or above
        time.sleep(10)

        # Navigate to Gains & Loss / Unrealized Summary
        # Verify text exists in Price Column

        current_url = driver.current_url
        slashparts = current_url.split('/')

        bbu = build_base_url()
        home_index_string = bbu.return_home_index_string()
        nav_url = '/'.join(slashparts[:3]) + '/' + home_index_string

        screen_to_navigate_to_1 = "gains_loss_unrealized_summary"
        screen_1 = Screens.return_screens(screen_to_navigate_to_1)

        driver.get(nav_url + screen_1)

        # Set timeout to 25
        time.sleep(30)

        glus = gain_loss_unrealized_summary(driver)

        time.sleep(1)

        glus.verify_values_display_in_Price_Column(test_case_ID, browser, env, time_stamp)

        time.sleep(1)

        # Take screenshot, save to utilities/test_results/screenshots
        screenshot_2 = test_case_ID + "_" + browser + "_" + env + "_" + "screenshot_2" + "_" + control_point_2 + "_" + time_stamp + ".png"
        saved_screenshot_location_2 = str(screenshot_directory / screenshot_2)
        driver.get_screenshot_as_file(saved_screenshot_location_2)

        # Navigate to Gains & Loss / Unrealized Detail
        # Verify text exists in Price Column

        bbu = build_base_url()
        home_index_string = bbu.return_home_index_string()
        nav_url = '/'.join(slashparts[:3]) + '/' + home_index_string

        screen_to_navigate_to_2 = "gains_loss_unrealized_detail"
        screen_2 = Screens.return_screens(screen_to_navigate_to_2)

        driver.get(nav_url + screen_2)

        time.sleep(25)

        glud = gain_loss_unrealized_detail(driver)

        glud.verify_values_display_in_Price_Column(test_case_ID, browser, env, time_stamp)

        # Take screenshot, save to utilities/test_results/screenshots
        screenshot_3 = test_case_ID + "_" + browser + "_" + env + "_" + "screenshot_3" + "_" + control_point_3 + "_" + time_stamp + ".png"
        saved_screenshot_location_3 = str(screenshot_directory / screenshot_3)
        driver.get_screenshot_as_file(saved_screenshot_location_3)

        # Navigate to Account / Positions
        # Verify text exists in Price Column

        bbu = build_base_url()
        home_index_string = bbu.return_home_index_string()
        nav_url = '/'.join(slashparts[:3]) + '/' + home_index_string

        screen_to_navigate_to_3 = "account_positions"
        screen_3 = Screens.return_screens(screen_to_navigate_to_3)

        driver.get(nav_url + screen_3)

        time.sleep(25)

        ap = positions(driver)

        ap.verify_values_display_in_Price_Column(test_case_ID, browser, env, time_stamp)

        # Take screenshot, save to utilities/test_results/screenshots
        screenshot_4 = test_case_ID + "_" + browser + "_" + env + "_" + "screenshot_4" + "_" + control_point_4 + "_" + time_stamp + ".png"
        saved_screenshot_location_4 = str(screenshot_directory / screenshot_4)
        driver.get_screenshot_as_file(saved_screenshot_location_4)

        time.sleep(1)

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