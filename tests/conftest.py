import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome()
    driver.get("http://automationpractice.com/index.php")
    driver.maximize_window()

    request.cls.driver = driver
    yield
    driver.close()
