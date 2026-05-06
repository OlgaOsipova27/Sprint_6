from selenium.webdriver.common.by import By

class LocatorOrderForms:

    #1 page

        ORDER_HEADER_SCOOTER = (By.XPATH,"//div[text()='Для кого самокат']")
        INPUT_NAME = (By.XPATH, "//input[@placeholder = '* Имя']")
        INPUT_SURNAME = (By.XPATH, "//input[@placeholder = '* Фамилия']")
        INPUT_ADDRESS = (By.XPATH, "//input[@placeholder = '* Адрес: куда привезти заказ']")
        DROPDOWN_METROSTATION = (By.XPATH, "//input[@placeholder = '* Станция метро']")
        METRO_STATION_OPTION = lambda station_name: (By.XPATH, f"//button[contains(@class,'select-search__option') and .//div[normalize-space()='{station_name}']]")
        INPUT_PHONE_NUMBER = (By.XPATH, "//input[@placeholder = '* Телефон: на него позвонит курьер']")
        BUTTON_NEXT = (By.XPATH, "//button[text()='Далее']")

    #2 page

        INPUT_DELIVERY_DATE = (By.XPATH, "//input[@placeholder = '* Когда привезти самокат']")
        DROPDOWN_RENTAL_PERIOD = (By.XPATH, "//div[text()='* Срок аренды']")
        RENTAL_PERIOD_OPTION = lambda period_name: (By.XPATH, f"//div[contains(@class,'Dropdown-option') and normalize-space()='{period_name}']")
        COLOR_CHECKBOX = lambda color_id: (By.XPATH, f"//label[@for='{color_id}']")

        INPUT_COMMENT = (By.CSS_SELECTOR, "input[placeholder='Комментарий для курьера']")

        BUTTON_ORDER = (By.XPATH, "(//button[text()='Заказать'])[2]")

        MODAL_WINDOW_APROVE = (By.XPATH, "//div[contains(@class,'Order_Modal') and .//div[contains(text(),'Хотите оформить заказ?')]]")
        BUTTON_YES_MODAL_WIN = (By.XPATH, "//button[text()='Да']")
        ORDER_SUCCESS_HEADER = (By.XPATH, "//div[text()='Заказ оформлен']")

