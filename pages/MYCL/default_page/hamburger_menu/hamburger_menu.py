from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

class hamburger_menu():

    def __init__(self, driver):
        self.driver = driver

    def Page_Elements(self):

        return self

        # Actions

    def click_client_link(self):
        actions = ActionChains(self.driver)
        actions.move_to_element(self.driver.find_element(By.XPATH, "//div[@id='idForJS']/div[1]/span[4]/ul/li/div/ul/li[1]/a")).click().perform()

    def click_documents_link(self):
        actions = ActionChains(self.driver)
        actions.move_to_element(
            self.driver.find_element(By.XPATH,
                                     "/html/body/div[1]/div[1]/div[1]/span[4]/ul/li/div/ul/li[2]/a")).click().perform()

    def click_account_link(self):
        actions = ActionChains(self.driver)
        actions.move_to_element(
            self.driver.find_element(By.XPATH,
                                     "/html/body/div[1]/div[1]/div[1]/span[4]/ul/li/div/ul/li[3]/span")).click().perform()

