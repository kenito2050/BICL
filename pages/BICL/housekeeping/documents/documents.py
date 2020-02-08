from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
import time
from config_globals import *

class documents():

    def __init__(self, driver):
        self.driver = driver

    def Page_Elements(self):

        self.panel_title = self.driver.find_element(By.XPATH, './/span[@class = "ws-main-header-title ng-binding"]')

        # Rep Code Text Field
        self.rep_code_text_field = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div/ui-view/div/div[2]/div[1]/form/span[1]/span/span/input")

        # Rep Code drop down
        self.rep_code_drop_down = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div/ui-view/div/div[2]/div[1]/form/span[1]/span/span/span[2]/span")

        # View Drop Down
        self.view_drop_down = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div/ui-view/div/div[2]/div[1]/form/span[3]/span/span[2]/span")

        # Date Field
        # self.date_text_field = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div/ui-view/div/div[2]/div[1]/form/span[5]/span/span/input")

        # Search Button
        self.search_button = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div/ui-view/div/div[2]/div[1]/form/button[1]/i")

        return self

    # Validate that Correct Title Displays
    def validate_correct_text_displays(self, test_data, test_case_ID, browser, env, time_stamp):
        text_found = documents.Page_Elements(self).panel_title.get_attribute("innerHTML")
        print(text_found)
        try:
            assert test_data in text_found
        except AssertionError:
            screenshot_name = "FAIL" + "_" + test_case_ID + "_" + browser + "_" + env + "_" + time_stamp + ".png"
            saved_screenshot_location = str(screenshot_directory / screenshot_name)
            self.driver.get_screenshot_as_file(saved_screenshot_location)
            raise

    def input_rep_code(self, rep_code):
        documents.Page_Elements(self).rep_code_text_field.click()
        documents.Page_Elements(self).rep_code_text_field.clear()
        documents.Page_Elements(self).rep_code_text_field.send_keys(rep_code)
        documents.Page_Elements(self).rep_code_text_field.send_keys(Keys.ENTER)

    def input_rep_code_new(self, rep_code):
        actions = ActionChains(self.driver)
        actions.move_to_element(self.driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div/ui-view/div/div[2]/div[1]/form/span[1]/span/span/input")).click().perform()
        actions.send_keys(rep_code)
        actions.perform()

    def click_rep_code(self):
        documents.Page_Elements(self).rep_code_text_field.click()

    def select_confirms_old(self):

        documents.Page_Elements(self).view_drop_down.click()
        actions = ActionChains(self.driver)
        actions.send_keys(Keys.ARROW_DOWN)
        actions.send_keys(Keys.ENTER)
        actions.send_keys(Keys.TAB)
        actions.perform()

        # select_confirms = self.driver.find_element(By.XPATH, "//select[@class='k-item']/option[@value='Confirms']")
        # select_confirms.click()
        #
        # documents.Page_Elements(self).driver.send_keys('Confirms')

    def select_confirms(self):
        actions = ActionChains(self.driver)
        actions.move_to_element(self.driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div/ui-view/div/div[2]/div[1]/form/span[3]/span[1]/span[2]/span")).click().perform()
        actions.send_keys(Keys.ARROW_DOWN)
        actions.perform()

    def select_open_order_confirms(self):
        documents.Page_Elements(self).view_drop_down.click()
        actions = ActionChains(self.driver)
        actions.send_keys(Keys.ARROW_DOWN)
        actions.send_keys(Keys.ARROW_DOWN)
        actions.send_keys(Keys.ENTER)
        actions.send_keys(Keys.TAB)
        actions.perform()

    def select_monthly_statements(self):
        documents.Page_Elements(self).view_drop_down.click()
        actions = ActionChains(self.driver)
        actions.send_keys(Keys.ARROW_DOWN)
        actions.send_keys(Keys.ARROW_DOWN)
        actions.send_keys(Keys.ARROW_DOWN)
        actions.send_keys(Keys.ENTER)
        actions.perform()


    def select_tax_statements(self):
        documents.Page_Elements(self).view_drop_down.click()
        actions = ActionChains(self.driver)
        actions.send_keys(Keys.ARROW_DOWN)
        actions.perform()

    def select_401B_letters(self):
        documents.Page_Elements(self).view_drop_down.click()
        actions = ActionChains(self.driver)
        actions.send_keys(Keys.ARROW_DOWN)
        actions.send_keys(Keys.ARROW_DOWN)
        actions.send_keys(Keys.ARROW_DOWN)
        actions.send_keys(Keys.ENTER)
        actions.send_keys(Keys.TAB)
        actions.perform()

    def select_arrow_down(self):
        documents.Page_Elements(self).view_drop_down.click()
        actions = ActionChains(self.driver)
        actions.send_keys(Keys.ARROW_DOWN)
        actions.send_keys(Keys.ENTER)
        actions.send_keys(Keys.TAB)
        actions.perform()

    def select_GMAP_reports(self):
        documents.Page_Elements(self).view_drop_down.click()
        actions = ActionChains(self.driver)
        actions.send_keys(Keys.ARROW_DOWN)
        actions.send_keys(Keys.ARROW_DOWN)
        actions.send_keys(Keys.ARROW_DOWN)
        actions.send_keys(Keys.ARROW_DOWN)
        actions.send_keys(Keys.ARROW_DOWN)
        actions.send_keys(Keys.ARROW_DOWN)
        actions.send_keys(Keys.ENTER)
        actions.send_keys(Keys.TAB)
        actions.perform()

    def input_date(self, date_value):
        date_text_field = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div/ui-view/div/div[2]/div[1]/form/span[5]/span/span/input")
        date_text_field.click()
        date_text_field.send_keys(date_value)

    def click_search_button(self):
        documents.Page_Elements(self).search_button.click()

    def click_confirms_document(self):
        confirms_document = self.driver.find_element(By.XPATH,
                                                "/html/body/div[1]/div[3]/div/div/ui-view/div/div[2]/div[2]/div/div[1]/div/a[1]")
        confirms_document.click()


