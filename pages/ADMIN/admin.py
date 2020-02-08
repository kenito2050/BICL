from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from config_globals import *

class admin():

    def __init__(self, driver):
        self.driver = driver

    def Page_Elements(self):

        # Find User
        self.find_user_field = self.driver.find_element(By.ID, "MainContent_tbFindUser")

        # Go Button
        self.go_button = self.driver.find_element(By.ID, "MainContent_btnFindUser")

        # First Name
        self.first_name = self.driver.find_element(By.ID, "MainContent_tbFirstName")

        # System Used
        self.system_used = self.driver.find_element(By.ID, "MainContent_ddSystemUsed")

        # Office Code
        self.office_code = self.driver.find_element(By.ID, "MainContent_tbOfficeCode")

        # Primary Rep Code
        self.rep_code = self.driver.find_element(By.ID, "MainContent_tbPrimaryRepCode")

        # Reset Password Button
        # self.reset_password_button = self.driver.find_element(By.ID, "MainContent_btnResetPassword")

        # Save Button
        self.save_button = self.driver.find_element(By.ID, "MainContent_btnCommitUser")

        # Entitlements

        # Broker Insight

        # Monitoring

        # Site Status
        self.site_status = self.driver.find_element(By.ID, "MainContent_cbHasSiteStatus")

        # Replay
        self.replay = self.driver.find_element(By.ID, "MainContent_cbHasReplay")

        return self

    # Actions

    def enter_user_account_click_search(self, user_account):
        admin.Page_Elements(self).find_user_field.send_keys(user_account)
        admin.Page_Elements(self).go_button.click()

    def click_first_name_tab_3_times(self):
        admin.Page_Elements(self).first_name.click()
        actions = ActionChains(self.driver)
        actions.send_keys(Keys.TAB)
        actions.send_keys(Keys.TAB)
        actions.send_keys(Keys.TAB)
        actions.perform()

    def change_system_used_P3(self):
        actions = ActionChains(self.driver)
        actions.send_keys(Keys.ARROW_DOWN)
        actions.perform()

    def change_system_used_BETA(self):
        actions = ActionChains(self.driver)
        actions.send_keys(Keys.ARROW_UP)
        actions.perform()

    def update_office_code(self):
        admin.Page_Elements(self).office_code.click()
        admin.Page_Elements(self).office_code.send_keys("SH")

    def update_office_code_new(self, rep_code):
        admin.Page_Elements(self).office_code.click()
        admin.Page_Elements(self).office_code.clear()
        admin.Page_Elements(self).office_code.send_keys(rep_code)

    def update_office_code_to_CA(self):
        admin.Page_Elements(self).office_code.click()
        admin.Page_Elements(self).office_code.clear()
        admin.Page_Elements(self).office_code.send_keys("CA")

    def update_office_code_to_KS(self):
        admin.Page_Elements(self).office_code.click()
        admin.Page_Elements(self).office_code.clear()
        admin.Page_Elements(self).office_code.send_keys("KS")

    def update_rep_code(self):
        admin.Page_Elements(self).rep_code.click()
        admin.Page_Elements(self).rep_code.send_keys("CA")

    def check_uncheck_site_status(self):
        admin.Page_Elements(self).site_status.click()

    def check_uncheck_replay(self):
        admin.Page_Elements(self).replay.click()

    def click_password_reset_button(self):
        reset_password_button = self.driver.find_element(By.ID, "MainContent_btnResetPassword")
        reset_password_button.click()

    def validate_replay_link_displays(self, test_case_ID, browser, env, time_stamp):
        replay_link = self.driver.find_element(By.LINK_TEXT, "Replay Feature")
        try:
            replay_link.click()
        except AssertionError:
            screenshot_name = "FAIL" + "_" + test_case_ID + "_" + browser + "_" + env + "_" + time_stamp + ".png"
            saved_screenshot_location = str(screenshot_directory / screenshot_name)
            self.driver.get_screenshot_as_file(saved_screenshot_location)
            raise

    def click_save(self):
        admin.Page_Elements(self).save_button.click()