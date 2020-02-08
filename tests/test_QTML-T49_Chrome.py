from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from selenium.common.exceptions import NoSuchElementException
import time
import csv
from config_globals import *
from pages.BICL.login.LoginPage import LoginPage
from pages.BICL.default_page.user_drop_down.user_drop_down import user_drop_down
from pages.BICL.default_page.default_page import default_page
from pages.BICL.housekeeping.housekeeping import housekeeping
from pages.BICL.housekeeping.documents.documents import documents
from utilities.environments.environments_BICL import Environments_BICL
from utilities.date_time_generator.date_time_generator import date_time_generator
from utilities.date_validator.date_validator import date_validator
import pandas as pd

class Test_login_Chrome:

    @pytest.mark.smoke
    @pytest.mark.bicl

    def test_login_chrome(self, browser, env):

        driver = browser

        # Create Time Stamp Variable (using Date Time Generator Class in utilities)
        dg = date_time_generator()
        time_stamp = dg.return_time_stamp()

        # Create a valid date (1 month ago)
        date_previous_month = dg.return_date_one_month_ago()
        dv = date_validator()
        valid_date = dv.return_valid_date(date_previous_month).strftime("%m/%d/%Y")
        july_01_date = "07/01/2019" # Error Displays using this date -- SDBICL-2236

        # This section reads in values from csv file using Pandas Library

        # Declare Test Case ID
        test_case_ID = 'QTML-T49'

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

        # env = "PROD"
        baseURL = Environments_BICL.return_environments(env)
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

        # Verify if account icon can be clicked, if not, throw exception and take screenshot
        try:
            account_icon = dp.Page_Elements().driver.find_element_by_xpath(
                "/html/body/div[1]/aside/div/div[2]/ul/li[1]/a/i")
            account_icon.click()
            driver.set_page_load_timeout(30)
        except NoSuchElementException:
            screenshot_name = "FAIL" + "_" + test_case_ID + "_" + browser + "_" + env + "_" + time_stamp + ".png"
            saved_screenshot_location = str(screenshot_directory / screenshot_name)
            driver.get_screenshot_as_file(saved_screenshot_location)
            raise

        time.sleep(20)

        # Click HouseKeeping link

        dp.click_housekeeping_icon()
        # change to 10
        time.sleep(5)

        # instantiate housekeeping
        hk = housekeeping(driver)

        # Click Documents
        # hk.click_documents()

        time.sleep(5)

        # instantiate documents
        doc = documents(driver)

        # Input Rep Code
        doc.input_rep_code(rep_code)

        time.sleep(20)

        # Select Open Order Confirms
        doc.select_open_order_confirms()
        # change to 20
        time.sleep(20)

        # Input Date
        doc.input_date(july_01_date)

        # change to 10
        time.sleep(1)

        # click Search Button
        doc.click_search_button()

        # Take screenshot after clicking search button and save to utilities/test_results/screenshots
        screenshot_2 = test_case_ID + "_" + browser + "_" + env + "_" + "screenshot_2" + "_" + control_point_2 + "_" + time_stamp + ".png"
        saved_screenshot_location_2 = str(screenshot_directory / screenshot_2)
        driver.get_screenshot_as_file(saved_screenshot_location_2)

        # Set to 20
        time.sleep(1)

        # click Confirms Document
        # Commented out 8-8-19 - K.V.
        # doc.click_confirms_document()

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

        time.sleep(15)

        # Take screenshot after Display of Document and save to utilities/test_results/screenshots
        screenshot_3 = test_case_ID + "_" + browser + "_" + env + "_" + "screenshot_3" + "_" + control_point_3 + "_" + time_stamp + ".png"
        saved_screenshot_location_3 = str(screenshot_directory / screenshot_3)
        driver.get_screenshot_as_file(saved_screenshot_location_3)

        time.sleep(15)

        # Take screenshot BEFORE logout and save to utilities/test_results/screenshots
        screenshot_4 = test_case_ID + "_" + browser + "_" + env + "_" + "screenshot_4" + "_" + control_point_4 + "_" + time_stamp + ".png"
        saved_screenshot_location_4 = str(screenshot_directory / screenshot_4)
        driver.get_screenshot_as_file(saved_screenshot_location_4)

        # Logout

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