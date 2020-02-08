from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class left_panel():

    def __init__(self, driver):
        self.driver = driver

    def Page_Elements(self):

        # Dashboard

        # Account
        # self.account = self.driver.find_elements(By.XPATH, "/html/body/div[1]/aside/div/div[1]/ul/li[2]/a/i")

        # Gain & Loss
        # self.gain_loss = self.driver.find_elements(By.XPATH, "/html/body/div[1]/aside/div/div[2]/ul/li[2]/a/i")

        # Documents

        # Tools

        # Profile / Preferences

        return self

    # Actions

    def click_dashboard(self):
        actions = ActionChains(self.driver)
        actions.move_to_element(self.driver.find_element(By.XPATH, "/html/body/div[1]/aside/div/div[1]/ul/li[1]")).click().perform()

    def click_account(self):
        actions = ActionChains(self.driver)
        actions.move_to_element(self.driver.find_element(By.XPATH, "/html/body/div[1]/aside/div/div[2]/ul/li[1]/a/i")).click().perform()

    def click_gain_loss(self):
        actions = ActionChains(self.driver)
        actions.move_to_element(self.driver.find_element(By.XPATH, "/html/body/div[1]/aside/div/div[2]/ul/li[2]/a/i")).click().perform()

    def click_documents(self):
        actions = ActionChains(self.driver)
        actions.move_to_element(self.driver.find_element(By.XPATH, "/html/body/div[1]/aside/div/div[2]/ul/li[3]/a/i")).click().perform()

    def click_tools(self):
        actions = ActionChains(self.driver)
        actions.move_to_element(self.driver.find_element(By.XPATH, "/html/body/div[1]/aside/div/div[4]/ul/li[1]")).click().perform()

    def click_profile_preferences(self):
        actions = ActionChains(self.driver)
        actions.move_to_element(self.driver.find_element(By.XPATH, "/html/body/div[1]/aside/div/div[4]/ul/li[2]")).click().perform()
