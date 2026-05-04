from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:
    def __init__(self, browser):
        self.driver = browser

    def wait_for_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
    
    def wait_for_visible_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def scroll_to_element(self, element):
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});", element
        )
        self.driver.execute_script("window.scrollBy(0, 1);")

    def click_element(self, locator):
        element = self.wait_for_element(locator)
        self.scroll_to_element(element)
        ActionChains(self.driver).move_to_element(element).click().perform()

    def fill_input(self, locator, text):
        element = self.wait_for_visible_element(locator)
        self.scroll_to_element(element)
        element.clear()
        element.send_keys(text)

    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    def switch_to_new_tab(self, locator):
        self.click_element(locator)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        
