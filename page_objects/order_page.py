from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.order_page_locators import LocatorOrderForms
from selenium.webdriver.common.keys import Keys


from page_objects.base_page import BasePage

class CreateOrder(BasePage):

    def __init__(self, driver):
        self.driver = driver
        self.locators = LocatorOrderForms
        self.wait = WebDriverWait(driver, 10)
    
    
    def fill_order_step_one(self, name, surname, address, station_name, phone_num):
        self.fill_input(LocatorOrderForms.INPUT_NAME, name)
        self.fill_input(LocatorOrderForms.INPUT_SURNAME, surname)
        self.fill_input(LocatorOrderForms.INPUT_ADDRESS, address)
        self.click_element(LocatorOrderForms.DROPDOWN_METROSTATION)
        self.click_element(LocatorOrderForms.METRO_STATION_OPTION(station_name))
        self.fill_input(LocatorOrderForms.INPUT_PHONE_NUMBER, phone_num)

   
    def go_to_second_step(self):
        self.click_element(self.locators.BUTTON_NEXT)
        self.wait_for_element(self.locators.INPUT_DELIVERY_DATE)

    def select_delivery_date(self, date_value):
        element = self.wait_for_element(self.locators.INPUT_DELIVERY_DATE)
        element.send_keys(date_value)
        element.send_keys(Keys.ENTER)
    
    def select_rental_period(self, period_name):
        self.click_element(self.locators.DROPDOWN_RENTAL_PERIOD)
        self.wait_for_element(self.locators.RENTAL_PERIOD_OPTION(period_name))
        self.click_element(self.locators.RENTAL_PERIOD_OPTION(period_name))


    def select_scooter_color(self, color_name):
        self.click_element(self.locators.COLOR_CHECKBOX(color_name))
 
    def fill_comment(self, comment_text):
        self.fill_input(self.locators.INPUT_COMMENT, comment_text)
 

    def fill_order_step_two(self, delivery_date, rental_period, color_name, comment_text):
        self.select_delivery_date(delivery_date)
        self.select_rental_period(rental_period)
        self.select_scooter_color(color_name)
        self.fill_comment(comment_text)
    