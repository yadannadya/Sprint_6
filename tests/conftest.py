from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import pytest
import curl


@pytest.fixture(scope="function")
def driver():
    options = Options() 
    options.add_argument('--headless')
    driver = webdriver.Firefox(options=options)
    driver.maximize_window()
    driver.get(curl.main_page)
    yield driver
    driver.quit()