from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from config_globals import *

class profile_preferences():

    def __init__(self, driver):
        self.driver = driver

    def Page_Elements(self):

        # User Preferences
        self.user_preferences = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/ul/li[1]/a")

        # Account Preferences
        self.account_preferences = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/ul/li[2]/a")

        return self

    # Actions

    def click_account_preferences(self):
        profile_preferences.Page_Elements(self).account_preferences.click()

    def click_user_preferences(self):
        profile_preferences.Page_Elements(self).user_preferences.click()
