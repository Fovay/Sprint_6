from selenium.webdriver.common.by import By

class OrderPageLocators:
    FIRST_NAME_INPUT = (By.XPATH, "//input[contains(@placeholder,'Имя')]")
    LAST_NAME_INPUT = (By.XPATH, "//input[contains(@placeholder,'Фамилия')]")
    ADDRESS_INPUT = (By.XPATH, "//input[contains(@placeholder,'Адрес')]")
    SUBWAY_FIELD = (By.XPATH, "//input[contains(@placeholder,'метро')]")
    TELEPHONE_NUMBER_FIELD = (By.XPATH, "//input[contains(@placeholder,'Телефон')]")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")
    BACK_BUTTON = (By.XPATH, "//button[text()='Назад']")

    DATE_FIELD = (By.XPATH, "//input[contains(@placeholder,'Когда')]")
    RENTAL_PERIOD_FIELD = (By.XPATH, "//span[@class='Dropdown-arrow']")
    RENTAL_PERIOD_LIST = (By.XPATH, "//div[@class='Dropdown-option']")
    COLOR_CHECKBOXES = (By.XPATH, "//div[contains(text(),'Цвет')]/parent::div//input")
    COMMENT_FOR_COURIER_FIELD = (By.XPATH, "//input[contains(@placeholder,'Комментарий для курьера')]")
    ORDER_BUTTON = (By.XPATH, "//button[text()='Назад']/parent::div/button[text()='Заказать']")
    ACCEPT_ORDER_BUTTON = (By.XPATH, "//button[text()='Да']")
    
    ORDER_COMPLETED_INFO = (By.XPATH, "//div[contains(@class, 'Order_ModalHeader')]")
    SHOW_STATUS_BUTTON = (By.XPATH, "//button[text()='Посмотреть статус']")

    @staticmethod
    def SUBWAY_HINT_BUTTON(subway_name: str):
        return (By.XPATH, f"//div[text()='{subway_name}']/parent::button")