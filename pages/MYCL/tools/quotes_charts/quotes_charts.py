from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class quotes_charts():

    def __init__(self, driver):
        self.driver = driver

    def Page_Elements(self):

        # Quotes & Charts

        # Options Lookup

        # My Portfolio

        # My Watchlist

        return self

    # Actions

    def click_quotes_charts(self):
        actions = ActionChains(self.driver)
        actions.move_to_element(self.driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div/ui-view/div/div[1]/ul/li[1]/a")).click().perform()

        # quotes_charts = self.driver.find_element(By.LINK_TEXT, "Quotes & Charts")
        # actions = ActionChains(self.driver)
        # actions.move_to_element(quotes_charts).click().perform()

    def click_options_lookup(self):
        options_lookup = self.driver.find_element(By.LINK_TEXT, "Options Lookup")
        actions = ActionChains(self.driver)
        actions.move_to_element(options_lookup).click().perform()

        # actions = ActionChains(self.driver)
        # actions.move_to_element(self.driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div/ui-view/div/div[1]/ul/li[2]/a")).click().perform()

    def click_my_portfolio(self):
        my_portfolio = self.driver.find_element(By.LINK_TEXT, "My Portfolio")
        actions = ActionChains(self.driver)
        actions.move_to_element(my_portfolio).click().perform()

        # actions = ActionChains(self.driver)
        # actions.move_to_element(self.driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div/ui-view/div/div[1]/ul/li[3]/a")).click().perform()

    def click_my_watchlist(self):
        my_watchlist = self.driver.find_element(By.LINK_TEXT, "My Watchlist")
        actions = ActionChains(self.driver)
        actions.move_to_element(my_watchlist).click().perform()

        # actions = ActionChains(self.driver)
        # actions.move_to_element(self.driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div/ui-view/div/div[1]/ul/li[4]/a")).click().perform()