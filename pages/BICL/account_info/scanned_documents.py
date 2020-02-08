from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class scanned_documents():

    def __init__(self, driver):
        self.driver = driver

    def Page_Elements(self):

        # Document Drop Down

        self.email_changes_document = self.driver.find_element(By.XPATH,
                                                             "/html/body/div[1]/div[3]/div/div/ui-view/div/div[2]/div[3]/div/div/div/div[2]/div/div[1]/div/a[1]")

        return self

    # Actions
    def click_address_change_form(self):
        actions = ActionChains(self.driver)
        actions.move_to_element(self.driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div/ui-view/div/div[2]/div[3]/div/div/div/div[2]/div/div[1]/div/a[1]")).click().perform()

    def select_email_changes_document(self):
        scanned_documents.Page_Elements(self).email_changes_document.click()