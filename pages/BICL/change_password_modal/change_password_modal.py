from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from config_globals import *

class change_password_modal():

    def __init__(self, driver):
        self.driver = driver

    def Page_Elements(self):

        # Enter New Password
        self.enter_new_password = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/form/div[2]/input[2]")

        # Confirm New Password
        self.confirm_new_password = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/form/div[2]/input[3]")

        # Submit Button
        self.submit_button = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/form/div[2]/div[5]/button")

        return self

    def input_new_password(self, password):
        change_password_modal.Page_Elements(self).enter_new_password.click()
        change_password_modal.Page_Elements(self).enter_new_password.send_keys(password)
        ActionChains(self.driver).send_keys(Keys.TAB).perform()
        ActionChains(self.driver).send_keys(password).perform()


    def confirm_password(self, password):
        change_password_modal.Page_Elements(self).confirm_new_password.click()
        change_password_modal.Page_Elements(self).confirm_new_password.send_keys(password)

    def click_submit_button(self):
        change_password_modal.Page_Elements(self).submit_button.click()

    def close_change_password_modal(self):
        change_password_modal = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div[2]/button")
        change_password_modal.click()

