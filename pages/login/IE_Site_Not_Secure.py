from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

class IE_Site_Not_Secure():

    def __init__(self, driver):
        self.driver = driver

    def Page_Elements(self):
        # User Name Field
        self.proceed_link = self.driver.find_element(By.ID, "overridelink")

        return self

    def locate_click_proceed_link(self):
        IE_Site_Not_Secure.Page_Elements(self).proceed_link.click()

    def locate_click_proceed_link_action_chains(self, proceed_link):
        ActionChains(self.driver).move_to_element(proceed_link).perform()
        IE_Site_Not_Secure.Page_Elements(self).proceed_link.click()

    def click_proceed_workaround(self):
        self.driver.send_keys(Keys.TAB)
        self.driver.send_keys(Keys.TAB)
        self.driver.send_keys(Keys.TAB)
        self.driver.send_keys(Keys.TAB)
        self.driver.send_keys(Keys.ENTER)

