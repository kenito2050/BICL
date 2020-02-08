from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

class security_description_tab():

    def __init__(self, driver):
        self.driver = driver

    def Page_Elements(self):

        # Security
        self.security_field = self.driver.find_element(By.XPATH, "/html/body/div[20]/div[2]/div/div/div/div[2]/div/form/div/input")

        return self

    # Actions