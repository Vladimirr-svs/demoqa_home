from selenium import webdriver
from selenium.webdriver.common.by import By
from component import Component

def test_check_footer_text():
    driver = webdriver.Chrome()
    driver.get('https://demoqa.com/')

    footer = Component(driver, (By.XPATH, "//footer[@id='app']//span"))
    assert footer.get_text() == '© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED.'

    driver.quit()

def test_check_center_text():
    driver = webdriver.Chrome()
    driver.get('https://demoqa.com/')

    elements_button = Component(driver, (By.XPATH, "//h5[text()='Elements']"))
    elements_button.find_element().click()

    center_text = Component(driver, (By.XPATH, "//div[@class='col-12 mt-4 col-md-6']/div"))
    assert center_text.get_text() == 'Please select an item from left to start practice.'

    driver.quit()
