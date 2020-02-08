from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class balances():

    def __init__(self, driver):
        self.driver = driver

    def Page_Elements(self):

        # View Page Drop Down
        self.view_page_drop_down = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div/ui-view/div/div[2]/div[3]/span/span")

        # Balances : Cash
        self.balances_cash_field = self.driver.find_element(By.XPATH,
                                                             "/html/body/div[1]/div[3]/div/div/ui-view/div/div[3]/div[2]/div[1]/div[1]/div[2]/table/tbody/tr[1]/td[1]/span")
        return self

    # Actions

    def click_view_page_drop_down(self):
        balances.Page_Elements(self).view_page_drop_down.click()

    # This method toggles the view page drop down back to original status (unfocused)
    def reset_view_page_drop_down(self):
        balances.Page_Elements(self).view_page_drop_down.click()

    def read_return_cash_balance_value(self):
        cash_balance = balances.Page_Elements(self).balances_cash_field.getText()
        return cash_balance