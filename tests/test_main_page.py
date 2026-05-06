import pytest
import allure
import sys
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

ROOT_PATH = Path(__file__).parent.parent
sys.path.insert(0, str(ROOT_PATH))

from page_objects.main_page import MainPage
from page_objects.order_page import CreateOrder
from data.faq_data import FAQ_DATA
from data.url_data import URL_SCOOTER, URL_DZEN
from locators.main_page_locators import LocatorHeadderButton, LocatorOrderButtonMainPage
from locators.order_page_locators import LocatorOrderForms


class TestMainPage:

    @classmethod
    def setup_class(cls):
        
        cls.driver = webdriver.Firefox()
        


    @allure.title('Проверка, что при нажатии на вопрос в разделе "Вопросы о важном" появляется соответствующий ответ')
    @pytest.mark.parametrize("question_loc, answer_loc, text_to_check", FAQ_DATA)
    def test_click_on_question_open_answers(self, question_loc, answer_loc, text_to_check):
        
        self.driver.get(URL_SCOOTER)

        main_page = MainPage(self.driver)
        

        main_page.open_answer_section(question_loc)
        answer_elem = main_page.wait_answer(answer_loc)
        text = main_page.text_of_answer(answer_loc)

        assert answer_elem.is_displayed()
        assert text == text_to_check


    @allure.title('Проверка, что при нажатии на логотип "Яндекс" открывается Яндекс.Дзен')
    def test_click_on_yandex_open_dzen(self):
        
        self.driver.get(URL_SCOOTER)
        main_page = MainPage(self.driver)
        
        url = main_page.url_after_click_on_Yandexlogo_new_tab()
 
        assert URL_DZEN == url


    @allure.title('Проверка, что при нажатии на логотип "Самокат" с неглавной страницы открывается главная страница Самокат')
    def test_click_on_scooter_open_main_page(self):
        
        self.driver.get(URL_SCOOTER)
        main_page = MainPage(self.driver)
        order_page = CreateOrder(self.driver)
       
        order_page.open_order_page()

        url = main_page.url_after_click_on_SCOOTERlogo_old_tab()

        assert URL_SCOOTER == url

        
    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
