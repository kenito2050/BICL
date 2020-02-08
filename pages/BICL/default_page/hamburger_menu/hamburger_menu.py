from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

class hamburger_menu():

    def __init__(self, driver):
        self.driver = driver

    def Page_Elements(self):

        # Client Link
        self.client_link = self.driver.find_element(By.XPATH, "//div[@id='idForJS']/div[1]/span[4]/ul/li/div/ul/li[1]")

        # Reports
        self.reports = self.driver.find_element(By.XPATH, "//div[@id='idForJS']/div[1]/span[4]/ul/li/div/ul/li[3]/a")

        # Forms Library
        self.forms_library = self.driver.find_element(By.XPATH, "//div[@id='idForJS']/div[1]/span[4]/ul/li/div/ul/li[4]/a")

        # Account
        self.account = self.driver.find_element(By.XPATH, "//div[@id='idForJS']/div[1]/span[4]/ul/li/div/ul/li[5]")

        return self

    def click_client_link(self):
        client_link = self.driver.find_element(By.LINK_TEXT, "Client Link")
        actions = ActionChains(self.driver)
        actions.move_to_element(client_link).click().perform()

    def click_documentes(self):
        documents = self.driver.find_element(By.LINK_TEXT, "Documents")
        actions = ActionChains(self.driver)
        actions.move_to_element(documents).click().perform()

    def click_reports(self):
        hamburger_menu.Page_Elements(self).reports.click()

    def click_forms_library(self):
        hamburger_menu.Page_Elements(self).forms_library.click()

    def click_account(self):
        hamburger_menu.Page_Elements(self).account.click()

    def select_account_info(self):
        account_info = self.driver.find_element(By.LINK_TEXT, "Account Info")
        actions = ActionChains(self.driver)
        actions.move_to_element(account_info).click().perform()

    def select_account_changes(self):
        account_changes = self.driver.find_element(By.LINK_TEXT, "Account Changes")
        actions = ActionChains(self.driver)
        actions.move_to_element(account_changes).click().perform()

    def select_alternate_address(self):
        alternate_address = self.driver.find_element(By.LINK_TEXT, "Alternate Address")
        actions = ActionChains(self.driver)
        actions.move_to_element(alternate_address).click().perform()

    def select_distributions(self):
        distributions = self.driver.find_element(By.LINK_TEXT, "Distributions")
        actions = ActionChains(self.driver)
        actions.move_to_element(distributions).click().perform()

    def select_interested_party(self):
        interested_party = self.driver.find_element(By.LINK_TEXT, "Interested Party")
        actions = ActionChains(self.driver)
        actions.move_to_element(interested_party).click().perform()

    def select_ira_summary(self):
        ira_summary = self.driver.find_element(By.LINK_TEXT, "IRA Summary")
        actions = ActionChains(self.driver)
        actions.move_to_element(ira_summary).click().perform()

    def select_ira_beneficiary(self):
        ira_beneficiary = self.driver.find_element(By.LINK_TEXT, "IRA Beneficiary")
        actions = ActionChains(self.driver)
        actions.move_to_element(ira_beneficiary).click().perform()

    def select_violations(self):
        violations = self.driver.find_element(By.LINK_TEXT, "Violations")
        actions = ActionChains(self.driver)
        actions.move_to_element(violations).click().perform()