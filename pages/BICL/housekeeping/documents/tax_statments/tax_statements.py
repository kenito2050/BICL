from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
import time

class tax_statements():

    def __init__(self, driver):
        self.driver = driver

    def Page_Elements(self):

        # Rep Code
        self.rep_code = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div/ui-view/div/div[2]/div[1]/form/span[1]/span/span/input")

        # month text field
        # self.month_field = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div/ui-view/div/div[2]/div[1]/form/span[6]/span/select")

        # month drop down
        # self.month_drop_down = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div/ui-view/div/div[2]/div[1]/form/span[6]/span/span[1]/span[2]/span")

        # year text field
        # self.year_field = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div/ui-view/div/div[2]/div[1]/form/span[5]/span/span[1]/input")

        # year drop down
        # self.year_drop_down = self.driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/div/div/ui-view/div/div[2]/div[1]/form/span[5]/span/span[1]/span[2]/span")

        return self

    # def input_month(self):
    #     tax_statements.Page_Elements(self).month_drop_down.click()
    #     time.sleep(10)
    #     actions = ActionChains(self.driver)
    #     actions.send_keys(Keys.ARROW_DOWN)
    #     actions.send_keys(Keys.ARROW_DOWN)
    #     actions.send_keys(Keys.ARROW_DOWN)
    #     time.sleep(10)
    #     actions.perform()

    def click_rep_code(self):
        tax_statements.Page_Elements(self).rep_code.click()

    def input_year(self):
        actions = ActionChains(self.driver)
        actions.move_to_element(self.driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div/ui-view/div/div[2]/div[1]/form/span[5]/span/span[1]/span[2]/span")).click().perform()
        actions.send_keys(Keys.ARROW_DOWN)
        actions.send_keys(Keys.ENTER)
        actions.send_keys(Keys.TAB)
        actions.perform()

    # def input_year(self):
    #     tax_statements.Page_Elements(self).year_drop_down.click()
    #     actions = ActionChains(self.driver)
    #     actions.send_keys(Keys.ARROW_DOWN)
    #     actions.send_keys(Keys.ENTER)
    #     actions.send_keys(Keys.TAB)
    #     actions.perform()

        # TAB + SHIFT
        # actions.key_down(Keys.SHIFT).send_keys(Keys.TAB).key_up(Keys.SHIFT)