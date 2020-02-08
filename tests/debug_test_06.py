import pytest
from selenium import webdriver
import time
from config_globals import *
from pages.BICL.login.LoginPage import LoginPage
from pages.generic_page.generic_page import generic_page
from pages.BICL.default_page.user_drop_down.user_drop_down import user_drop_down
from pages.BICL.default_page.default_page import default_page
from pages.BICL.account_search_modal.account_search_modal import account_search_modal
from utilities.environments.environments_BICL import Environments_BICL
from utilities.date_time_generator.date_time_generator import date_time_generator
import pandas as pd

# class Test_login_Chrome:
#
#     @pytest.mark.regression
#
#     def test_login_chrome(self, browser, env):

        # driver = browser

# Create Time Stamp Variable (using Date Time Generator Class in utilities)
dg = date_time_generator()
time_stamp = dg.return_time_stamp()

# This section reads in values from csv file using Pandas Library

# Declare Test Case ID
test_case_ID = 'QTML-T373'

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
driver = webdriver.Chrome(str(CONFIG_PATH / 'chromedriver.exe'))

## Select Appropriate URL based on the Environment Value (env)

env = "PROD"
baseURL = Environments_BICL.return_environments(env)
# baseURL = "https://beta.bi.dev.wedbus.com"

driver.get(baseURL)
driver.maximize_window()

# Search for User Account

time.sleep(5)

# Login to Site
lp = LoginPage(driver)

lp.login(username, password)
lp.click_login_button()

time.sleep(10)

gp = generic_page(driver)

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

# Click on Security Description Tab
asm.click_security_description_tab()

# Enter Security and Click Go
asm.input_security(test_data1)
asm.click_go_button()

time.sleep(5)

# Take Screenshot 3
screenshot_number = "3"
time_stamp_3 = dg.return_time_stamp()
gp.take_screenshot(test_case_ID, browser, control_point_3, screenshot_number, env, time_stamp_3)

# close account_search_modal

asm.close_account_search_modal()

time.sleep(5)

# Take Screenshot 4
screenshot_number = "4"
time_stamp_4 = dg.return_time_stamp()
gp.take_screenshot(test_case_ID, browser, control_point_4, screenshot_number, env, time_stamp_4)

time.sleep(5)

# LOGOUT Section

# Click User Drop Down (on BICL Default Page)
dp.click_user_drop_down()

time.sleep(2)

# Click Logout
udd = user_drop_down(driver)
udd.click_logout()

# Close Browser
driver.quit()