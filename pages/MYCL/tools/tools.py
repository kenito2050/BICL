from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class tools():

    def __init__(self, driver):
        self.driver = driver

    def Page_Elements(self):

        # Wedbush Research

        # Quotes & Charts

        # Calculators

        # Help

        return self

    # Actions

    def click_Wedbush_Research(self):
        actions = ActionChains(self.driver)
        actions.move_to_element(self.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/ul/li[1]/a")).click().perform()

    def click_quotes_charts(self):
        actions = ActionChains(self.driver)
        actions.move_to_element(self.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/ul/li[2]/a")).click().perform()

    def click_calculators(self):
        actions = ActionChains(self.driver)
        actions.move_to_element(self.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/ul/li[3]/a")).click().perform()

    def click_help(self):
        actions = ActionChains(self.driver)
        actions.move_to_element(self.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/ul/li[4]/a")).click().perform()