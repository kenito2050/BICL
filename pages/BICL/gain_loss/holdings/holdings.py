from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

class holdings():

    def __init__(self, driver):
        self.driver = driver

    def Page_Elements(self):

        # View Drop Down
        self.view_drop_down = self.driver.find_element(By.XPATH,
                                                           "/html/body/div[1]/div[3]/div/div/ui-view/div/div[2]/div/div[1]/select")
        return self

    def select_unrealized_detail(self):
        holdings.Page_Elements(self).view_drop_down.send_keys("Unrealized Detail")

    def select_realized(self):
        holdings.Page_Elements(self).view_drop_down.send_keys("Realized")

    def select_unrealized_summary(self):
        holdings.Page_Elements(self).view_drop_down.send_keys("Unrealized Summary")