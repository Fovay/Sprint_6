from selenium.webdriver.common.by import By

class HomePageLocators:
    ORDER_BUTTON_TOP = (By.XPATH, "//div[contains(@class, 'Header')]//button[text()='Заказать']")
    ORDER_BUTTON_BOTTOM = (By.XPATH, "//div[contains(@class, 'Home')]//button[text()='Заказать']")

    QUESTION_PATTERN = "//div[@id='accordion__heading-{}']"
    ANSWER_PATTERN = "//div[@id='accordion__panel-{}']/p"

    SCOOTER_LOGO = (By.XPATH, "//img[@alt='Scooter']")
    YANDEX_LOGO = (By.XPATH, "//a[contains(@class, 'Header_LogoYandex')]")
    YANDEX_LOGO_BY_IMG = (By.XPATH, "//img[@alt='Yandex']/parent::a")
    YANDEX_LOGO_BY_HREF = (By.XPATH, "//a[contains(@href, 'yandex')]")
    YANDEX_LOGO_FALLBACK = (By.XPATH, "//div[contains(@class, 'Header')]//a[not(contains(@class, 'Header_LogoScooter'))]")

    COOKIE_ACCEPT_BUTTON = (By.XPATH, "//button[text()='да все привыкли']")