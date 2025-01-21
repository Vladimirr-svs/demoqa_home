from pages.swag_labs import SwagLabs


def test_check_icon(browser):
    swag_labs_page = SwagLabs(browser)
    swag_labs_page.visit()
    assert swag_labs_page.exist_icon()

def test_check_username_field(browser):
    swag_labs_page = SwagLabs(browser)
    swag_labs_page.visit()
    username_field_locator = 'input#user-name'
    assert swag_labs_page.find_element(username_field_locator).is_displayed()


def test_check_password_field(browser):
    swag_labs_page = SwagLabs(browser)
    swag_labs_page.visit()
    password_field_locator = 'input#password'
    assert swag_labs_page.find_element(password_field_locator).is_displayed()