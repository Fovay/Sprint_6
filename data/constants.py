class Timeouts:  
    IMPLICIT_WAIT = 5
    EXPLICIT_WAIT = 10
    PAGE_LOAD_WAIT = 15
    SCRIPT_TIMEOUT = 30

class Browser: 
    WINDOW_WIDTH = 1920
    WINDOW_HEIGHT = 1080
    HEADLESS = False

class Messages:
    ORDER_SUCCESS = "Заказ оформлен"
    ORDER_CREATED = "Заказ создан успешно"
    COOKIE_ACCEPTED = "Cookie приняты"
    
    ERROR_ORDER_NOT_CREATED = "Заказ не был создан"
    ERROR_WRONG_URL = "Неверный URL"
    ERROR_ELEMENT_NOT_FOUND = "Элемент не найден"
    ERROR_WRONG_TEXT = "Текст не соответствует ожидаемому"

class Colors:  
    BLACK = "black"
    GREY = "grey"
    BOTH = "both"