# Automation Framework written in Python using a Page Object Framework

## Key Features include

(1) Date Time Generator - In utilities folder, the file date_time_generator.py uses the datetime and dateutil.relativedelta libraries to determine and format a date. Each test script assigns a date time stamp for screen captures or error logging. See code example below:

        # Create Time Stamp Variable (using Date Time Generator Class in utilities)
        dg = date_time_generator()
        time_stamp = dg.return_time_stamp()

(2) Screen Captures - Screen captures are taken & saved at critical control points (i.e., after successful login). See code example below:

        # Take screenshot, save to utilities/test_results/screenshots
        screenshot_1 = test_case_ID + "_" + browser + "_" + env + "_" + "screenshot_1" + "_" + control_point_1 + "_" + time_stamp +     ".png"
        saved_screenshot_location_1 = str(screenshot_directory / screenshot_1)
        driver.get_screenshot_as_file(saved_screenshot_location_1)

(3) CSV Reader - CSV files are read using Pandas library which allows indexed ordering.

        # Declare Test Case ID
        test_case_ID = 'QTML-T4'

        # Declare csv directory
        df = pd.read_csv(csv_directory)

        # Select Row where "Test_Case_ID" Column Matches the test_case_ID declared above
        # This is the row that contains the data values for this test scenario
        test_case_row = df.loc[df.Test_Case_ID == test_case_ID]
        
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

(4) Pytest Mark - pytest.mark allows setting of metadata on test functions. Scripts with certain marker attributes (i.e., "smoke") can be invoked at the command line. See example code below:

    @pytest.mark.smoke
    
(5) Environments Management using Data Dictionary Funtion - Test Environment can be specified at the command line. There are data dictionary classes in utilities/environments (in Java, this function is called a hash table) that return a URL string based on the value provided at the command line. The following command specifies the "UAT" test environment. 

    pytest -m test --env UAT

(6) Reporting using Pytest - Reports can be generated after each test run using the following commands. First line uses Pytest HTML and second line uses Allure.

    pytest -m smoke --env UAT --html=test_results/report.html

    pytest -m smoke --env UAT --alluredir=C:\test_results

(7) Assert Statements - The following code validates that there are the correct number of decimals (2) in a certain column.

    def verify_decimals_in_margin_balance_total(self, test_case_ID, browser, env, time_stamp):
        rows = overview.Page_Elements(self).summary_of_accounts_table.find_elements(By.TAG_NAME, "tr")
        is_decimal = False
        for row in rows:
            cols = row.find_elements(By.TAG_NAME, "td")
            for col in cols:
                text_found = cols[2].text
                num_decimal_places = text_found[::-1].find('.')
                if num_decimal_places == 2:
                    is_decimal = True
                    break

                try:
                    assert is_decimal is True
                except AssertionError:
                    screenshot_name = "FAIL" + "_" + test_case_ID + "_" + browser + "_" + env + "_" + time_stamp + ".png"
                    saved_screenshot_location = str(screenshot_directory / screenshot_name)
                    self.driver.get_screenshot_as_file(saved_screenshot_location)
                    raise

(8) Error Handling - The following is an example of a Try / Except Block to check for the presence of an error modal:

        # If Error Button displays, mark errorDisplays "TRUE"
        # errorDisplays default is FALSE
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
            
(9) Iterate through a web table and fail if a value is NOT found - On the website in test, there are HTML tables with data. In the next code example, (a) there is a FOR loop that iterates through the HTML table (table is located using Xpath in the Page_Elements section) (b) and the code looks for the presence of a decimal point (.) in the text_found (which is in the Price column). If a decimal point is found, then values_filled becomes True. However, if no decimal point is found, then values_filled is False (which is the default value), an Assertion Error is thrown and a screen shot is taken.


    def Page_Elements(self):

        # Table
        self.table = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div/ui-view/div/div[2]/div[4]/table/tbody")

        return self

        # Actions

    def verify_values_display_in_Price_Column(self, test_case_ID, browser, env, time_stamp):
        rows = gain_loss_unrealized_detail.Page_Elements(self).table.find_elements(By.TAG_NAME, "tr")
        values_filled = False
        for row in rows:
            cols = row.find_elements(By.TAG_NAME, "td")
            for col in cols:
                text_found = cols[7].text
                if ("." in text_found):
                    values_filled = True
                    break

        try:
            assert values_filled is True
        except AssertionError:
            screenshot_name = "FAIL" + "_" + test_case_ID + "_" + browser + "_" + env + "_" + time_stamp + ".png"
            saved_screenshot_location = str(screenshot_directory / screenshot_name)
            self.driver.get_screenshot_as_file(saved_screenshot_location)
            raise
