from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

class gain_loss():

    def __init__(self, driver):
        self.driver = driver

    def Page_Elements(self):

        return self

    def click_holdings(self):
        holdings = self.driver.find_element(By.LINK_TEXT, "Holdings")
        actions = ActionChains(self.driver)
        actions.move_to_element(holdings).click().perform()

    def click_tax_info(self):
        tax_info = self.driver.find_element(By.LINK_TEXT, "Tax Info")
        actions = ActionChains(self.driver)
        actions.move_to_element(tax_info).click().perform()

    def click_projected_income(self):
        projected_income = self.driver.find_element(By.LINK_TEXT, "Projected Income")
        actions = ActionChains(self.driver)
        actions.move_to_element(projected_income).click().perform()

    def click_pending_income(self):
        pending_income = self.driver.find_element(By.LINK_TEXT, "Pending Income")
        actions = ActionChains(self.driver)
        actions.move_to_element(pending_income).click().perform()

    def click_reinvested_div(self):
        reinvested_div = self.driver.find_element(By.LINK_TEXT, "Reinvested Div")
        actions = ActionChains(self.driver)
        actions.move_to_element(reinvested_div).click().perform()