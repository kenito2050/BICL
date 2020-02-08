from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

class user_drop_down():

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

    def click_help(self):
        actions = ActionChains(self.driver)
        actions.move_to_element(self.driver.find_element(By.XPATH, "/html/body/div[1]/header/div[2]/div/ul/div[1]/li[1]/a")).click().perform()

    def close_help_modal(self):
        actions = ActionChains(self.driver)
        actions.move_to_element(self.driver.find_element(By.XPATH, "/html/body/div[7]/div[1]/div/a[2]")).click().perform()

    def click_change_password(self):
        actions = ActionChains(self.driver)
        actions.move_to_element(self.driver.find_element(By.XPATH, "/html/body/div[1]/header/div[2]/div/ul/div[1]/li[2]/a")).click().perform()

    def close_password_modal(self):
        actions = ActionChains(self.driver)
        actions.move_to_element(
        self.driver.find_element(By.XPATH, "/html/body/div[5]/div[1]/div/a[2]/span")).click().perform()

    def click_announcements(self):
        actions = ActionChains(self.driver)
        actions.move_to_element(self.driver.find_element(By.XPATH, "/html/body/div[1]/header/div[2]/div/ul/div[1]/li[3]/a")).click().perform()

    def close_announcements_modal(self):
        actions = ActionChains(self.driver)
        actions.move_to_element(
        self.driver.find_element(By.XPATH, "/html/body/div[5]/div[1]/div/a[2]/span")).click().perform()

    def click_client_link(self):
        actions = ActionChains(self.driver)
        actions.move_to_element(self.driver.find_element(By.XPATH, "/html/body/div[1]/header/div[2]/div/ul/div[2]/li/a")).click().perform()

    def click_logout(self):
        actions = ActionChains(self.driver)
        actions.move_to_element(self.driver.find_element(By.XPATH, "/html/body/div[1]/header/div[2]/div/ul/li/a")).click().perform()
