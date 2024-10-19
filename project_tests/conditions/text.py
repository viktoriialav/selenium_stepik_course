from typing import Tuple

from selenium.common import StaleElementReferenceException
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.expected_conditions import WebDriverOrWebElement


def text_to_be_present_in_element_located_(locator: Tuple[str, str]):
    def _predicate(driver: WebDriverOrWebElement):
        try:
            element_text = driver.find_element(*locator).text
            return element_text
        except StaleElementReferenceException:
            return False

    return _predicate

def text_to_be_present_in_element_(element: WebElement):
    def _predicate(_):
        try:
            element_text = element.text
            return element_text
        except StaleElementReferenceException:
            return False

    return _predicate