from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from data.urls import Urls

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_element_located(locator),
            message=f"Can't find element by locator {locator}"
        )

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_all_elements_located(locator),
            message=f"Can't find elements by locator {locator}"
        )

    def click_element(self, locator, time=10):
        element = self.find_element(locator, time)
        self.scroll_to_element(element)
        element.click()

    def send_keys(self, locator, text, time=10):
        element = self.find_element(locator, time)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator, time=10):
        return self.find_element(locator, time).text

    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def go_to_site(self, url=None):
        if url is None:
            url = Urls.MAIN_PAGE
        self.driver.get(url)

    def get_current_url(self):
        return self.driver.current_url

    def switch_to_new_window(self):
        current_window = self.driver.current_window_handle
        for window_handle in self.driver.window_handles:
            if window_handle != current_window:
                self.driver.switch_to.window(window_handle)
                break

    def wait_for_page_load(self, timeout=10):
        WebDriverWait(self.driver, timeout).until(lambda d: d.current_url != "about:blank")

    def is_element_displayed(self, locator, time=5):
        try:
            return self.find_element(locator, time).is_displayed()
        except TimeoutException:
            return False

    def wait_for_number_of_windows(self, count, time=10):
        WebDriverWait(self.driver, time).until(EC.number_of_windows_to_be(count))

    def get_current_window_handle(self):
        return self.driver.current_window_handle

    def get_window_handles(self):
        return self.driver.window_handles

    def click_with_js(self, locator, time=10):
        element = self.find_element(locator, time)
        self.scroll_to_element(element)
        self.driver.execute_script("arguments[0].click();", element)