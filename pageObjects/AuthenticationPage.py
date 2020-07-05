from selenium.webdriver.common.by import By

from pageObjects.RegistrationPage import RegistrationPage


class AuthenticationPage:

    def __init__(self, driver):
        self.driver = driver

    # Create new account elements
    create_email = (By.ID, "email_create")
    create_email_submit = (By.NAME, "SubmitCreate")

    # Log into existing account elements
    email = (By.ID, "email")
    password = (By.ID, "passwd")
    submit_login = (By.NAME, "SubmitLogin")
    forgot_pwd = (By.LINK_TEXT, "Forgot your password?")

    def get_create_email(self):
        return self.driver.find_element(*AuthenticationPage.create_email)

    def get_create_email_submit(self):
        return self.driver.find_element(*AuthenticationPage.create_email_submit)

    def get_email(self):
        return self.driver.find_element(*AuthenticationPage.email)

    def get_password(self):
        return self.driver.find_element(*AuthenticationPage.password)

    def get_submit_login(self):
        return self.driver.find_element(*AuthenticationPage.submit_login)

    def get_forgot_pwd(self):
        return self.driver.find_element(*AuthenticationPage.forgot_pwd)

    # Redirects to Create Account Page
    def get_authentication_page(self):
        self.driver.find_element(*AuthenticationPage.create_email_submit).click()
        registration_page = RegistrationPage(self.driver)
        return registration_page
