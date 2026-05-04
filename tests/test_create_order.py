import pytest
import allure 
import sys
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

ROOT_PATH = Path(__file__).parent.parent
sys.path.insert(0, str(ROOT_PATH))

from page_objects.base_page import BasePage
from locators.main_page_locators import LocatorOrderButtonMainPage
from locators.order_page_locators import LocatorOrderForms
from page_objects.order_page import CreateOrder
from fixture.order_data import ORDER_DATA
from fixture.url_data import URL_SCOOTER



class TestCreateOrderHeadderButton:

    def setup_class(cls):
        cls.driver = webdriver.Firefox()
        cls.wait = WebDriverWait(cls.driver, 10)

    @allure.title('Проверка, что после создания заказа появляется модальное окно с информацией об успешном заказе')
    @pytest.mark.parametrize("name, surname, address, station_name, phone_num, delivery_date, rental_period, color_name, comment_text", ORDER_DATA)
    def test_new_order_from_headder(self, name, surname, address, station_name, phone_num, delivery_date, rental_period, color_name, comment_text):

        self.driver.get(URL_SCOOTER)

        bp = BasePage(self.driver)

        bp.wait_for_element(LocatorOrderButtonMainPage.ORDER_BUTTON_ON_HEADDER)
        bp.click_element(LocatorOrderButtonMainPage.ORDER_BUTTON_ON_HEADDER)
        bp.wait_for_element(LocatorOrderForms.ORDER_HEADER_SCOOTER)


        order_page = CreateOrder(self.driver)
        order_page.fill_order_step_one(name, surname, address, station_name, phone_num)
        
        bp.click_element(LocatorOrderForms.BUTTON_NEXT)

        order_page.fill_order_step_two(delivery_date, rental_period, color_name, comment_text)

        bp.click_element(LocatorOrderForms.BUTTON_ORDER)
        bp.wait_for_visible_element(LocatorOrderForms.MODAL_WINDOW_APROVE)
        bp.click_element(LocatorOrderForms.BUTTON_YES_MODAL_WIN)
        bp.wait_for_element(LocatorOrderForms.ORDER_SUCCESS_HEADER)

        assert bp.find_element(LocatorOrderForms.ORDER_SUCCESS_HEADER).is_displayed()

    @allure.title('Проверка, что по нажатию на вторую кнопку "Заказать" открывается форма создания заказа')
    def test_click_on_second_order_button_open_create_order_form(self):

        self.driver.get(URL_SCOOTER)

        bp = BasePage(self.driver)

        bp.click_element(LocatorOrderButtonMainPage.ORDER_BUTTON_SECOND)
        bp.wait_for_element(LocatorOrderForms.ORDER_HEADER_SCOOTER)

        assert bp.find_element(LocatorOrderForms.ORDER_HEADER_SCOOTER).is_displayed()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

        


        






        