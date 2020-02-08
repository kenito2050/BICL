from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

class IE_User_Drop_Down():

    def __init__(self, driver):
        self.driver = driver

    def Page_Elements(self):

        # User Drop Down Menu
        self.user_drop_down = self.driver.find_element(By.XPATH, "/html/body/div[1]/header/div[3]/i[2]")

        return self

    def click_user_drop_down(self):
        IE_User_Drop_Down.Page_Elements(self).user_drop_down.click()

    def click_user_drop_down_IE(self, user_drop_down):
        ActionChains(self.driver).move_to_element(user_drop_down).perform()
        IE_User_Drop_Down.Page_Elements(self).user_drop_down.click()