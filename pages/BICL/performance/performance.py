from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from config_globals import *

class performance():

    def __init__(self, driver):
        self.driver = driver

    def Page_Elements(self):

        # Commissions
        # self.commissions = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/ul/li[7]/a")

        # Analysis Detail
        # self.analysis_detail = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/ul/li[2]/a")

        # Analysis Detail
        # self.analysis_detail = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/ul/li[3]/a")

        return self

    # Actions

    def click_commissions(self):
        commissions = self.driver.find_element(By.LINK_TEXT, "Commissions")
        actions = ActionChains(self.driver)
        actions.move_to_element(commissions).click().perform()

    def click_analysis_detail(self):
        analysis_detail = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/ul/li[2]/a")
        actions = ActionChains(self.driver)
        actions.move_to_element(analysis_detail).click().perform()

    def click_branch(self):
        branch = self.driver.find_element(By.LINK_TEXT, "Branch")
        actions = ActionChains(self.driver)
        actions.move_to_element(branch).click().perform()