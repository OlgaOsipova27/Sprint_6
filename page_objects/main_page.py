from page_objects.base_page import BasePage
from locators.main_page_locators import LocatorQuestionAnswer
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class MainPage(BasePage):

    def __init__(self, browser):
        super().__init__(browser)

    def open_answer_section(self, locator):
        self.wait_for_element(LocatorQuestionAnswer.HEAD_OF_QUESTIONS)
        self.click_element(locator)

    def text_of_answer(self, locator):
        return self.find_element(locator).text
    
    def url_after_click_on_logo_new_tab(self, locator):

        old_tabs = len(self.driver.window_handles)
        self.click_element(locator)
        WebDriverWait(self.driver, 10).until(lambda d: len(d.window_handles) > old_tabs)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        WebDriverWait(self.driver, 10).until(lambda d: d.current_url != "about:blank")
        return self.driver.current_url

    def url_after_click_on_logo_old_tab(self, locator):

        old_url = self.driver.current_url
        self.click_element(locator)
        WebDriverWait(self.driver, 10).until(EC.url_changes(old_url))
        return self.driver.current_url