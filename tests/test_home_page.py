import allure
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data.urls import Urls
from data.test_data import TestData

@allure.epic('Главная страница')
@allure.parent_suite('Домашняя страница')
class TestHomePage:
    @allure.feature('Вопросы о важном')
    @allure.story('Проверка ответов на вопросы')
    @allure.title('Проверка ответа на вопрос №{question_number}')
    @pytest.mark.parametrize("question_number, expected_answer", TestData.questions)
    def test_questions_answers(self, home_page, question_number, expected_answer):
        actual_answer = home_page.get_answer_text(question_number)

    @allure.feature('Переход к оформлению заказа')
    @allure.story('Кнопка заказа в хедере')
    @allure.title('Нажатие на кнопку "Заказать" в хедере')
    def test_click_top_order_button_show_order_page(self, home_page):
        home_page.click_order_button_top()
        assert home_page.get_current_url() == Urls.order_page

    @allure.feature('Переход к оформлению заказа')
    @allure.story('Кнопка заказа внизу страницы')
    @allure.title('Нажатие на кнопку "Заказать" внизу страницы')
    def test_click_bottom_order_button_show_order_page(self, home_page):
        home_page.click_order_button_bottom()
        assert home_page.get_current_url() == Urls.order_page
        
    @allure.feature('Переход на Яндекс')
    @allure.story('Логотип Яндекса')
    @allure.title('При нажатии на логотип Яндекса происходит переход на Дзен')
    def test_click_yandex_button_go_to_yandex(self, home_page, driver):
        original_window = driver.current_window_handle
        home_page.click_yandex_logo()
        WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))
        for window_handle in driver.window_handles:
            if window_handle != original_window:
                driver.switch_to.window(window_handle)
                break
        home_page.wait_for_page_load()
        current_url = driver.current_url
        assert (Urls.dzen_home_page in current_url.lower() or Urls.yandex_home_page in current_url.lower() or Urls.yandex_captcha_page in current_url.lower())