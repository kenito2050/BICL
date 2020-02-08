from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

class notes_modal():

    def __init__(self, driver):
        self.driver = driver

    def Page_Elements(self):

        # Add Note Tab
        self.add_note_tab = self.driver.find_element(By.XPATH, "/html/body/div[10]/div[2]/div/div/ul/li[1]/a")

        # All Rep Notes Tab
        self.all_rep_notes_tab = self.driver.find_element(By.XPATH, "/html/body/div[10]/div[2]/div/div/ul/li[2]/a")

        # Account Notes Tab
        self.account_notes_tab = self.driver.find_element(By.XPATH, "/html/body/div[10]/div[2]/div/div/ul/li[3]/a")

        # Activity Notes Tab
        self.activity_notes_tab = self.driver.find_element(By.XPATH, "/html/body/div[10]/div[2]/div/div/ul/li[4]/a")

        # Close Button
        self.close_button = self.driver.find_element(By.XPATH, "/html/body/div[10]/div[1]/div/a[2]/span")

        return self

    # Actions

    def click_all_rep_notes_tab(self):
        notes_modal.Page_Elements(self).all_rep_notes_tab.click()

    def click_account_notes_tab(self):
        notes_modal.Page_Elements(self).account_notes_tab.click()

    def click_activity_notes_tab(self):
        notes_modal.Page_Elements(self).activity_notes_tab.click()