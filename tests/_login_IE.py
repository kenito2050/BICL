from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import NoSuchElementException
import time
from config_globals import *
import csv
from pages.BICL.login.LoginPage import LoginPage
from utilities.environments.environments_BICL import Environments
from utilities.date_time_generator.date_time_generator import date_time_generator

## NOTES
# Script will execute but hangs before logout -- fixed 5-3-19 K.V.
# Script runs in debug mode -- fixed 5-3-19 K.V.
# Need to configure contest to run IE Driver -- 5-3-19

# class test_login:

# def test_login_IE(self, browser, env):

# @pytest.mark.smoke

def test_login_IE(env):

        test_case = "test_login_IE"
        # driver = browser

        # Create Time Stamp Variable (using Date Time Generator Class in utilities)
        dg = date_time_generator()
        time_stamp = dg.return_time_stamp()

        # Declare csv directory
        # csv_directory = str(test_case_directory / test_case) + ".csv"

        # CSV Reader
        # Read in username, password and env variables
        with open(csv_directory) as f:
            rows = list(csv.reader(f))
            test_scenario = rows[3][0]
            username = rows[3][1]
            password = rows[3][2]
            account_number = rows[3][3]

        cap = DesiredCapabilities.INTERNETEXPLORER.copy()
        # cap['INTRODUCE_FLAKINESS_BY_IGNORING_SECURITY_DOMAINS'] = True
        # cap['nativeEvents'] = False
        cap['IE_ENSURE_CLEAN_SESSION'] = True
        cap['ENABLE_ELEMENT_CACHE_CLEANUP'] = True

        # cap['pageLoadStrategy'] = 'eager'

        driver = webdriver.Ie(str(CONFIG_PATH / 'IEDriverServer.exe'))

        ## Select Appropriate URL based on the Environment Value (env)

        # env = "BICL_UAT"
        baseURL = Environments.return_environments(env)
        # baseURL = "https://beta.bi.dev.wedbush.com"

        driver.get(baseURL)
        driver.maximize_window()

        # This section closes extra open window tabs
        handles = driver.window_handles
        size = len(handles)
        parent_handle = driver.current_window_handle
        for x in range(size):
            if handles[x] != parent_handle:
                driver.switch_to.window(handles[x])
                print(driver.title)
                driver.close()
            else:
                driver.switch_to.window(parent_handle)
                print(driver.title)

        time.sleep(5)

        # If IE browser, click More Information \ Proceed to Website
        more_information_link = driver.find_element(By.LINK_TEXT, "More information")
        ActionChains(driver).move_to_element(more_information_link).perform()
        more_information_link.click()
        time.sleep(5)

        # IESNS = IE_Site_Not_Secure(driver)
        # proceed_link = driver.find_element(By.ID, "overridelink")
        # IESNS.locate_click_proceed_link_action_chains(proceed_link)

        # Workaround to click "Override Link" -K.V. 5-20-19
        proceed_link = driver.find_element(By.ID, "overridelink")
        ActionChains(driver).move_to_element(proceed_link).perform()
        proceed_link.click()

        time.sleep(5)

        # Login to Site
        lp = LoginPage(driver)

        # Verify if UserName field displays, if not, throw exception and take screenshot
        try:
            username_field = lp.Page_Elements().driver.find_element_by_id("UserName")
            username_field.click()
        except NoSuchElementException:
            screenshot_name = "FAIL" + "_" + test_scenario + "_" + env + "_" + time_stamp + ".png"
            saved_screenshot_location = str(screenshot_directory / screenshot_name)
            driver.get_screenshot_as_file(saved_screenshot_location)
            raise

        # enter username and password
        lp.IE_login(username, password)

        # Note: Script would hang after clicking "Login" button
        # to fix this, I added an IE_login() method with the following lines
        # ...send_keys(Keys.TAB)
        # ...send_keys(Keys.ENTER)
        #
        # Script works with this update -- K.V 5-2-19

        # Added wait because script cannot find "user_drop_down_element --K.V. 5-2-19
        time.sleep(10)

        # Take screenshot and save to utilities/test_results/screenshots
        screenshot_name = test_scenario + "_" + env + "_" + time_stamp + ".png"
        saved_screenshot_location = str(screenshot_directory / screenshot_name)
        driver.get_screenshot_as_file(saved_screenshot_location)

        # Move Mouse to User Drop Down (Upper Right Corner)
        user_drop_down = driver.find_element(By.XPATH, "/html/body/div[1]/header/div[3]/i[2]")
        ActionChains(driver).move_to_element(user_drop_down).perform()

        # Click Logout, if not, throw exception and take screenshot
        logout_link = driver.find_element(By.XPATH, "/html/body/div[1]/header/div[3]/div/ul/li/a")
        # ActionChains(driver).move_to_element(logout_link).perform()
        logout_link.click()

        time.sleep(10)

        # For IE Browser, Force Navigate to Logout page
        # Logout Workaround -K.V. --5-20-19
        # current_url = driver.current_url
        # slashparts = current_url.split('/')
        # Now join back the first three sections 'http:', '' and 'example.com'
        # new_base_url = '/'.join(slashparts[:3]) + '/'
        # logout_string = "/user/login?logout=1"
        # logout_screen = new_base_url + logout_string
        # driver.get(logout_screen)

        # IE-Specific Logout

        # Click User Drop Down
        # IEU = IE_User_Drop_Down(driver)
        # user_drop_down = driver.find_element(By.XPATH, "/html/body/div[1]/header/div[3]/i[2]")
        # ActionChains(driver).move_to_element(user_drop_down).perform()
        # user_drop_down.click()

        # Click Logout
        # logout_link = driver.find_element(By.XPATH, "/html/body/div[1]/header/div[3]/div/ul/li/a")
        # ActionChains(driver).move_to_element(logout_link).perform()
        # logout_link.click()

        # Close Browser
        driver.close()