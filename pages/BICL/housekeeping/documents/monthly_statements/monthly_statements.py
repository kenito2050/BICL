from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
import time

class monthly_statements():

    def __init__(self, driver):
        self.driver = driver

    def Page_Elements(self):

        return self

    def select_month(self):
        month_text_field = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div/ui-view/div/div[2]/div[1]/form/span[5]/span/span/span[2]/span")
        month_text_field.click()
        actions = ActionChains(self.driver)
        actions.send_keys(Keys.ARROW_DOWN)
        actions.send_keys(Keys.ARROW_DOWN)
        actions.send_keys(Keys.ARROW_DOWN)
        actions.send_keys(Keys.ENTER)
        actions.send_keys(Keys.TAB)
        actions.perform()

    def click_document(self):
        document = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div/ui-view/div/div[2]/div[2]/div/div[1]/div/a[1]")
        document.click()