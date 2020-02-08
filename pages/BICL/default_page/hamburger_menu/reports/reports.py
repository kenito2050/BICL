from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class reports():

    def __init__(self, driver):
        self.driver = driver

    def Page_Elements(self):

        # Reports
        self.reports_drop_down = self.driver.find_element(By.ID, "ddlReports")

        # Go Button
        self.go_button = self.driver.find_element(By.ID, "btnGo")

        return self

    def select_Portfolio_Valuation(self):
        reports.Page_Elements(self).reports_drop_down.send_keys("Portfolio Valuation")

    def select_Portfolio_Performance(self):
        reports.Page_Elements(self).reports_drop_down.send_keys("Portfolio Performance")

    def click_go_button(self):
        reports.Page_Elements(self).go_button.click()