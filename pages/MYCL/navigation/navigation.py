from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.MYCL.navigation.Screens import Screens
from config_globals import *

class navigation():

    def __init__(self, driver):
        self.driver = driver

