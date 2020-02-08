from selenium.webdriver.common.by import By

class document_drop_down():

    def __init__(self, driver):
        self.driver = driver

    def Page_Elements(self):

        # Document Drop Down

        self.document_drop_down = self.driver.find_element(By.XPATH,
                                                             "/html/body/div[1]/div[3]/div/div/ui-view/div/div[2]/div[1]/form/div[2]/div/select")

        return self

    # Actions

    def select_confirms(self):
        document_drop_down.Page_Elements(self).document_drop_down.send_keys("Confirms")

    def select_open_order_confirms(self):
            document_drop_down.Page_Elements(self).document_drop_down.send_keys("Open Order Confirms")

    def select_tax_statements(self):
        document_drop_down.Page_Elements(self).document_drop_down.send_keys("Tax Statements")

    def select_monthly_statements(self):
        document_drop_down.Page_Elements(self).document_drop_down.send_keys("Monthly Statements")

    def select_401B_letters(self):
        document_drop_down.Page_Elements(self).document_drop_down.send_keys("401B Letters")

    def select_scanned_documents(self):
        document_drop_down.Page_Elements(self).document_drop_down.send_keys("Scanned Documents")
