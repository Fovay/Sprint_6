import re
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators as Locators

class OrderPage(BasePage):
    def input_first_name(self, first_name: str):
        self.send_keys(Locators.first_name_input, first_name)

    def input_last_name(self, last_name: str):
        self.send_keys(Locators.last_name_input, last_name)

    def input_address(self, address: str):
        self.send_keys(Locators.address_input, address)

    def choose_subway(self, subway_name: str):
        self.click_element(Locators.subway_field)
        button = self.find_element(Locators.subway_hint_button(subway_name))
        self.scroll_to_element(button)
        button.click()

    def input_telephone_number(self, telephone_number: str):
        self.send_keys(Locators.telephone_number_field, telephone_number)

    def go_next(self):
        button = self.find_element(Locators.next_button)
        self.scroll_to_element(button)
        self.driver.execute_script("arguments[0].click();", button)

    def input_date(self, date: str):
        self.send_keys(Locators.date_field, date) 

    def choose_rental_period(self, option: int):
        self.click_element(Locators.rental_period_field)
        options = self.find_elements(Locators.rental_period_list)
        self.scroll_to_element(options[option])
        options[option].click()

    def choose_color(self, option: int):
        colors = self.find_elements(Locators.color_checkboxes)
        self.scroll_to_element(colors[option])
        colors[option].click()

    def input_comment(self, comment_text):
        self.send_keys(Locators.comment_for_courier_field, comment_text)

    def click_order(self):
        button = self.find_element(Locators.order_button)
        self.scroll_to_element(button)
        self.driver.execute_script("arguments[0].click();", button)

    def click_accept_order(self):
        button = self.find_element(Locators.accept_order_button)
        self.scroll_to_element(button)
        self.driver.execute_script("arguments[0].click();", button)

    def get_order_number(self):
        wait = WebDriverWait(self.driver, 15)
        wait.until(lambda driver: re.search(r'\d+',driver.find_element(*Locators.order_completed_info).text))
        text = self.find_element(Locators.order_completed_info).text
        match = re.search(r'\d+', text)
        return match.group() if match else ""

    def click_go_to_status(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(Locators.show_status_button))
        button = self.find_element(Locators.show_status_button)
        self.scroll_to_element(button)
        self.driver.execute_script("arguments[0].click();", button)

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