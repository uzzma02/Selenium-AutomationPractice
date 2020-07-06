import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class DressesPage:

    def __init__(self, driver):
        self.driver = driver

    category_casual = (By.LINK_TEXT, "Casual Dresses")
    category_evening = (By.LINK_TEXT, "Evening Dresses")
    category_summer = (By.LINK_TEXT, "Summer Dresses")
    product_containers = (By.XPATH, "//div[@class='product-container']")
    quick_view = (By.XPATH, "//div[@class='product-image-container']/a[2]")
    add_to_cart = (By.XPATH, "//span[contains(text(), 'Add to cart')]")
    product_list = (By.XPATH, "//div[@class='product-container']")

    def get_casual_dresses_list(self):
        return self.driver.find_element(*DressesPage.category_casual).click()

    def get_evening_dresses_list(self):
        return self.driver.find_element(*DressesPage.category_evening).click()

    def get_summer_dresses_list(self):
        return self.driver.find_element(*DressesPage.category_summer).click()

    def get_product_list_names(self):
        products = self.driver.find_elements_by_xpath("//div[@class='product-container']")
        list_of_products = []
        for product in products:
            list_of_products.append(product.find_element_by_xpath("div/h5/a").text)
        return list_of_products

    def get_product_list_prices(self):
        hover_action = ActionChains(self.driver)
        hover_action.move_to_element(self.driver.find_element_by_xpath("//div[@class='product-container']/div[2]/h5/a")).perform()
        print(hover_action.move_to_element(self.driver.find_element_by_xpath("//div[@class='product-image-container']/div[2]/span")).text)

        # list_of_prices = []
        # for product in products:
        #     print(list_of_prices.append(product.find_element_by_xpath("div/span").text))

    def get_quick_view(self):
        hover_action = ActionChains(self.driver)
        hover_action.move_to_element(self.driver.find_element(*DressesPage.product_containers)).perform()
        hover_action.move_to_element(self.driver.find_element(*DressesPage.quick_view)).click()

    def get_add_to_cart(self, product_chosen):
        hover_action = ActionChains(self.driver)
        products = self.driver.find_elements(*DressesPage.product_list)
        for product in products:
            print(product)
            if product == product_chosen:
                hover_action.move_to_element(product).perform()
                hover_action.move_to_element(self.driver.find_element(*DressesPage.add_to_cart)).click()
            break

