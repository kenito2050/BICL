from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class violations():

    def __init__(self, driver):
        self.driver = driver

    def Page_Elements(self):

        # Violations
        self.violations_modal = self.driver.find_element(By.XPATH, "/html/body/div[17]")

        # Close Button - Violations
        self.close_button_violations_modal = self.driver.find_element(By.XPATH, "/html/body/div[17]/div[1]/div/a[2]")

        return self

    # Actions

    def close_Violations_Modal(self):
        violations.Page_Elements(self).close_button_violations_modal.click()

