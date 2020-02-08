from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from config_globals import *

class role_templates():

    def __init__(self, driver):
        self.driver = driver

    def Page_Elements(self):

        # Application
        self.application_drop_down = self.driver.find_element(By.ID, "MainContent_ddlApplication")

        # System Used
        self.system_used_drop_down = self.driver.find_element(By.ID, "MainContent_ddlSystemUsed")

        # Role
        # self.role_drop_down = self.driver.find_element(By.ID, "MainContent_ddlRole")

        # Update Button
        # //*[@id="MainContent_btnSave"]

        # "X" Label
        # self.x_label = self.driver.find_element(By.XPATH, "//div[@id='MainContent_cbRoles']/tbody/tr[10]/td[5]/label")

        return self

        # Actions

    def change_role_to_developer(self):
        role_drop_down = self.driver.find_element(By.ID, "MainContent_ddlRole")
        role_drop_down.click()
        # role_templates.Page_Elements(self).role_drop_down.send_keys(test_data)
        ActionChains(self.driver).send_keys(Keys.ARROW_DOWN).perform()
        ActionChains(self.driver).send_keys(Keys.ARROW_DOWN).perform()
        ActionChains(self.driver).send_keys(Keys.ARROW_DOWN).perform()
        ActionChains(self.driver).send_keys(Keys.ARROW_DOWN).perform()
        ActionChains(self.driver).send_keys(Keys.ARROW_DOWN).perform()
        ActionChains(self.driver).send_keys(Keys.ARROW_DOWN).perform()
        ActionChains(self.driver).send_keys(Keys.ARROW_DOWN).perform()
        ActionChains(self.driver).send_keys(Keys.ARROW_DOWN).perform()
        ActionChains(self.driver).send_keys(Keys.ARROW_DOWN).perform()
        ActionChains(self.driver).send_keys(Keys.ARROW_DOWN).perform()
        ActionChains(self.driver).send_keys(Keys.ARROW_DOWN).perform()
        ActionChains(self.driver).send_keys(Keys.ARROW_DOWN).perform()
        ActionChains(self.driver).send_keys(Keys.ARROW_DOWN).perform()
        ActionChains(self.driver).send_keys(Keys.ARROW_DOWN).perform()
        ActionChains(self.driver).send_keys(Keys.ENTER).perform()

    def checkmark_x_label(self):
        x_label = self.driver.find_element(By.ID, "MainContent_cbRoles_68")
        x_label.click()

    def click_update_button(self):
        update_button = self.driver.find_element(By.ID, "MainContent_btnSave")
        update_button.click()


    def verify_x_label_checked(self, test_case_ID, browser, env, time_stamp):
        x_label = self.driver.find_element(By.ID, "MainContent_cbRoles_68")
        label_checked = x_label.is_selected()
        if label_checked:
            print("label checked")
        else:
            print("label not checked")

        try:
            assert label_checked is True
        except AssertionError:
            screenshot_name = "FAIL" + "_" + test_case_ID + "_" + browser + "_" + env + "_" + time_stamp + ".png"
            saved_screenshot_location = str(screenshot_directory / screenshot_name)
            self.driver.get_screenshot_as_file(saved_screenshot_location)
            raise
