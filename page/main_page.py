from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import visibility_of_element_located

from helpers.helper import wait_for_element


class MainPage:
    __LOGOUT_BUTTON = (By.LINK_TEXT, 'Logout')

    def __init__(self, driver):
        self.__driver = driver

    def get_logout_button_presence(self, __driver):
        wait_for_element(self.__LOGOUT_BUTTON, self.__driver)
        return visibility_of_element_located(self.__LOGOUT_BUTTON)
