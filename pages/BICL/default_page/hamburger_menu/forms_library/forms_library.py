from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class forms_library():

    def __init__(self, driver):
        self.driver = driver

    def Page_Elements(self):

        # 529 College Savings Plan Worksheet
        self._529_College_Savings_Plan = self.driver.find_element(By.ID, "DataGrid1")

        return self

    def click_529_College_Savings_Plan(self):
        forms_library.Page_Elements(self)._529_College_Savings_Plan.click()

