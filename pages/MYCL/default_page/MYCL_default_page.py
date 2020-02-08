from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import time
from config_globals import *

class MYCL_default_page():

    def __init__(self, driver):
        self.driver = driver

    def Page_Elements(self):

        #### Left Panel Icons

        #### Upper Right Area

        # User Drop Down
        self.user_drop_down = self.driver.find_element(By.XPATH, "/html/body/div[1]/header/div[2]/i[2]")

        return self

    # Actions

    #### Left Panel


    #### Upper Right Area

    def click_user_drop_down(self):
        MYCL_default_page.Page_Elements(self).user_drop_down.click()

    def click_hamburger_menu(self):
        actions = ActionChains(self.driver)
        actions.move_to_element(self.driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/span[4]/ul/li/span/i")).click().perform()

    def select_client_link(self):
        actions = ActionChains(self.driver)
        actions.move_to_element(self.driver.find_element(By.XPATH,
                                                         "/html/body/div[1]/div[1]/div[1]/span[4]/ul/li/span/i")).click().perform()
        time.sleep(1)
        actions.send_keys(Keys.ARROW_DOWN).perform()
        actions.send_keys(Keys.ENTER).perform()

    # Validate https in current URl
    def validate_https_in_url_address(self, test_data, test_case_ID, browser, env, time_stamp):
        current_url = self.driver.current_url

        try:
            assert test_data in current_url
        except AssertionError:
            screenshot_name = "FAIL" + "_" + test_case_ID + "_" + browser + "_" + env + "_" + time_stamp + ".png"
            saved_screenshot_location = str(screenshot_directory / screenshot_name)
            self.driver.get_screenshot_as_file(saved_screenshot_location)
            raise