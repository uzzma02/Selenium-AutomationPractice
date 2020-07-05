from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class RegistrationPage:

    def __init__(self, driver):
        self.driver = driver

    customer_male = (By.ID, "uniform-id_gender1")
    customer_female = (By.ID, "uniform-id_gender2")
    customer_firstname = (By.ID, "customer_firstname")
    customer_lastname = (By.ID, "customer_lastname")
    email = (By.ID, "email")
    password = (By.ID, "passwd")
    dob_day = (By.NAME, "days")
    dob_month = (By.NAME, "months")
    dob_year = (By.NAME, "years")
    newsletter_signup = (By.NAME, "newsletter")
    address_firstname = (By.NAME, "firstname")
    address_lastname = (By.NAME, "lastname")
    street_address = (By.NAME, "address1")
    address_city = (By.NAME, "city")
    address_state = (By.NAME, "id_state")
    address_zipcode = (By.NAME, "postcode")
    address_country = (By.NAME, "id_country")
    customer_mobile = (By.NAME, "phone_mobile")
    address_alias = (By.NAME, "alias")
    register = (By.NAME, "submitAccount")

    # def get_customer_male(self):
    #     return self.driver.find_element(*RegistrationPage.customer_male)
    #
    # def get_customer_female(self):
    #     return self.driver.find_element(*RegistrationPage.customer_female)

    def get_customer_firstname(self):
        return self.driver.find_element(*RegistrationPage.customer_firstname)

    def get_customer_lastname(self):
        return self.driver.find_element(*RegistrationPage.customer_lastname)

    def get_email(self):
        return self.driver.find_element(*RegistrationPage.email)

    def get_password(self):
        return self.driver.find_element(*RegistrationPage.password)

    def get_dob_day(self, text):
        return self.driver.find_element(*RegistrationPage.dob_day).click()

    def get_dob_month(self):
        return self.driver.find_element(*RegistrationPage.dob_month).click()

    def get_dob_year(self):
        return self.driver.find_element(*RegistrationPage.dob_year).click()

    def get_newsletter_signup(self):
        return self.driver.find_element(*RegistrationPage.newsletter_signup)

    def get_address_firstname(self):
        return self.driver.find_element(*RegistrationPage.address_firstname)

    def get_address_lastname(self):
        return self.driver.find_element(*RegistrationPage.address_lastname)

    def get_street_address(self):
        return self.driver.find_element(*RegistrationPage.street_address)

    def get_address_city(self):
        return self.driver.find_element(*RegistrationPage.address_city)

    def get_address_state(self):
        return self.driver.find_element(*RegistrationPage.address_state)

    def get_address_zipcode(self):
        return self.driver.find_element(*RegistrationPage.address_zipcode)

    def get_address_country(self):
        return self.driver.find_element(*RegistrationPage.address_country)

    def get_customer_mobile(self):
        return self.driver.find_element(*RegistrationPage.customer_mobile)

    def get_address_alias(self):
        return self.driver.find_element(*RegistrationPage.address_alias)

    # def get_register_account(self):
