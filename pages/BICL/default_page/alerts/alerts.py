from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

class alerts():

    def __init__(self, driver):
        self.driver = driver

    def Page_Elements(self):

        # Alerts
        self.alerts = self.driver.find_element(By.XPATH, "/html/body/div[9]/div[2]/div/div/ul/li[1]/a/uib-tab-heading")

        # Portfolio
        self.portfolio = self.driver.find_element(By.XPATH, "/html/body/div[9]/div[2]/div/div/ul/li[2]/a/uib-tab-heading")

        # Risks
        self.risks = self.driver.find_element(By.XPATH, "/html/body/div[9]/div[2]/div/div/ul/li[3]/a/uib-tab-heading")

        # Close Alerts Button
        self.close_alerts_modal_button = self.driver.find_element(By.XPATH, "/html/body/div[9]/div[1]/div/a[2]/span")

        return self

        # Actions

    def click_alerts(self):
        alerts.Page_Elements(self).alerts.click()

    def click_portfolio(self):
        alerts.Page_Elements(self).portfolio.click()

    def click_risks(self):
        alerts.Page_Elements(self).risks.click()

    def close_alerts_modal(self):
        alerts.Page_Elements(self).close_alerts_modal_button.click()