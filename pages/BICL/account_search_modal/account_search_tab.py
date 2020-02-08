from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

class account_search_tab():

    def __init__(self, driver):
        self.driver = driver

    def Page_Elements(self):

        # Name
        self.account_search_tab = self.driver.find_element(By.ID, "accountSearchName")

        # SSN/TIN
        self.ssn_tin = self.driver.find_element(By.XPATH, "/html/body/div[20]/div[2]/div/div/div/div[1]/div/form/div/span[1]/input")

        # Rep Code
        self.rep_code = self.driver.find_element(By.XPATH, "/html/body/div[20]/div[2]/div/div/div/div[1]/div/form/div/span[2]/span/input")

        # Go Button
        self.go_button = self.driver.find_element(By.XPATH, "/html/body/div[20]/div[2]/div/div/div/div[1]/div/form/div/button")

        return self

    # Actions