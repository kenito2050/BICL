import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
import csv
from config_globals import *
from pages.BICL.login.LoginPage import LoginPage
from pages.BICL.default_page.default_page import default_page
from pages.BICL.order_entry.order_entry import order_entry
from pages.BICL.order_entry.mutual_funds import mutual_funds
from pages.BICL.default_page.user_drop_down.user_drop_down import user_drop_down
from utilities.environments.environments_BICL import Environments_BICL
from utilities.date_time_generator.date_time_generator import date_time_generator
import pandas as pd

class Test_login_Chrome:

    @pytest.mark.skip
    @pytest.mark.bicl

    def test_login_chrome(self, browser, env):

        driver = browser

        # Create Time Stamp Variable (using Date Time Generator Class in utilities)
        dg = date_time_generator()
        time_stamp = dg.return_time_stamp()
        date_today = dg.return_date_today()
        time_today = dg.return_time_today()

        # This section reads in values from csv file using Pandas Library

        # Declare Test Case ID
        test_case_ID = 'QTML-T175'

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

        time.sleep(5)

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

        time.sleep(5)

        # Enter Account Number and click Search
        dp.enter_account_number_search(account_number)

        time.sleep(1)

        # Navigate to Order Entry
        dp.click_order_entry_icon()

        time.sleep(1)

        oe = order_entry(driver)

        time.sleep(3)

        # Click Mutual Funds
        oe.click_mutual_funds()

        mf = mutual_funds(driver)

        time.sleep(2)

        # Mutual Funds Screen

        # Select Sell on Action Drop Down
        mf.select_sell_from_action_dropdown()

        time.sleep(2)

        # Input Sell Quantity in Quantity Field
        mf.input_value_in_quantity()

        time.sleep(2)

        # Input Value in Fund
        mf.input_value_in_fund(test_data1)

        time.sleep(2)

        # Select SHARE from Transaction Type
        mf.select_share_from_transaction_type_dropdown()

        time.sleep(2)

        # Select SOLICITED from Drop Down
        mf.select_solicited_from_dropdown()

        time.sleep(2)

        # Input value in Accepted By
        mf.input_value_in_accepted_by(username)

        time.sleep(2)

        # Input Date Today
        mf.input_date_today(date_today)

        time.sleep(2)

        # Input Time Today
        mf.input_time_today(time_today)

        time.sleep(2)

        # Click Submit
        mf.click_submit_button()

        time.sleep(1)

        # Verify that Questionnaire does not display

        # Logout

        # Click User Drop Down (on BICL Default Page)
        dp.click_user_drop_down()

        time.sleep(2)

        # Click Logout
        udd = user_drop_down(driver)
        udd.click_logout()

        # Take screenshot, save to utilities/test_results/screenshots
        screenshot_4 = test_case_ID + "_" + browser + "_" + env + "_" + "screenshot_4" + "_" + control_point_4 + "_" + time_stamp + ".png"
        saved_screenshot_location_4 = str(screenshot_directory / screenshot_4)
        driver.get_screenshot_as_file(saved_screenshot_location_4)

        driver.quit()