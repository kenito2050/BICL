from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

class account_info():

    def __init__(self, driver):
        self.driver = driver

    def Page_Elements(self):

        # VIEW Drop Down

        # self.view_drop_down = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div/ui-view/div/div[2]/div[1]/form/div[1]/select")

        return self

    # Actions

    def select_documents(self):
        actions = ActionChains(self.driver)
        actions.move_to_element(self.driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div/ui-view/div/div[2]/div[1]/form/div[1]/select")).click().perform()
        actions.send_keys(Keys.ARROW_DOWN)
        actions.send_keys(Keys.ENTER)
        actions.perform()

    # def select_documents_old(self):
    #     account_info.Page_Elements(self).view_drop_down.send_keys("Documents")
