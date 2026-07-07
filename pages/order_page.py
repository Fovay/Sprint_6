import re
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators as Locators

class OrderPage(BasePage):
    @staticmethod
    def _subway_hint_locator(subway_name: str):
        return (By.XPATH, f"//div[text()='{subway_name}']/parent::button")

    def input_first_name(self, first_name: str):
        self.send_keys(Locators.FIRST_NAME_INPUT, first_name)

    def input_last_name(self, last_name: str):
        self.send_keys(Locators.LAST_NAME_INPUT, last_name)

    def input_address(self, address: str):
        self.send_keys(Locators.ADDRESS_INPUT, address)

    def choose_subway(self, subway_name: str):
        self.click_element(Locators.SUBWAY_FIELD)
        button = self.find_element(self._subway_hint_locator(subway_name))
        self.scroll_to_element(button)
        button.click()

    def input_telephone_number(self, telephone_number: str):
        self.send_keys(Locators.TELEPHONE_NUMBER_FIELD, telephone_number)

    def go_next(self):
        self.click(Locators.NEXT_BUTTON)

    def input_date(self, date: str):
        self.send_keys(Locators.DATE_FIELD, date)

    def choose_rental_period(self, option: int):
        self.click_element(Locators.RENTAL_PERIOD_FIELD)
        options = self.find_elements(Locators.RENTAL_PERIOD_LIST)
        self.scroll_to_element(options[option])
        options[option].click()

    def choose_color(self, option: int):
        colors = self.find_elements(Locators.COLOR_CHECKBOXES)
        self.scroll_to_element(colors[option])
        colors[option].click()

    def input_comment(self, comment_text):
        self.send_keys(Locators.COMMENT_FOR_COURIER_FIELD, comment_text)

    def click_order(self):
        self.click(Locators.ORDER_BUTTON)

    def click_accept_order(self):
        self.click(Locators.ACCEPT_ORDER_BUTTON)

    def get_order_number(self):
        self.wait_for_element_visible(Locators.ORDER_COMPLETED_INFO, time=15)
        self.wait_for_condition(lambda: re.search(r'\d+', self.get_text(Locators.ORDER_COMPLETED_INFO)),time=15)
        text = self.get_text(Locators.ORDER_COMPLETED_INFO)
        match = re.search(r'\d+', text)
        return match.group() if match else ""

    def click_go_to_status(self):
        self.click(Locators.SHOW_STATUS_BUTTON)

    def fill_user_data(self, data_set: dict):
        self.input_first_name(data_set['first_name'])
        self.input_last_name(data_set['last_name'])
        self.input_address(data_set['address'])
        self.choose_subway(data_set['subway_name'])
        self.input_telephone_number(data_set['telephone_number'])

    def fill_rent_data(self, data_set: dict):
        self.input_date(data_set['date'])
        self.choose_rental_period(data_set['rental_period'])
        for color_option in data_set['color']:
            self.choose_color(color_option)
        self.input_comment(data_set['comment_for_courier'])