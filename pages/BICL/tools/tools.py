from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from config_globals import *

class tools():

    def __init__(self, driver):
        self.driver = driver

    def Page_Elements(self):

        # Client Search

        # Stock Record

        # ACATS

        # Bond Rating

        # FolioDX

        # Calculators

        # Research

        # Wedbush Research

        # Firelight -- Displays only if configured in Admin Tool

        return self

    # Actions

    def click_client_search(self):
        client_search = self.driver.find_element(By.LINK_TEXT, "Client Search")
        actions = ActionChains(self.driver)
        actions.move_to_element(client_search).click().perform()

    def click_stock_record(self):
        stock_record = self.driver.find_element(By.LINK_TEXT, "Stock Record")
        actions = ActionChains(self.driver)
        actions.move_to_element(stock_record).click().perform()

    def click_acats(self):
        acats = self.driver.find_element(By.LINK_TEXT, "ACATS")
        actions = ActionChains(self.driver)
        actions.move_to_element(acats).click().perform()

    def click_bond_rating(self):
        bond_rating = self.driver.find_element(By.LINK_TEXT, "Bond Rating")
        actions = ActionChains(self.driver)
        actions.move_to_element(bond_rating).click().perform()

    def click_foliodx(self):
        folio_dx = self.driver.find_element(By.LINK_TEXT, "FolioDX")
        actions = ActionChains(self.driver)
        actions.move_to_element(folio_dx).click().perform()

    def click_calculators(self):
        calculators = self.driver.find_element(By.LINK_TEXT, "Calculators")
        actions = ActionChains(self.driver)
        actions.move_to_element(calculators).click().perform()

    def click_research(self):
        research = self.driver.find_element(By.LINK_TEXT, "Research")
        actions = ActionChains(self.driver)
        actions.move_to_element(research).click().perform()

    def click_wedbush_research(self):
        wedbush_research = self.driver.find_element(By.LINK_TEXT, "Wedbush Research")
        actions = ActionChains(self.driver)
        actions.move_to_element(wedbush_research).click().perform()

    def click_firelight(self):
        firelight = self.driver.find_element(By.LINK_TEXT, "Firelight")
        actions = ActionChains(self.driver)
        actions.move_to_element(firelight).click().perform()

    def confirm_firelight_displays(self, test_case_ID, browser, env, time_stamp):

        firelightDisplays = False

        # Check if Firelight Displays
        if len(self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[2]/div/div/ul/li[9]/a")) > 0:
            firelightDisplays = True
        else:
            print("Firelight Not Found")

        # Try / Except Block to test if firelightDisplays True
        # If False, throw exception, take screenshot and FAIL test

        try:
            assert firelightDisplays is True
        except AssertionError:
            screenshot_name = "FAIL" + "_" + test_case_ID + "_" + browser + "_" + env + "_" + time_stamp + ".png"
            saved_screenshot_location = str(screenshot_directory / screenshot_name)
            self.driver.get_screenshot_as_file(saved_screenshot_location)
            raise

    def confirm_firelight_not_present(self, test_case_ID, browser, env, time_stamp):

        firelightDisplays = False

        # Check if Firelight not present
        if len(self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[2]/div/div/ul/li[9]/a")) > 0:
            firelightDisplays = True
        else:
            print("Firelight Not Found")

        # Try / Except Block to test if firelightDisplays True
        # If False, throw exception, take screenshot and FAIL test

        try:
            assert firelightDisplays is False
        except AssertionError:
            screenshot_name = "FAIL" + "_" + test_case_ID + "_" + browser + "_" + env + "_" + time_stamp + ".png"
            saved_screenshot_location = str(screenshot_directory / screenshot_name)
            self.driver.get_screenshot_as_file(saved_screenshot_location)
            raise