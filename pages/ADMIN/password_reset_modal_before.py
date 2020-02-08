from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

class password_reset_modal_before():

    def __init__(self, driver):
        self.driver = driver

    def Page_Elements(self):

        # reset password button
        self.reset_password_button = self.driver.find_element(By.ID, "btnReset")

        return self

    def click_reset_password(self):
        password_reset_modal_before.Page_Elements(self).reset_password_button.click()



