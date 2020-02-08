import pytest
from selenium.common.exceptions import NoSuchElementException
import time
import csv
from config_globals import *
from pages.BICL.login.LoginPage import LoginPage
from pages.BICL.default_page import default_page
from pages.BICL.logout import Logout
from utilities.environments.environments_BICL import Environments_BICL
from utilities.date_time_generator.date_time_generator import date_time_generator

class Test_login_Chrome_user_1:

    @pytest.mark.skip

    def test_login_chrome(self, browser, env):

        driver = browser

        # Create Time Stamp Variable (using Date Time Generator Class in utilities)
        dg = date_time_generator()
        time_stamp = dg.return_time_stamp()

        # CSV Reader
        # Read in username, password and env variables
        with open(csv_directory) as f:
            rows = list(csv.reader(f))
            test_scenario = rows[2][0]
            username = rows[2][1]
            password = rows[2][2]
            account_number = rows[1][3]

        # To DEBUG, Uncomment this NEXT line AND Comment lines 13, 15 and 18. Also, SHIFT + TAB lines 17 - 86 (This will remove indents)
        # driver = webdriver.Chrome(str(CONFIG_PATH / 'chromedriver.exe'))

        ## Select Appropriate URL based on the Environment Value (env)
        # env = "BICL_UAT"
        baseURL = Environments_BICL.return_environments(env)
        # baseURL = "https://beta.bi.dev.wedbus.com"

        driver.get(baseURL)
        driver.maximize_window()

        time.sleep(5)

        # Login to Site
        lp = LoginPage(driver)

        # Verify if page loads, if not, throw exception and take screenshot
        try:
            username_field = lp.Page_Elements().driver.find_element_by_id("UserName")
            username_field.click()
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
            driver.set_page_load_timeout(5)
        except:
            screenshot_name = "FAIL" + "_" + test_scenario + "_" + env + "_" + time_stamp + ".png"
            saved_screenshot_location = str(screenshot_directory / screenshot_name)
            driver.get_screenshot_as_file(saved_screenshot_location)

        time.sleep(3)

        # Enter Account Number and click Search
        dp.enter_account_number_search(account_number)

        time.sleep(5)

        # Verify if overview displays, if not, throw exception and take screenshot
        try:
            overview = dp.Page_Elements().driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/ul/li[1]/a")
            overview.click
            driver.set_page_load_timeout(30)
        except NoSuchElementException:
            screenshot_name = "FAIL" + "_" + test_scenario + "_" + env + "_" + time_stamp + ".png"
            saved_screenshot_location = str(screenshot_directory / screenshot_name)
            driver.get_screenshot_as_file(saved_screenshot_location)

        # Logout
        lg = Logout(driver)
        lg.click_user_drop_down()
        time.sleep(2)
        lg.click_logout()

        driver.quit()