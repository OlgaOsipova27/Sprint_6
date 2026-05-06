import allure 

from page_objects.base_page import BasePage
from locators.main_page_locators import LocatorQuestionAnswer, LocatorHeadderButton
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class MainPage(BasePage):

    def __init__(self, driver):
        self.driver = driver
        self.locators = LocatorQuestionAnswer
        self.locators_headder = LocatorHeadderButton

    @allure.step('Нажимаем на вопрос для того, чтобы открыть область ответа')
    def open_answer_section(self, locator):
        self.wait_for_element(LocatorQuestionAnswer.HEAD_OF_QUESTIONS)
        self.click_element(locator)

    @allure.step('Ждем появления ответа')
    def wait_answer(self, locators):
        return self.wait_for_element(locators)
    
    @allure.step('Получаем текст ответа')
    def text_of_answer(self, locator):
        return self.find_element(locator).text
    
    @allure.step('Получаем URL страницы в новой вкладке, после нажатия на лого Яндекс')
    def url_after_click_on_Yandexlogo_new_tab(self):
        return self.get_url_new_tab(self.locators_headder.YANDEX_LOGO)

    @allure.step('Получаем URL страницы в той же вкладке, после нажатия на лого Самокат')
    def url_after_click_on_SCOOTERlogo_old_tab(self):
        return self.get_url_same_tab(self.locators_headder.SCOOTER_LOGO)
    
    