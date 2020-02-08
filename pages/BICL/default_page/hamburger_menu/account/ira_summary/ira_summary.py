from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class ira_summary_modal():

    def __init__(self, driver):
        self.driver = driver

    def Page_Elements(self):

        # IRA Summary Modal
        self.ira_summary_modal = self.driver.find_element(By.XPATH, "/html/body/div[15]")

        # Close Button - IRA Summary Modal
        self.close_button_ira_summary_modal = self.driver.find_element(By.XPATH, "/html/body/div[15]/div[1]/div/a[2]")

        return self

    # Actions

    def close_IRA_Summary_Modal(self):
        ira_summary_modal.Page_Elements(self).close_button_ira_summary_modal.click()

