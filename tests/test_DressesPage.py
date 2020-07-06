import time

from pageObjects.CasualDressesPage import CasualDressesPage
from pageObjects.DressesPage import DressesPage
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestDressesPage(BaseClass):

    def test_chiffon_dress_selection(self):
        home_page = HomePage(self.driver)
        home_page.get_dresses()
        time.sleep(5)

        # Navigate to dresses page
        dresses_page = DressesPage(self.driver)
        self.driver.execute_script("window.scrollTo(0, 1000);")

        dresses_page.get_add_to_cart("Printed Chiffon Dress")
        time.sleep(5)
        # dresses_page.get_product_list_names()


