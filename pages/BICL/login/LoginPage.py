from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from config_globals import *

class LoginPage():

    def __init__(self, driver):
        self.driver = driver

    def Page_Elements(self):
        # User Name Field
        self.user_field = self.driver.find_element(By.ID, "UserName")

        # Password Field
        self.password_field = self.driver.find_element(By.ID, "Password")

        # Submit Button
        self.submit_button = self.driver.find_element(By.XPATH, "/html/body/div/div/div[1]/form/button")

        return self

    def login(self, username, password):
        LoginPage.Page_Elements(self).user_field.clear()
        LoginPage.Page_Elements(self).user_field.send_keys(username)
        LoginPage.Page_Elements(self).password_field.click()
        LoginPage.Page_Elements(self).password_field.clear()
        LoginPage.Page_Elements(self).password_field.send_keys(password)
        self.driver.implicitly_wait(3)

    def click_login_button(self):
        LoginPage.Page_Elements(self).submit_button.click()

    # IE Login method
    # problem is that IE hangs on the login button click
    def IE_login(self, username, password):
        LoginPage.Page_Elements(self).user_field.clear()
        LoginPage.Page_Elements(self).user_field.send_keys(username)
        LoginPage.Page_Elements(self).password_field.click()
        LoginPage.Page_Elements(self).password_field.clear()
        LoginPage.Page_Elements(self).password_field.send_keys(password)
        LoginPage.Page_Elements(self).password_field.send_keys(Keys.TAB)
        LoginPage.Page_Elements(self).password_field.send_keys(Keys.ENTER)

    def verify_username_field_displays(self, test_case_ID, browser, env, time_stamp):
    # Verify if page loads (username_field should be clickable), if not, throw exception and take screenshot
        try:
            LoginPage.Page_Elements(self).user_field.click()
        except NoSuchElementException:
            screenshot_name = "FAIL" + "_" + test_case_ID + "_" + browser + "_" + env + "_" + time_stamp + ".png"
            saved_screenshot_location = str(screenshot_directory / screenshot_name)
            self.driver.get_screenshot_as_file(saved_screenshot_location)
            raise