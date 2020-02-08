from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

class password_reset_modal_after():

    def __init__(self, driver):
        self.driver = driver

    def Page_Elements(self):

        # close button
        self.close_button = self.driver.find_element(By.ID, "btnClose")

        # Updated password
        self.updated_password_text = self.driver.find_element(By.ID, "lblOut")

        return self

    def return_new_password(self):
        new_password = password_reset_modal_after.Page_Elements(self).updated_password_text.text
        formatted_password = new_password.split("-", 1)[1]
        return formatted_password

    def click_close(self):
        password_reset_modal_after.Page_Elements(self).close_button.click()





