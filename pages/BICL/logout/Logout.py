from selenium.webdriver.common.by import By

class Logout():

    def __init__(self, driver):
        self.driver = driver

    def Page_Elements(self):

        # User Drop Down Menu
        self.user_drop_down = self.driver.find_element(By.XPATH, "/html/body/div[1]/header/div[3]/i[2]")

        # TODO: Logout not recognized in IE
        # Logout
        self.logout_link = self.driver.find_element(By.XPATH, "/html/body/div[1]/header/div[3]/div/ul/li/a")

        return self

    def click_user_drop_down(self):
        Logout.Page_Elements(self).user_drop_down.click()

    def click_logout(self):
        Logout.Page_Elements(self).logout_link.click()

