import allure
import pytest
from data.test_data import TestData
from data.urls import Urls
from locators.order_page_locators import OrderPageLocators

@allure.epic('Создание заказа')
class TestOrder:
    @allure.feature('Оформление заказа')
    @allure.title('Создание заказа')
    @pytest.mark.parametrize('order_data', TestData.ORDER_DATA)
    def test_create_order(self, home_page, order_page, order_data):
        button_location = order_data.get('button_location', 'top')
        if button_location == "top":
            home_page.click_order_button_top()
        else:
            home_page.click_order_button_bottom()
        order_page.fill_user_data(order_data)
        order_page.go_next()
        order_page.fill_rent_data(order_data)
        order_page.click_order()
        order_page.click_accept_order()
        assert len(order_page.find_elements(OrderPageLocators.ORDER_COMPLETED_INFO)) > 0
    
    @allure.feature('Оформление заказа')
    @allure.title('Оформление заказа и переход на страницу статуса')
    @pytest.mark.parametrize('order_data', [TestData.ORDER_DATA[0], TestData.ORDER_DATA[1]])
    def test_order_and_go_to_status(self, home_page, order_page, order_data):
        button_location = order_data.get('button_location', 'top')
        if button_location == "top":
            home_page.click_order_button_top()
        else:
            home_page.click_order_button_bottom()
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