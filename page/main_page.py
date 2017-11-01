from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import visibility_of_element_located

from helpers.helper import wait_for_element

LOGOUT_BUTTON = (By.LINK_TEXT, 'Logout')


def get_logout_button_presence(driver):
    wait_for_element(LOGOUT_BUTTON, driver)
    return visibility_of_element_located(LOGOUT_BUTTON)
