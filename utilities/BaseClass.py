import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")
class BaseClass:

    def wait_to_load_page(self, text):
        wait = WebDriverWait(self.driver, 7).until(expected_conditions.presence_of_element_located((By.LINK_TEXT, text)))
