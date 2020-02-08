from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class mutual_funds():

    def __init__(self, driver):
        self.driver = driver

    def Page_Elements(self):

        # Action (Drop Down)
        self.action_dropdown = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div/ui-view/div/div[2]/div/div/section[1]/div/div[1]/div[1]/div/div[2]/form/div[2]/div[1]/div/select")

        # Quantity / Dollars
        self.quantity = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div/ui-view/div/div[2]/div/div/section[1]/div/div[1]/div[1]/div/div[2]/form/div[2]/div[2]/div/input")

        # Fund
        self.fund = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div/ui-view/div/div[2]/div/div/section[1]/div/div[1]/div[1]/div/div[2]/form/div[2]/div[3]/div/div/input")

        # Transaction Type (Drop Down)
        self.transaction_type_drop_down = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div/ui-view/div/div[2]/div/div/section[1]/div/div[1]/div[1]/div/div[2]/form/div[2]/div[4]/div/select")

        # Solicited / Unsolicited
        self.solicited_unsolicited = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div/ui-view/div/div[2]/div/div/section[1]/div/div[1]/div[1]/div/div[2]/form/div[4]/div[4]/div/select")

        # Accepted By
        self.accepted_by = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div/ui-view/div/div[2]/div/div/section[1]/div/div[1]/div[3]/div/div[2]/form/div[5]/div[1]/div/input")

        # Date (MM/DD/YY)
        self.date = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div/ui-view/div/div[2]/div/div/section[1]/div/div[1]/div[3]/div/div[2]/form/div[5]/div[2]/div/span/span/input")

        # Time (EST HHMMSS)
        self.time = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div/ui-view/div/div[2]/div/div/section[1]/div/div[1]/div[3]/div/div[2]/form/div[5]/div[3]/div/input")

        # Submit Button
        self.submit_button = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div/ui-view/div/div[2]/div/div/section[1]/div/div[1]/div[4]/button[2]")

        return self

    def select_sell_from_action_dropdown(self):
        mutual_funds.Page_Elements(self).action_dropdown.click()
        mutual_funds.Page_Elements(self).action_dropdown.send_keys("Sell")

    def input_value_in_quantity(self):
        mutual_funds.Page_Elements(self).quantity.click()
        mutual_funds.Page_Elements(self).quantity.send_keys("1")

    def input_value_in_fund(self, test_data):
        mutual_funds.Page_Elements(self).fund.click()
        mutual_funds.Page_Elements(self).fund.send_keys(test_data)

    def select_share_from_transaction_type_dropdown(self):
        mutual_funds.Page_Elements(self).transaction_type_drop_down.click()
        mutual_funds.Page_Elements(self).transaction_type_drop_down.send_keys("Share")

    def select_solicited_from_dropdown(self):
        mutual_funds.Page_Elements(self).solicited_unsolicited.click()
        mutual_funds.Page_Elements(self).solicited_unsolicited.send_keys("Solicited")

    def input_value_in_accepted_by(self, username):
        mutual_funds.Page_Elements(self).accepted_by.click()
        mutual_funds.Page_Elements(self).accepted_by.send_keys(username)

    def input_date_today(self, date_today):
        mutual_funds.Page_Elements(self).date.click()
        mutual_funds.Page_Elements(self).date.send_keys(date_today)

    def input_time_today(self, test_data):
        mutual_funds.Page_Elements(self).time.click()
        mutual_funds.Page_Elements(self).time.send_keys(test_data)

    def click_submit_button(self):
        mutual_funds.Page_Elements(self).submit_button.click()




