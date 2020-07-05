import time

from pageObjects.AuthenticationPage import AuthenticationPage
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestAuthenticationPage(BaseClass):

    def test_create_account(self):
        home_page = HomePage(self.driver)
        home_page.get_sign_in()
        time.sleep(5)
        auth_page = AuthenticationPage(self.driver)
        # element = driver.find_element(someLocatorHere)
        # self.driver.execute_script("arguments[0].scrollIntoView(true);", AuthenticationPage.create_email)
        self.driver.execute_script("window.scrollTo(0, 500);")
        time.sleep(2)
        auth_page.get_create_email().send_keys("uzzma01@gmail.com")
        time.sleep(2)
        auth_page.get_create_email_submit().click()

    def test_sign_in(self):
        home_page = HomePage(self.driver)
        home_page.get_sign_in()
        time.sleep(3)
        auth_page = AuthenticationPage(self.driver)
        # element = driver.find_element(someLocatorHere)
        # self.driver.execute_script("arguments[0].scrollIntoView(true);", AuthenticationPage.create_email)
        self.driver.execute_script("window.scrollTo(0, 500);")
        time.sleep(2)
        auth_page.get_email().send_keys("uzzma02@gmail.com")
        time.sleep(2)
        auth_page.get_password().send_keys("Sep2uzz!")
        time.sleep(3)
        auth_page.get_submit_login().click()
        time.sleep(5)
