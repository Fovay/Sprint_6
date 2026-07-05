import allure
from data.urls import Urls

@allure.epic("Навигация")
class TestLogo:
    @allure.feature("Логотипы")
    @allure.title("Проверка логотипа Самоката")
    def test_scooter_logo_redirect(self, home_page):
        home_page.click_scooter_logo()
        current_url = home_page.get_current_url()
        assert Urls.MAIN_PAGE in current_url
    
    @allure.feature("Логотипы")
    @allure.title("Проверка логотипа Яндекса")
    def test_yandex_logo_redirect(self, home_page):
        home_page.click_yandex_logo()
        home_page.wait_for_number_of_windows(2)
        home_page.switch_to_new_window()
        home_page.wait_for_page_load()
        current_url = home_page.get_current_url()
        assert (Urls.DZEN_HOME_PAGE in current_url.lower() 
                or Urls.YANDEX_HOME_PAGE in current_url.lower() 
                or Urls.YANDEX_CAPTCHA_PAGE in current_url.lower())