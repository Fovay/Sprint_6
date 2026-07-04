class Timeouts:  
    implicit_wait = 5
    explicit_wait = 10
    page_load_wait = 15
    script_timeout = 30

class Browser: 
    window_width = 1920
    window_height = 1080
    headless = False

class Messages:
    order_success = "Заказ оформлен"
    order_created = "Заказ создан успешно"
    cookie_accepted = "Cookie приняты"
    
    error_order_not_created = "Заказ не был создан"
    error_wrong_url = "Неверный URL"
    error_element_not_found = "Элемент не найден"
    error_wrong_text = "Текст не соответствует ожидаемому"

class Colors:  
    black = "black"
    grey = "grey"
    both = "both"