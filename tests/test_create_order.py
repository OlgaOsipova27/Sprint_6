import pytest
import allure 
import sys
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

ROOT_PATH = Path(__file__).parent.parent
sys.path.insert(0, str(ROOT_PATH))
from page_objects.order_page import CreateOrder
from data.order_data import ORDER_DATA
from data.url_data import URL_SCOOTER



class TestCreateOrderHeadderButton:

    def setup_class(cls):
        cls.driver = webdriver.Firefox()
        cls.wait = WebDriverWait(cls.driver, 10)

    @allure.title('Проверка, что после создания заказа появляется модальное окно с информацией об успешном заказе')
    @pytest.mark.parametrize("name, surname, address, station_name, phone_num, delivery_date, rental_period, color_name, comment_text", ORDER_DATA)
    def test_new_order_from_headder(self, name, surname, address, station_name, phone_num, delivery_date, rental_period, color_name, comment_text):

        self.driver.get(URL_SCOOTER)

        order_page = CreateOrder(self.driver)

        order_page.open_order_page()
        order_page.fill_order_step_one(name, surname, address, station_name, phone_num)
        order_page.go_to_second_step()
        order_page.fill_order_step_two(delivery_date, rental_period, color_name, comment_text)
        order_page.approve_order()

        assert order_page.headder_of_success_create().is_displayed()

    @allure.title('Проверка, что по нажатию на вторую кнопку "Заказать" открывается форма создания заказа')
    def test_click_on_second_order_button_open_create_order_form(self):

        self.driver.get(URL_SCOOTER)

        order_page = CreateOrder(self.driver)

        order_page.open_order_page_with_second_button()

        assert order_page.headder_of_order_page().is_displayed()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

        


        






        