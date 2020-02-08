from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

class account():

    def __init__(self, driver):
        self.driver = driver

    def Page_Elements(self):

        return self

    # Actions

    def click_overview(self):
        overview = self.driver.find_element(By.LINK_TEXT, "Overview")
        actions = ActionChains(self.driver)
        actions.move_to_element(overview).click().perform()

    def click_positions(self):
        positions = self.driver.find_element(By.LINK_TEXT, "Positions")
        actions = ActionChains(self.driver)
        actions.move_to_element(positions).click().perform()

    def click_balances(self):
        balances = self.driver.find_element(By.LINK_TEXT, "Balances")
        actions = ActionChains(self.driver)
        actions.move_to_element(balances).click().perform()

    def click_activity_link(self):
        activity = self.driver.find_element(By.LINK_TEXT, "Activity")
        actions = ActionChains(self.driver)
        actions.move_to_element(activity).click().perform()

    def click_cash_flow(self):
        cash_flow = self.driver.find_element(By.LINK_TEXT, "Cash Flow")
        actions = ActionChains(self.driver)
        actions.move_to_element(cash_flow).click().perform()

    def click_IRA(self):
        ira = self.driver.find_element(By.LINK_TEXT, "IRA")
        actions = ActionChains(self.driver)
        actions.move_to_element(ira).click().perform()

    def click_commissions(self):
        commissions = self.driver.find_element(By.LINK_TEXT, "Commissions")
        actions = ActionChains(self.driver)
        actions.move_to_element(commissions).click().perform()

    def click_account_info(self):
        account_info = self.driver.find_element(By.LINK_TEXT, "Account Info")
        actions = ActionChains(self.driver)
        actions.move_to_element(account_info).click().perform()

    def click_order_inquiry(self):
        order_inquiry = self.driver.find_element(By.LINK_TEXT, "Order Inquiry")
        actions = ActionChains(self.driver)
        actions.move_to_element(order_inquiry).click().perform()

    def click_maturing_securities(self):
        maturing_securities = self.driver.find_element(By.LINK_TEXT, "Maturing Securities")
        actions = ActionChains(self.driver)
        actions.move_to_element(maturing_securities).click().perform()

    def click_funds_distribution(self):
        funds_distribution = self.driver.find_element(By.LINK_TEXT, "Funds Distribution")
        actions = ActionChains(self.driver)
        actions.move_to_element(funds_distribution).click().perform()