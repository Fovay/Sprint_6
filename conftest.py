import pytest
from selenium import webdriver
from data.urls import Urls

@pytest.fixture()
def driver():
    driver = webdriver.Firefox()
    driver.get(Urls.main_page)
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture()
def home_page(driver):
    from pages.home_page import HomePage
    page = HomePage(driver)
    page.accept_cookies()
    return page

@pytest.fixture()
def order_page(driver):
    from pages.order_page import OrderPage
    return OrderPage(driver)