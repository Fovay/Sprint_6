import allure
from pages.base_page import BasePage
from locators.home_page_locators import HomePageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage(BasePage):
    @allure.step('Принять cookies')
    def accept_cookies(self):
        try:
            if self.is_element_displayed(HomePageLocators.COOKIE_ACCEPT_BUTTON, 3):
                self.click_element(HomePageLocators.COOKIE_ACCEPT_BUTTON)
        except Exception:
            pass
    
    @allure.step('Клик по кнопке "Заказать" в хедере')
    def click_order_button_top(self):
        self.click_with_js(HomePageLocators.ORDER_BUTTON_TOP)
    
    @allure.step('Клик по кнопке "Заказать" внизу страницы')
    def click_order_button_bottom(self):
        self.click_with_js(HomePageLocators.ORDER_BUTTON_BOTTOM)
    
    @allure.step('Клик по логотипу Самоката')
    def click_scooter_logo(self):
        self.click_element(HomePageLocators.SCOOTER_LOGO)
    
    @allure.step('Клик по логотипу Яндекса')
    def click_yandex_logo(self):
        try:
            self.click_element(HomePageLocators.YANDEX_LOGO)
        except:
            try:
                self.click_element(HomePageLocators.YANDEX_LOGO_BY_IMG)
            except:
                try:
                    self.click_element(HomePageLocators.YANDEX_LOGO_BY_HREF)
                except:
                    self.click_element(HomePageLocators.YANDEX_LOGO_FALLBACK)
    
    @allure.step('Получить ответ на вопрос')
    def get_answer_text(self, question_number):
        question_locator = (By.XPATH, HomePageLocators.QUESTION_PATTERN.format(question_number))
        answer_locator = (By.XPATH, HomePageLocators.ANSWER_PATTERN.format(question_number))
        question_element = self.find_element(question_locator)
        self.scroll_to_element(question_element)
        self.click_element(question_locator)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(answer_locator))
        return self.get_text(answer_locator)