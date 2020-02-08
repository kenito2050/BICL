from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class order_entry():

    def __init__(self, driver):
        self.driver = driver

    def Page_Elements(self):

        # Equities / Options
        self.equities_options = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/ul/li[1]/a")

        # Mutual Funds
        self.mutual_funds = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/ul/li[2]/a")

        # Bonds
        self.bonds = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/ul/li[3]/a")

        # UIT
        self.UIT = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/ul/li[4]/a")

        # Order Billing
        self.order_billing = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/ul/li[5]/a")

        # PIPS
        self.pips = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/ul/li[6]/a")

        return self

    def click_equities_options(self):
        order_entry.Page_Elements(self).equities_options.click()

    def click_mutual_funds(self):
        order_entry.Page_Elements(self).mutual_funds.click()

    def click_bonds(self):
        order_entry.Page_Elements(self).bonds.click()

    def click_UIT(self):
        order_entry.Page_Elements(self).UIT.click()

    def click_order_billing(self):
        order_entry.Page_Elements(self).order_billing.click()

    def click_pips(self):
        order_entry.Page_Elements(self).pips.click()