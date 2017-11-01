from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from constants import auth_constants, tech_constants


def authenticate(driver):
    driver.get("https://" +
               auth_constants.LOGIN +
               ":" +
               auth_constants.PASSWORD +
               "@" +
               "auth-demo.aerobatic.io/protected-standard/")


def wait_for_element(locator, driver, time=tech_constants.TIMEOUT):
    wait = WebDriverWait(driver, time)
    wait.until(expected_conditions.visibility_of_element_located((locator[0], locator[1])))
