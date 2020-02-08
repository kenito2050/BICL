from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class help():

    def __init__(self, driver):
        self.driver = driver

    def Page_Elements(self):

        # Security Statement

        # Recommended Browser

        # Contact Us

        # Service Fees

        # Legal Information

        # User Agreement

        # Privacy Statement

        # My Disclosures

        return self

    # Actions

    def click_service_fees(self):
        actions = ActionChains(self.driver)
        actions.move_to_element(self.driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div/ui-view/div/div[2]/div[1]/div[2]/div[2]/ul/li[6]/a")).click().perform()