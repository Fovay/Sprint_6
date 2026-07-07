import allure
from pages.home_page import HomePage
from pages.order_page import OrderPage
from data.test_data import TestData
from data.urls import Urls
from locators.order_page_locators import OrderPageLocators

@allure.epic('Создание заказа')
class TestOrder:
    @allure.feature('Оформление заказа')
    @allure.title('Создание заказа через кнопку в хедере')
    def test_create_order_from_top_button(self, driver):
        home_page = HomePage(driver)
        home_page.accept_cookies()
        order_page = OrderPage(driver)
        order_data = TestData.ORDER_DATA[0]
        home_page.click_order_button_top()
        order_page.fill_user_data(order_data)
        order_page.go_next()
        order_page.fill_rent_data(order_data)
        order_page.click_order()
        order_page.click_accept_order()
        assert len(order_page.find_elements(OrderPageLocators.ORDER_COMPLETED_INFO)) > 0
    
    @allure.feature('Оформление заказа')
    @allure.title('Создание заказа через кнопку внизу страницы')
    def test_create_order_from_bottom_button(self, driver):
        home_page = HomePage(driver)
        home_page.accept_cookies()
        order_page = OrderPage(driver)
        order_data = TestData.ORDER_DATA[1]
        home_page.click_order_button_bottom()
        order_page.fill_user_data(order_data)
        order_page.go_next()
        order_page.fill_rent_data(order_data)
        order_page.click_order()
        order_page.click_accept_order()
        assert len(order_page.find_elements(OrderPageLocators.ORDER_COMPLETED_INFO)) > 0
    
    @allure.feature('Оформление заказа')
    @allure.title('Оформление заказа и переход на страницу статуса')
    def test_order_and_go_to_status(self, driver):
        home_page = HomePage(driver)
        home_page.accept_cookies()
        order_page = OrderPage(driver)
        order_data = TestData.ORDER_DATA[0]
        home_page.click_order_button_top()
        order_page.fill_user_data(order_data)
        order_page.go_next()
        order_page.fill_rent_data(order_data)
        order_page.click_order()
        order_page.click_accept_order()
        order_number = order_page.get_order_number()
        assert order_number
        order_page.click_go_to_status()
        current_url = order_page.get_current_url()
        assert Urls.ORDER_STATUS_PAGE in current_url
        assert order_number in current_url