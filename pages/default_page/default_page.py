from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class default_page():

    def __init__(self, driver):
        self.driver = driver

    def Page_Elements(self):

        # Account Search Field
        self.account_search_field = self.driver.find_element(By.XPATH, "//div[@id='idForJS']/div[1]/span[1]/span[2]/span/input")

        # Account Search Submit Button
        self.account_search_submit_button = self.driver.find_element(By.XPATH,
                                                             "//div[@id='idForJS']/div[1]/span[2]/button[1]/i")

        #### Navigation Bar under Account

        # Overview
        self.overview = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/ul/li[1]/a")

        # Positions
        self.positions = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/ul/li[2]/a")

        # Balances
        self.balances = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/ul/li[3]/a")

        # Activity
        self.activity = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/ul/li[4]/a")

        # Cash Flow
        self.cash_flow = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/ul/li[5]/a")

        # IRA
        self.ira = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/ul/li[6]/a")

        # Commissions
        self.commissions = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/ul/li[7]/a")

        # Account Info
        self.account_info = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/ul/li[8]/a")

        # Order Inquiry
        self.order_inquiry = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/ul/li[9]/a")

        # Maturing Securities
        self.maturing_securities = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/ul/li[10]/a")

        # Funds Distribution
        self.funds_distribution = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/ul/li[11]/a")

        #### Left Panel Icons

        # Account Icon
        self.account_icon = self.driver.find_element(By.XPATH, "/html/body/div[1]/aside/div/div[2]/ul/li[1]/a/i")

        # Gain & Loss Icon
        self.gain_loss_icon = self.driver.find_element(By.XPATH, "/html/body/div[1]/aside/div/div[2]/ul/li[2]/a/i")

        # Order Entry
        self.order_entry_icon = self.driver.find_element(By.XPATH, "/html/body/div[1]/aside/div/div[2]/ul/li[3]/a/i")

        # House Keeping
        self.housekeeping_icon = self.driver.find_element(By.XPATH, "/html/body/div[1]/aside/div/div[3]/ul/li/a/i")

        # Performance
        self.performance_icon = self.driver.find_element(By.XPATH, "/html/body/div[1]/aside/div/div[4]/ul/li/a/i")

        # Tools
        self.tools_icon = self.driver.find_element(By.XPATH, "/html/body/div[1]/aside/div/div[5]/ul/li/a/i")

        return self

    # Actions

    def enter_account_number_search(self, account_number):
        default_page.Page_Elements(self).account_search_field.click()
        default_page.Page_Elements(self).account_search_field.send_keys(account_number)
        default_page.Page_Elements(self).account_search_field.send_keys(Keys.ENTER)
        # default_page.Page_Elements(self).account_search_submit_button.click()

    #### Navigation Bar under Account

    def click_overview_button(self):
        default_page.Page_Elements(self).overview.click()

    def click_positions_button(self):
        default_page.Page_Elements(self).positions.click()

    def click_balances_button(self):
        default_page.Page_Elements(self).balances.click()

    def click_activity_button(self):
        default_page.Page_Elements(self).activity.click()

    def click_cash_flow_button(self):
        default_page.Page_Elements(self).cash_flow.click()

    def click_ira_button(self):
        default_page.Page_Elements(self).ira.click()

    def click_commissions_button(self):
        default_page.Page_Elements(self).commissions.click()

    def click_account_info_button(self):
        default_page.Page_Elements(self).account_info.click()

    def click_order_inquiry_button(self):
        default_page.Page_Elements(self).order_inquiry.click()

    def click_maturing_securities_button(self):
        default_page.Page_Elements(self).maturing_securities.click()

    def click_funds_distribution_button(self):
        default_page.Page_Elements(self).funds_distribution.click()

    #### Left Panel

    def click_account_icon(self):
        default_page.Page_Elements(self).account_icon.click()

    def click_gain_loss_icon(self):
        default_page.Page_Elements(self).gain_loss_icon.click()

    def click_order_entry_icon(self):
        default_page.Page_Elements(self).order_entry_icon.click()

    def click_housekeeping_icon(self):
        default_page.Page_Elements(self).housekeeping_icon.click()

    def click_performance_icon(self):
        default_page.Page_Elements(self).performance_icon.click()

    def click_tools_icon(self):
        default_page.Page_Elements(self).tools_icon.click()













