from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from config_globals import *

class housekeeping():

    def __init__(self, driver):
        self.driver = driver

    def Page_Elements(self):

        # Documents
        self.documents = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/ul/li[1]/a")

        # Shareholder Materials

        # Activity

        # Action Items

        # Open Orders

        # Order Details

        # ACAT Status

        # Reorg Tracking

        # Maturity Schedule

        # New Account

        # Account Transfer

        # Update

        # MF Questionnaire

        # MF Questionnaire Mgr

        return self

    def click_documents(self):
        documents = self.driver.find_element(By.LINK_TEXT, "Documents")
        actions = ActionChains(self.driver)
        actions.move_to_element(documents).click().perform()

    def verify_shareholder_materials_not_display(self, test_case_ID, browser, env, time_stamp):

        text_displays = False

        if len(self.driver.find_elements(By.LINK_TEXT, "Shareholder Materials")) > 0:
            text_displays = True
        else:
            print("No Error")

        try:
            assert text_displays is False
        except AssertionError:
            screenshot_name = "FAIL" + "_" + test_case_ID + "_" + browser + "_" + env + "_" + time_stamp + ".png"
            saved_screenshot_location = str(screenshot_directory / screenshot_name)
            self.driver.get_screenshot_as_file(saved_screenshot_location)
            raise



    def click_activity(self):
        activity = self.driver.find_element(By.LINK_TEXT, "Activity")
        actions = ActionChains(self.driver)
        actions.move_to_element(activity).click().perform()

    def click_action_items(self):
        action_items = self.driver.find_element(By.LINK_TEXT, "Action Items")
        actions = ActionChains(self.driver)
        actions.move_to_element(action_items).click().perform()

    def click_open_orders(self):
        open_orders = self.driver.find_element(By.LINK_TEXT, "Open Orders")
        actions = ActionChains(self.driver)
        actions.move_to_element(open_orders).click().perform()

    def click_order_details(self):
        order_details = self.driver.find_element(By.LINK_TEXT, "Order Details")
        actions = ActionChains(self.driver)
        actions.move_to_element(order_details).click().perform()

    def click_acat_status(self):
        acat_status = self.driver.find_element(By.LINK_TEXT, "ACAT Status")
        actions = ActionChains(self.driver)
        actions.move_to_element(acat_status).click().perform()

    def click_reorg_tracking(self):
        reorg_tracking = self.driver.find_element(By.LINK_TEXT, "Reorg Tracking")
        actions = ActionChains(self.driver)
        actions.move_to_element(reorg_tracking).click().perform()

    def click_maturity_schedule(self):
        maturity_schedule = self.driver.find_element(By.LINK_TEXT, "Maturity Schedule")
        actions = ActionChains(self.driver)
        actions.move_to_element(maturity_schedule).click().perform()

    def click_new_account(self):
        new_account = self.driver.find_element(By.LINK_TEXT, "New Account")
        actions = ActionChains(self.driver)
        actions.move_to_element(new_account).click().perform()

    def verify_account_transfer_not_display(self, test_case_ID, browser, env, time_stamp):

        text_displays = False

        if len(self.driver.find_elements(By.LINK_TEXT, "Account Transfer")) > 0:
            text_displays = True
        else:
            print("No Error")

        try:
            assert text_displays is False
        except AssertionError:
            screenshot_name = "FAIL" + "_" + test_case_ID + "_" + browser + "_" + env + "_" + time_stamp + ".png"
            saved_screenshot_location = str(screenshot_directory / screenshot_name)
            self.driver.get_screenshot_as_file(saved_screenshot_location)
            raise


    def click_update_account(self):
        update_account = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/ul/li[12]/a")
        actions = ActionChains(self.driver)
        actions.move_to_element(update_account).click().perform()

    def click_mf_questionnaire(self):
        mf_questionnaire = self.driver.find_element(By.LINK_TEXT, "MF Questionnaire")
        actions = ActionChains(self.driver)
        actions.move_to_element(mf_questionnaire).click().perform()

    def click_mf_questionnaire_mgr(self):
        mf_questionnaire_mgr = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/ul/li[14]/a")
        actions = ActionChains(self.driver)
        actions.move_to_element(mf_questionnaire_mgr).click().perform()

