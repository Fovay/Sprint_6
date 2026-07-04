import allure
from pages.base_page import BasePage
from locators.home_page_locators import HomePageLocators
from selenium.webdriver.common.by import By

class HomePage(BasePage):
    
    @allure.step('Принять cookies')
    def accept_cookies(self):
        try:
            if self.is_element_displayed(HomePageLocators.cookie_accept_button, 3):
                self.click_element(HomePageLocators.cookie_accept_button)
        except Exception:
            pass
    
    @allure.step('Клик по кнопке "Заказать" в хедере')
    def click_order_button_top(self):
        button = self.find_element(HomePageLocators.order_button_top)
        self.scroll_to_element(button)
        self.driver.execute_script("arguments[0].click();", button)
    
    @allure.step('Клик по кнопке "Заказать" внизу страницы')
    def click_order_button_bottom(self):
        # Скроллим вниз до кнопки
        button = self.find_element(HomePageLocators.order_button_bottom)
        self.scroll_to_element(button)
        self.driver.execute_script("arguments[0].click();", button)
    
    @allure.step('Клик по логотипу Самоката')
    def click_scooter_logo(self):
        self.click_element(HomePageLocators.scooter_logo)
    
    @allure.step('Клик по логотипу Яндекса')
    def click_yandex_logo(self):
        try:
            self.click_element(HomePageLocators.yandex_logo)
        except:
            try:
                self.click_element((By.XPATH, "//img[@alt='Yandex']/parent::a"))
            except:
                try:
                    self.click_element((By.XPATH, "//a[contains(@href, 'yandex')]"))
                except:
                    self.click_element((By.XPATH, "//div[contains(@class, 'Header')]//a[not(contains(@class, 'Header_LogoScooter'))]"))
    
    @allure.step('Получить ответ на вопрос')
    def get_answer_text(self, question_number):
        question_locator = (By.XPATH, HomePageLocators.question_pattern.format(question_number))
        answer_locator = (By.XPATH, HomePageLocators.answer_pattern.format(question_number))
        
        question_element = self.find_element(question_locator)
        self.scroll_to_element(question_element)
        
        self.click_element(question_locator)
        return self.get_text(answer_locator)