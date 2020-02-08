from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class distributions_modal():

    def __init__(self, driver):
        self.driver = driver

    def Page_Elements(self):

        # Distributions
        self.distributions_modal = self.driver.find_element(By.XPATH, "/html/body/div[14]/div[1]/span")

        # Close Button - Distributions
        self.close_button_distributions_modal = self.driver.find_element(By.XPATH, "/html/body/div[14]/div[1]/div/a[2]/span")

        return self

    def click_close_button_distributions_modal(self):
        distributions_modal.Page_Elements(self).close_button_distributions_modal.click()