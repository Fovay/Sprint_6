import allure
from data.urls import Urls
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@allure.epic("Навигация")
class TestLogo:
    @allure.feature("Логотипы")
    @allure.title("Проверка логотипа Самоката")
    def test_scooter_logo_redirect(self, home_page):
        home_page.click_scooter_logo()
        current_url = home_page.get_current_url()
        assert Urls.main_page in current_url
    
    @allure.feature("Логотипы")
    @allure.title("Проверка логотипа Яндекса")
    def test_yandex_logo_redirect(self, home_page, driver):
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