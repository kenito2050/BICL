from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from config_globals import *

class user_preferences():

    def __init__(self, driver):
        self.driver = driver

    def Page_Elements(self):

        # Question 1 - Answer
        # self.question_1_answer = self.driver.find_element(By.ID, "formly_3_input_answer1_1")

        # Question 2 - Answer
        # self.question_2_answer  = self.driver.find_element(By.ID, "formly_3_input_answer2_3")

        # Question 3 - Answer
        # self.question_3_answer  = self.driver.find_element(By.ID, "formly_3_input_answer3_5")

        # Question 4 - Answer
        # self.question_4_answer  = self.driver.find_element(By.ID, "formly_3_input_answer4_7")

        # Question 5 - Answer
        # self.question_5_answer  = self.driver.find_element(By.ID, "formly_3_input_answer5_9")

        # Enter Login Password Field
        # self.password_field = self.driver.find_element(By.ID, "formly_3_input_TradingPass_10")

        # Security Questions - Save Button
        self.save_button_security_questions = self.driver.find_element(By.XPATH, "//div[@id='securityQuestion']/div/div[2]/form/ng-form/div[12]/button")

        # Change User Name - Save Button
        self.save_button_change_user_name = self.driver.find_element(By.XPATH,
                                                                       "//div[@id='changeUsername']/div/div[2]/form/ng-form/div[5]/button[1]")


        # Default Landing Page - Save Button
        self.save_button_default_landing_page = self.driver.find_element(By.XPATH, "//div[@id='defaultLandingPage']/div/div[2]/form/ng-form/div[2]/button")
        return self

    # Actions

    # Security Questions

    def update_question_1(self, test_data1):
        question_1_answer = self.driver.find_element(By.ID, "formly_3_input_answer1_1")
        question_1_answer.click()
        question_1_answer.clear()
        question_1_answer.send_keys(test_data1)

    def reset_question_1(self, test_data2):
        question_1_answer = self.driver.find_element(By.ID, "formly_11_input_answer1_1")
        question_1_answer.click()
        question_1_answer.clear()
        question_1_answer.send_keys(test_data2)

    def update_question_2(self, test_data1):
        question_2_answer = self.driver.find_element(By.ID, "formly_3_input_answer2_3")
        question_2_answer.click()
        question_2_answer.clear()
        question_2_answer.send_keys(test_data1)

    def reset_question_2(self, test_data2):
        question_2_answer = self.driver.find_element(By.ID, "formly_11_input_answer2_3")
        question_2_answer.click()
        question_2_answer.clear()
        question_2_answer.send_keys(test_data2)

    def update_question_3(self, test_data1):
        question_3_answer = self.driver.find_element(By.ID, "formly_3_input_answer3_5")
        question_3_answer.click()
        question_3_answer.clear()
        question_3_answer.send_keys(test_data1)

    def reset_question_3(self, test_data2):
        question_3_answer = self.driver.find_element(By.ID, "formly_11_input_answer3_5")
        question_3_answer.click()
        question_3_answer.clear()
        question_3_answer.send_keys(test_data2)

    def update_question_4(self, test_data1):
        question_4_answer = self.driver.find_element(By.ID, "formly_3_input_answer4_7")
        question_4_answer.click()
        question_4_answer.clear()
        question_4_answer.send_keys(test_data1)

    def reset_question_4(self, test_data2):
        question_4_answer = self.driver.find_element(By.ID, "formly_11_input_answer4_7")
        question_4_answer.click()
        question_4_answer.clear()
        question_4_answer.send_keys(test_data2)

    def update_question_5(self, test_data1):
        question_5_answer = self.driver.find_element(By.ID, "formly_3_input_answer5_9")
        question_5_answer.click()
        question_5_answer.clear()
        question_5_answer.send_keys(test_data1)

    def reset_question_5(self, test_data2):
        question_5_answer = self.driver.find_element(By.ID, "formly_11_input_answer5_9")
        question_5_answer.click()
        question_5_answer.clear()
        question_5_answer.send_keys(test_data2)

    def input_password(self, password):
        password_field = self.driver.find_element(By.ID, "formly_3_input_TradingPass_10")
        password_field.send_keys(password)

    def re_input_password(self, password):
        password_field = self.driver.find_element(By.ID, "formly_11_input_TradingPass_10")
        password_field.send_keys(password)

    def click_save_security_questions(self):
        user_preferences.Page_Elements(self).save_button_security_questions.click()

    def scroll_up(self):
        body = self.driver.find_element_by_xpath('/html/body')
        body.click()
        ActionChains(self.driver).send_keys(Keys.PAGE_UP).perform()

    # Change User Name

    def input_current_username(self, username):
        current_username = self.driver.find_element(By.ID, "formly_4_input_currentUsername_0")
        current_username.click()
        current_username.clear()
        current_username.send_keys(username)

    def enter_new_username(self, test_data):
        enter_new_username = self.driver.find_element(By.ID, "formly_4_input_newUsername_1")
        enter_new_username.click()
        enter_new_username.clear()
        enter_new_username.send_keys(test_data)

    def re_enter_new_username(self, test_data):
        confirm_new_username = self.driver.find_element(By.ID, "formly_4_input_confirmNewUsername_2")
        confirm_new_username.click()
        confirm_new_username.clear()
        confirm_new_username.send_keys(test_data)

    def enter_password(self, test_data):
        enter_password = self.driver.find_element(By.ID, "formly_4_input_tradingPass_3")
        enter_password.click()
        enter_password.clear()
        enter_password.send_keys(test_data)

    def click_save_button(self):
        user_preferences.Page_Elements(self).save_button_change_user_name.click()

    # Change Password

    # Customize Page Preferences

    def set_default_landing_page_to_documents(self):
        default_landing_page_drop_down = self.driver.find_element(By.ID, "formly_6_select_landingPageUrl_0")
        default_landing_page_drop_down.click()
        default_landing_page_drop_down.send_keys("Documents")
        # ActionChains(self.driver).send_keys(Keys.ARROW_DOWN).perform()
        # ActionChains(self.driver).send_keys(Keys.TAB).perform()

    def set_default_landing_page_to_dashboard(self):
        default_landing_page_drop_down = self.driver.find_element(By.ID, "formly_6_select_landingPageUrl_0")
        default_landing_page_drop_down.click()
        default_landing_page_drop_down.send_keys("Dashboard")
        # ActionChains(self.driver).send_keys(Keys.ARROW_UP).perform()
        # ActionChains(self.driver).send_keys(Keys.TAB).perform()

    def set_default_landing_page_to_account(self):
        default_landing_page_drop_down = self.driver.find_element(By.ID, "formly_6_select_landingPageUrl_0")
        default_landing_page_drop_down.click()
        default_landing_page_drop_down.send_keys("Account")

    def click_save_default_landing_page(self):
        user_preferences.Page_Elements(self).save_button_default_landing_page.click()

    def verify_text_exists_in_question_1_answer(self, test_data1, test_case_ID, browser, env, time_stamp):
        text_found = self.driver.find_element(By.ID, "formly_11_input_answer1_1").get_attribute("value")
        # print(text_found)
        try:
            assert test_data1 in text_found
        except AssertionError:
            screenshot_name = "FAIL" + "_" + test_case_ID + "_" + browser + "_" + env + "_" + time_stamp + ".png"
            saved_screenshot_location = str(screenshot_directory / screenshot_name)
            self.driver.get_screenshot_as_file(saved_screenshot_location)
            raise

    def verify_text_exists_in_question_2_answer(self, test_data1, test_case_ID, browser, env, time_stamp):
        text_found = self.driver.find_element(By.ID, "formly_11_input_answer2_3").get_attribute("value")
        # print(text_found)
        try:
            assert test_data1 in text_found
        except AssertionError:
            screenshot_name = "FAIL" + "_" + test_case_ID + "_" + browser + "_" + env + "_" + time_stamp + ".png"
            saved_screenshot_location = str(screenshot_directory / screenshot_name)
            self.driver.get_screenshot_as_file(saved_screenshot_location)
            raise

    def verify_text_exists_in_question_3_answer(self, test_data1, test_case_ID, browser, env, time_stamp):
        text_found = self.driver.find_element(By.ID, "formly_11_input_answer3_5").get_attribute("value")
        # print(text_found)
        try:
            assert test_data1 in text_found
        except AssertionError:
            screenshot_name = "FAIL" + "_" + test_case_ID + "_" + browser + "_" + env + "_" + time_stamp + ".png"
            saved_screenshot_location = str(screenshot_directory / screenshot_name)
            self.driver.get_screenshot_as_file(saved_screenshot_location)
            raise

    def verify_text_exists_in_question_4_answer(self, test_data1, test_case_ID, browser, env, time_stamp):
        text_found = self.driver.find_element(By.ID, "formly_11_input_answer4_7").get_attribute("value")
        # print(text_found)
        try:
            assert test_data1 in text_found
        except AssertionError:
            screenshot_name = "FAIL" + "_" + test_case_ID + "_" + browser + "_" + env + "_" + time_stamp + ".png"
            saved_screenshot_location = str(screenshot_directory / screenshot_name)
            self.driver.get_screenshot_as_file(saved_screenshot_location)
            raise

    def verify_text_exists_in_question_5_answer(self, test_data1, test_case_ID, browser, env, time_stamp):
        text_found = self.driver.find_element(By.ID, "formly_11_input_answer5_9").get_attribute("value")
        # print(text_found)
        try:
            assert test_data1 in text_found
        except AssertionError:
            screenshot_name = "FAIL" + "_" + test_case_ID + "_" + browser + "_" + env + "_" + time_stamp + ".png"
            saved_screenshot_location = str(screenshot_directory / screenshot_name)
            self.driver.get_screenshot_as_file(saved_screenshot_location)
            raise