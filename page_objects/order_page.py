import allure 

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.order_page_locators import LocatorOrderForms
from locators.main_page_locators import LocatorOrderButtonMainPage
from selenium.webdriver.common.keys import Keys


from page_objects.base_page import BasePage

class CreateOrder(BasePage):

    def __init__(self, driver):
        self.driver = driver
        self.locators = LocatorOrderForms
        self.locators_button_order = LocatorOrderButtonMainPage

    @allure.step('Открываем страницу создания заказа')
    def open_order_page(self):

        self.wait_for_element(self.locators_button_order.ORDER_BUTTON_ON_HEADDER)
        self.click_element(self.locators_button_order.ORDER_BUTTON_ON_HEADDER)
        self.wait_for_element(self.locators.ORDER_HEADER_SCOOTER)
    
    @allure.step('Заполняем информацию о заказе (страница 1)')
    def fill_order_step_one(self, name, surname, address, station_name, phone_num):
        self.fill_input(self.locators.INPUT_NAME, name)
        self.fill_input(self.locators.INPUT_SURNAME, surname)
        self.fill_input(self.locators.INPUT_ADDRESS, address)
        self.click_element(self.locators.DROPDOWN_METROSTATION)
        self.click_element(self.locators.METRO_STATION_OPTION(station_name))
        self.fill_input(self.locators.INPUT_PHONE_NUMBER, phone_num)

    @allure.step('Нажимаем кнопку Далее для перехода на вторую страницу')
    def go_to_second_step(self):
        self.click_element(self.locators.BUTTON_NEXT)
        self.wait_for_element(self.locators.INPUT_DELIVERY_DATE)

    @allure.step('Выбираем дату в календаре')
    def select_delivery_date(self, date_value):
        element = self.wait_for_element(self.locators.INPUT_DELIVERY_DATE)
        element.send_keys(date_value)
        element.send_keys(Keys.ENTER)
    
    @allure.step('Выбиарем срок аренды')
    def select_rental_period(self, period_name):
        self.click_element(self.locators.DROPDOWN_RENTAL_PERIOD)
        self.wait_for_element(self.locators.RENTAL_PERIOD_OPTION(period_name))
        self.click_element(self.locators.RENTAL_PERIOD_OPTION(period_name))

    @allure.step('Выбиарем цвет самоката')
    def select_scooter_color(self, color_name):
        self.click_element(self.locators.COLOR_CHECKBOX(color_name))

    @allure.step('Добавляем комментарий для курьера')
    def fill_comment(self, comment_text):
        self.fill_input(self.locators.INPUT_COMMENT, comment_text)
 
    @allure.step('Заполняем информацию о заказе (страница 2)')
    def fill_order_step_two(self, delivery_date, rental_period, color_name, comment_text):
        self.select_delivery_date(delivery_date)
        self.select_rental_period(rental_period)
        self.select_scooter_color(color_name)
        self.fill_comment(comment_text)

    @allure.step('Подтверждаем создание заказа')
    def approve_order(self):

        self.click_element(self.locators.BUTTON_ORDER)
        self.wait_for_element(self.locators.MODAL_WINDOW_APROVE)
        self.click_element(self.locators.BUTTON_YES_MODAL_WIN)
        self.wait_for_element(self.locators.ORDER_SUCCESS_HEADER)

    @allure.step('Находим заголовок окна с информацией об успешном заказе')
    def headder_of_success_create(self):
        return self.find_element(self.locators.ORDER_SUCCESS_HEADER)

    @allure.step('Находим заголовок страницы создания заказа')
    def headder_of_order_page(self):
        return self.find_element(self.locators.ORDER_HEADER_SCOOTER)
    
    @allure.step('Открываем страницу создания заказа через вторую кнопку главной страницы')
    def open_order_page_with_second_button(self):
        self.click_element(self.locators_button_order.ORDER_BUTTON_SECOND)
        self.wait_for_element(self.locators.ORDER_HEADER_SCOOTER)