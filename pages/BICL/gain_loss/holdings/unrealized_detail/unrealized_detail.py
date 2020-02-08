from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class unrealized_detail():

    def __init__(self, driver):
        self.driver = driver

    def Page_Elements(self):

        return self

    def click_PDF_Button(self):
        pdf_button = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div/ui-view/div/div[4]/div/div[1]/button[2]/i")
        actions = ActionChains(self.driver)
        actions.move_to_element(pdf_button).click().perform()