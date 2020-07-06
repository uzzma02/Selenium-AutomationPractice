import time

from selenium.webdriver import ActionChains

from pageObjects.AuthenticationPage import AuthenticationPage
from pageObjects.CasualDressesPage import CasualDressesPage
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass
import pytest


class TestHomePage(BaseClass):

    # def test_load_Homepage(self):
    #     home_page = HomePage(self.driver)
    #     self.wait_to_load_page("Sign in")
    #     print("Homepage loaded")

    def test_home_page_sign_in(self):
        home_page = HomePage(self.driver)
        self.wait_to_load_page("Sign in")
        # Test Authentication page redirect
        home_page.get_sign_in()
        time.sleep(3)

    # def test_casual_dresses_redirect(self):
    #     home_page = HomePage(self.driver)
    #     self.wait_to_load_page("DRESSES")
    #     # Test Casual Dresses page redirect
    #     home_page.get_casual_dresses()
    #     time.sleep(3)

    def test_dresses_page_redirect(self):
        home_page = HomePage(self.driver)
        home_page.get_dresses()



