from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class all_rep_notes_tab():

    def __init__(self, driver):
        self.driver = driver

    def Page_Elements(self):

        # PDF Export Button
        self.pdf_export_button = self.driver.find_element(By.XPATH, "/html/body/div[10]/div[2]/div/div/div/div[2]/div/div/div[1]/button/i")

        return self

    # Actions

    def click_export_pdf_button(self):
        actions = ActionChains(self.driver)
        actions.move_to_element(all_rep_notes_tab.Page_Elements(self).pdf_export_button).click().perform()