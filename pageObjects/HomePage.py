from selenium.webdriver.common.by import By
import time

from pageObjects.AuthenticationPage import AuthenticationPage
from selenium.webdriver import ActionChains

from pageObjects.CasualDressesPage import CasualDressesPage
from pageObjects.ContactUsPage import ContactUsPage
from pageObjects.DressesPage import DressesPage
from pageObjects.EveningDressesPage import EveningDressesPage
from pageObjects.SummerDressesPage import SummerDressesPage


class HomePage:

    def __init__(self, driver):
        self.driver = driver
    # header
    store_logo = (By.ID, "header_logo")
    sign_in = (By.LINK_TEXT, "Sign in")
    contact_us = (By.XPATH, "//a[@title='Contact Us']")

    # Navbar options
    women_menu = (By.LINK_TEXT, "WOMEN")
    dresses_menu = (By.LINK_TEXT, "DRESSES")
    tshirts_menu = (By.LINK_TEXT, "T-SHIRTS")
    casual_dresses_menu = (By.LINK_TEXT, "Casual Dresses")
    evening_dresses_menu = (By.LINK_TEXT, "Evening Dresses")
    summer_dresses_menu = (By.LINK_TEXT, "Summer Dresses")

    # Search box
    search_box = (By.ID, "searchbox")


    def get_store_logo(self):
        return self.driver.find_element(*HomePage.store_logo)

    def get_contact_us(self):
        self.driver.find_element(*HomePage.contact_us).click()
        contact_us_page = ContactUsPage(self.driver)
        return contact_us_page

    # Redirect to Authentication Page
    def get_sign_in(self):
        self.driver.find_element(*HomePage.sign_in).click()
        authentication_page = AuthenticationPage(self.driver)
        return authentication_page

    # Redirect to Casual dresses Page
    # def get_casual_dresses(self):
    #     hover_action = ActionChains(self.driver)
    #     hover_action.move_to_element(self.driver.find_element(*HomePage.dresses_menu)).perform()
    #     time.sleep(3)
    #     hover_action.move_to_element(self.driver.find_element(*HomePage.casual_dresses_menu)).click()
    #     time.sleep(2)
    #     casual_dresses_page = CasualDressesPage(self.driver)  # Casual Dresses page object
    #     return casual_dresses_page

    def get_search(self):
        return self.driver.find_element(*HomePage.search_box).click()

    def get_dresses(self):
        self.driver.find_element(*HomePage.dresses_menu).click()
        dresses_page = DressesPage(self.driver)
        return dresses_page

    def get_casual_dresses(self):
        self.driver.find_element(*HomePage.casual_dresses_menu).click()
        casual_dresses_page = CasualDressesPage(self.driver)
        return casual_dresses_page

    def get_evening_dresses(self):
        self.driver.find_element(*HomePage.evening_dresses_menu).click()
        evening_dresses_page = EveningDressesPage(self.driver)
        return evening_dresses_page

    def get_summer_dresses(self):
        self.driver.find_element(*HomePage.summer_dresses_menu).click()
        summer_dresses_page = SummerDressesPage(self.driver)
        return summer_dresses_page



