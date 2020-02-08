from selenium import webdriver
from config_globals import *

class build_base_url():

    def return_home_index_string(self):
        home_index_string = "/home/index#!"
        return home_index_string

    def return_logout_string(self):
        logout_string = "user/login?logout=1"
        return logout_string