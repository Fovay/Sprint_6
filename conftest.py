import pytest
from selenium import webdriver
from data.urls import Urls

@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Firefox()
    driver.get(Urls.MAIN_PAGE)
    driver.maximize_window()
    yield driver
    driver.quit()