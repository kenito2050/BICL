from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

class IE_Logout():

    def __init__(self, driver):
        self.driver = driver

    def Page_Elements(self):

        self.logout_link = self.driver.find_element(By.XPATH, "/html/body/div[1]/header/div[3]/div/ul/li/a")

        return self

    def IE_Logout(self, logout_link):
        ActionChains(self.driver).move_to_element(logout_link).perform()
        logout_link.Page_Elements(self).user_drop_down.click()

    def IE_Logout_old(self):
        # For IE Browser, Force Navigate to Logout page
        current_url = self.driver.current_url
        slashparts = current_url.split('/')
        # Now join back the first three sections 'http:', '' and 'example.com'
        new_base_url = '/'.join(slashparts[:3]) + '/'
        logout_string = "/user/login?logout=1"
        logout_screen = new_base_url + logout_string
        self.driver.get(logout_screen)