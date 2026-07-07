import allure
import pytest
from pages.home_page import HomePage
from data.urls import Urls
from data.test_data import TestData

@allure.epic('Главная страница')
@allure.parent_suite('Домашняя страница')
class TestHomePage:
    @allure.feature('Вопросы о важном')
    @allure.story('Проверка ответов на вопросы')
    @allure.title('Проверка ответа на вопрос №{question_number}')
    @pytest.mark.parametrize("question_number, expected_answer", TestData.QUESTIONS)
    def test_questions_answers(self, driver, question_number, expected_answer):
        home_page = HomePage(driver)
        home_page.accept_cookies()
        actual_answer = home_page.get_answer_text(question_number)
        assert actual_answer == expected_answer

    @allure.feature('Переход к оформлению заказа')
    @allure.story('Кнопка заказа в хедере')
    @allure.title('Нажатие на кнопку "Заказать" в хедере')
    def test_click_top_order_button_show_order_page(self, driver):
        home_page = HomePage(driver)
        home_page.accept_cookies()
        home_page.click_order_button_top()
        assert home_page.get_current_url() == Urls.ORDER_PAGE

    @allure.feature('Переход к оформлению заказа')
    @allure.story('Кнопка заказа внизу страницы')
    @allure.title('Нажатие на кнопку "Заказать" внизу страницы')
    def test_click_bottom_order_button_show_order_page(self, driver):
        home_page = HomePage(driver)
        home_page.accept_cookies()
        home_page.click_order_button_bottom()
        assert home_page.get_current_url() == Urls.ORDER_PAGE
        
    @allure.feature('Переход на Яндекс')
    @allure.story('Логотип Яндекса')
    @allure.title('При нажатии на логотип Яндекса происходит переход на Дзен')
    def test_click_yandex_button_go_to_yandex(self, driver):
        home_page = HomePage(driver)
        home_page.accept_cookies()
        home_page.click_yandex_logo()
        home_page.wait_for_number_of_windows(2)
        home_page.switch_to_new_window()
        home_page.wait_for_page_load()
        current_url = home_page.get_current_url()
        assert Urls.DZEN_HOME_PAGE in current_url.lower()