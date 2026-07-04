from selenium.webdriver.common.by import By

class HomePageLocators:
    order_button_top = (By.XPATH, "//div[starts-with(@class, 'Header')]/button[text()='Заказать']")
    order_button_bottom = (By.XPATH, "//div[starts-with(@class, 'Home')]//button[text()='Заказать']")

    question_pattern = "//div[@id='accordion__heading-{}']"
    answer_pattern = "//div[@id='accordion__panel-{}']/p"

    scooter_logo = (By.XPATH, "//img[@alt='Scooter']")
    yandex_logo = (By.XPATH, "//a[contains(@class, 'Header_LogoYandex')]")

    cookie_accept_button = (By.XPATH, "//button[text()='да все привыкли']")