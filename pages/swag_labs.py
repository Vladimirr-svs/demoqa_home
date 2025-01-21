from selenium.common.exceptions import NoSuchElementException
from pages.base_page import BasePage

class SwagLabs(BasePage):
    def exist_icon(self):
        locator = 'div.login_logo'
        try:
            self.find_element(locator)
        except NoSuchElementException:
            return False
        return True