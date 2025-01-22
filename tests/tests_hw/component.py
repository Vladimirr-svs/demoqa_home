# component.py
from selenium.common.exceptions import NoSuchElementException

class Component:
    def __init__(self, driver, locator):
        self.driver = driver
        self.locator = locator

    def find_element(self):
        try:
            return self.driver.find_element(*self.locator)
        except NoSuchElementException:
            return None

    def get_text(self):
        element = self.find_element()
        return str(element.text) if element else ""

    def close_browser(self):
        self.driver.quit()
