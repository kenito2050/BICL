from selenium.webdriver.common.by import By

class account_info():

    def __init__(self, driver):
        self.driver = driver

    def Page_Elements(self):

        # VIEW Drop Down

        self.view_drop_down = self.driver.find_element(By.XPATH,
                                                             "/html/body/div[1]/div[3]/div/div/ui-view/div/div[2]/div[1]/form/div[1]/select")
        # /html/body/div[1]/div[3]/div/div/ui-view/div/div[2]/div[1]/form/div[1]/select

        return self

    # Actions

    def select_documents(self):
        account_info.Page_Elements(self).view_drop_down.send_keys("Documents")
