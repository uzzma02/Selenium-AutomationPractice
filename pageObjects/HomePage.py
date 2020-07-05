from selenium.webdriver.common.by import By

from pageObjects.AuthenticationPage import AuthenticationPage
from selenium.webdriver import ActionChains


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    store_logo = (By.ID, "header_logo")
    sign_in = (By.LINK_TEXT, "Sign in")

    # Navbar options
    women_menu = (By.LINK_TEXT, "WOMEN")
    dresses_menu = (By.LINK_TEXT, "DRESSES")
    tshirts_menu = (By.LINK_TEXT, "T-SHIRTS")

    def get_store_logo(self):
        return self.driver.find_element(*HomePage.store_logo)

    # Redirect to Authentication Page
    def get_sign_in(self):
        self.driver.find_element(*HomePage.sign_in).click()
        authentication_page = AuthenticationPage(self.driver)
        return authentication_page

    def get_dresses_dropdown(self):
        hover_action = ActionChains(self.driver)
        hover_action.move_to_element(self.driver.find_element_by_link_text).perform()