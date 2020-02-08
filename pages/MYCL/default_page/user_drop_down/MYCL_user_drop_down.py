from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

class MYCL_user_drop_down():

    def __init__(self, driver):
        self.driver = driver

    def Page_Elements(self):

        # Help

        # Change Password

        # Announcements

        # Client Link
        # self.client_link = self.driver.find_element(By.XPATH, "/html/body/div[1]/header/div[2]/div/ul/div[2]/li/a")

        # Logout

        return self

    # Actions

    def click_contact_us(self):
        contact_us = self.driver.find_element(By.LINK_TEXT, "Contact Us")
        actions = ActionChains(self.driver)
        actions.move_to_element(contact_us).click().perform()

        # actions = ActionChains(self.driver)
        # actions.move_to_element(self.driver.find_element(By.XPATH, "/html/body/div[1]/header/div[2]/div/ul/div[1]/li[1]/a")).click().perform()

    def click_user_preferences(self):
        user_preference = self.driver.find_element(By.LINK_TEXT, "User Preference")
        actions = ActionChains(self.driver)
        actions.move_to_element(user_preference).click().perform()

        # actions = ActionChains(self.driver)
        # actions.move_to_element(self.driver.find_element(By.XPATH, "/html/body/div[1]/header/div[2]/div/ul/div[1]/li[2]/a")).click().perform()

    def click_account_preferences(self):
        account_preference = self.driver.find_element(By.LINK_TEXT, "Account Preference")
        actions = ActionChains(self.driver)
        actions.move_to_element(account_preference).click().perform()

        # actions = ActionChains(self.driver)
        # actions.move_to_element(self.driver.find_element(By.XPATH, "/html/body/div[1]/header/div[2]/div/ul/div[1]/li[3]/a")).click().perform()

    def click_help(self):
        actions = ActionChains(self.driver)
        actions.move_to_element(self.driver.find_element(By.XPATH, "/html/body/div[1]/header/div[2]/div/ul/div/li[1]/a")).click().perform()

    def click_change_password(self):
        actions = ActionChains(self.driver)
        actions.move_to_element(self.driver.find_element(By.XPATH, "/html/body/div[1]/header/div[2]/div/ul/div/li[2]/a")).click().perform()

    def click_announcements(self):
        actions = ActionChains(self.driver)
        actions.move_to_element(self.driver.find_element(By.XPATH, "/html/body/div[1]/header/div[2]/div/ul/div/li[3]/a")).click().perform()

    def click_logout(self):
        actions = ActionChains(self.driver)
        actions.move_to_element(self.driver.find_element(By.XPATH, "/html/body/div[1]/header/div[2]/div/ul/li/a")).click().perform()