from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
import csv
import math
from bs4 import BeautifulSoup
import requests
import warnings
from config_globals import *
import pytest
from pages.BICL.login.LoginPage import LoginPage
from pages.BICL.default_page import default_page
from pages.BICL.balances import balances
from pages.BICL.logout import Logout
from utilities.environments.environments_BICL import Environments_BICL
from utilities.date_time_generator.date_time_generator import date_time_generator

class Test_login_Chrome:

    @pytest.mark.skip

    def test_login_chrome(self, browser, env):

        test_case = "test_login_Chrome"
        driver = browser

        # Create Time Stamp Variable (using Date Time Generator Class in utilities)
        dg = date_time_generator()
        time_stamp = dg.return_time_stamp()

        # CSV Reader
        # Read in username, password and env variables
        with open(csv_directory) as f:
            rows = list(csv.reader(f))
            test_scenario = rows[1][0]
            username = rows[1][1]
            password = rows[1][2]
            account_number = rows[1][3]

        # To DEBUG, Uncomment this NEXT line AND Comment lines 13, 15 and 18. Also, SHIFT + TAB lines 17 - 86 (This will remove indents)
        driver = webdriver.Chrome(str(CONFIG_PATH / 'chromedriver.exe'))
        env = "BICL_UAT"

        ## Select Appropriate URL based on the Environment Value (env)
        baseURL = Environments.return_environments(env)
        # baseURL = "https://beta.bi.dev.wedbus.com"

        driver.get(baseURL)
        driver.maximize_window()

        time.sleep(5)

        # Login to Site
        lp = LoginPage(driver)

        # Verify if page loads, if not, throw exception and take screenshot
        try:
            username_field = lp.Page_Elements().driver.find_element_by_id("UserName")
        except NoSuchElementException:
            screenshot_name = "FAIL" + "_" + test_scenario + "_" + env + "_" + time_stamp + ".png"
            saved_screenshot_location = str(screenshot_directory / screenshot_name)
            driver.get_screenshot_as_file(saved_screenshot_location)

        lp.login(username, password)
        lp.click_login_button()

        time.sleep(10)

        # Take screenshot after login and save to utilities/test_results/screenshots
        screenshot_name = test_scenario + "_" + env + "_" + time_stamp + ".png"
        saved_screenshot_location = str(screenshot_directory / screenshot_name)
        driver.get_screenshot_as_file(saved_screenshot_location)

        dp = default_page(driver)

        # Timeout method for page to load, timeout set to 30 seconds
        try:
            driver.set_page_load_timeout(30)
        except:
            screenshot_name = "FAIL" + "_" + test_scenario + "_" + env + "_" + time_stamp + ".png"
            saved_screenshot_location = str(screenshot_directory / screenshot_name)
            driver.get_screenshot_as_file(saved_screenshot_location)

        time.sleep(3)

        # Enter Account Number and click Search
        dp.enter_account_number_search(account_number)

        time.sleep(5)

        # Click Balances
        # Expected = Balances Screen should load
        dp.Page_Elements().click_balances_button()

        # Declare Balances Screen
        bl = balances(driver)

        # Verify View Page Drop Down on Balances Screen can be clicked, if not, throw exception and take screenshot
        try:
            bl.click_view_page_drop_down()
        except NoSuchElementException:
            screenshot_name = "FAIL" + "_" + test_scenario + "_" "unable_to_load_balances" + "_" + env + "_" + time_stamp + ".png"
            saved_screenshot_location = str(screenshot_directory / screenshot_name)
            driver.get_screenshot_as_file(saved_screenshot_location)

        time.sleep(3)

        # Reset view page drop down to "unfocused" mode
        bl.reset_view_page_drop_down()

        time.sleep(5)

        # Declare cash balance value to compare
        # TODO : Retrieve cash balance value from db or previous session
        cash_balance_amount = "20.00"

        # ignore warnings
        warnings.filterwarnings("ignore")

        # Parse the current url
        url = driver.current_url
        parsed = requests.get(url, verify=False)

        # Unable to read from table
        soup = BeautifulSoup(parsed.content, 'html.parser')
        a = soup.find("table", {"class": "table"})
        print(a)

        time.sleep(3)

        try:
            cash_balance_test = bl.read_return_cash_balance_value()
        except:
            screenshot_name = "FAIL" + "_" + test_scenario + "_" "cash_balance not found" + "_" + env + "_" + time_stamp + ".png"
            saved_screenshot_location = str(screenshot_directory / screenshot_name)
            driver.get_screenshot_as_file(saved_screenshot_location)

        # Compare Cash Balance value from screen with stored cash balance value


        try:
            assert math.isclose(cash_balance_amount, cash_balance_test, rel_tol=0.02)
        except:
            screenshot_name = "FAIL" + "_" + test_scenario + "_" "cash_balances do not match" + "_" + env + "_" + time_stamp + ".png"
            saved_screenshot_location = str(screenshot_directory / screenshot_name)
            driver.get_screenshot_as_file(saved_screenshot_location)

        # Logout
        lg = Logout(driver)
        lg.click_user_drop_down()
        time.sleep(2)
        lg.click_logout()

        driver.quit()