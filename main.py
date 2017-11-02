import unittest
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities

from helpers import helper
from page import main_page


class TestLogin(unittest.TestCase):
    def setUp(self):
        firefox_capabilities = DesiredCapabilities.FIREFOX
        firefox_capabilities['marionette'] = True
        firefox_capabilities['binary'] = 'geckodriver'
        self.driver = webdriver.Firefox(capabilities=firefox_capabilities)

    def test_login(self):
        main = main_page.MainPage(self.driver)

        helper.authenticate(self.driver)

        self.assertTrue(main.get_logout_button_presence(self.driver))

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
