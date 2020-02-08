import time
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

class IE_More_Information():

    def __init__(self, driver):
        self.driver = driver

    def Page_Elements(self):
        # User Name Field
        self.more_information_link = self.driver.find_element(By.LINK_TEXT, "More information")

        return self

    def move_to_more_information_link_click(self, more_information_link):
        ActionChains.move_to_element(more_information_link).perform()
        IE_More_Information.Page_Elements(self).more_information_link.click()


    def locate_click_more_information(self):
        IE_More_Information.Page_Elements(self).more_information_link.click()
        # IE_More_Information.Page_Elements(self).more_information_link.click()
        time.sleep(2)
        # IE_More_Information.Page_Elements(self).more_information_link.send_keys("ENTER")
