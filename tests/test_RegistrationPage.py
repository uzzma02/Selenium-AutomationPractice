import time

from pageObjects.AuthenticationPage import AuthenticationPage
from pageObjects.HomePage import HomePage
from pageObjects.RegistrationPage import RegistrationPage
from utilities.BaseClass import BaseClass


class TestRegistrationPage(BaseClass):

    def test_registration_form(self):
        home_page = HomePage(self.driver)  # Home page object
        home_page.get_sign_in()
        time.sleep(5)

        auth_page = AuthenticationPage(self.driver)  # Authentication page object
        auth_page.get_create_email().send_keys("uzzma03@gmail.com")
        auth_page.get_authentication_page()
        time.sleep(5)

        register_account = RegistrationPage(self.driver)  # Registration page object
        register_account.get_customer_firstname().send_keys("John")
        register_account.get_customer_lastname().send_keys("Doe")
        register_account.get_password().send_keys("12345678")
        #register_account.get_dob_day()
        time.sleep(5)

        self.driver.execute_script("window.scrollTo(0, 500);")

        register_account.get_address_firstname().send_keys("Jane")
        register_account.get_address_lastname().send_keys("Doe")
        register_account.get_street_address().send_keys("1000 Bush Street")
        register_account.get_address_city().send_keys("New York")

        self.driver.execute_script("window.scrollTo(0, 1000);")

        register_account.get_address_zipcode().send_keys("91000")
        register_account.get_customer_mobile().send_keys("5100000000")
        register_account.get_address_alias().send_keys("My address")