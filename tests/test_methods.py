from selenium.common import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

import config


def test_hunting_for_hidden_treasures(driver_management):
    # GIVEN
    driver = driver_management
    wait = WebDriverWait(driver=driver, timeout=2, ignored_exceptions=(WebDriverException,))
    driver.get(config.settings.base_url + '/methods/1/index.html')

    # WHEN
    result = 'random'
    while not result.isdigit():
        result = wait.until(lambda driver: driver.find_element(By.CSS_SELECTOR, '#result')).text
        driver.refresh()

    # THEN
    assert result == '4168138981270992'

def test_operation_clean_sheet(driver_management):
    # GIVEN
    driver = driver_management
    wait = WebDriverWait(driver=driver, timeout=2, ignored_exceptions=(WebDriverException,))
    driver.get(config.settings.base_url + '/selenium/5.5/1/1.html')

    # WHEN
    fields = wait.until(lambda driver: driver.find_elements(By.CSS_SELECTOR, '.text-field'))
    for field in fields:
        field.clear()

    wait.until(lambda driver: driver.find_element(By.CSS_SELECTOR, '#checkButton')).click()
    alert_text = wait.until(lambda driver: driver.switch_to.alert).text

    # THEN
    assert alert_text == '6540634355436603541756586467083'


def test_code_name_pathfinder_of_even_numbered_cookies(driver_management):
    # GIVEN
    driver = driver_management
    wait = WebDriverWait(driver=driver, timeout=2, ignored_exceptions=(WebDriverException,))
    driver.get(config.settings.base_url + '/methods/3/index.html')

    # WHEN
    summ = 0
    cookies = driver.get_cookies()
    for cookie in cookies:
        num = int(cookie['name'].split('_')[-1])
        if num % 2 == 0:
            summ += int(cookie['value'])

    # THEN
    assert str(summ) == '1962101'


def test_operation_mine_field(driver_management):
    # GIVEN
    driver = driver_management
    wait = WebDriverWait(driver=driver, timeout=2, ignored_exceptions=(WebDriverException,))
    driver.get(config.settings.base_url + '/selenium/5.5/2/1.html')

    # WHEN
    fields = wait.until(lambda driver: driver.find_elements(By.CSS_SELECTOR, '.text-field[data-enabled="true"]'))
    for field in fields:
        field.clear()

    wait.until(lambda driver: driver.find_element(By.CSS_SELECTOR, '#checkButton')).click()
    alert_text = wait.until(lambda driver: driver.switch_to.alert).text

    # THEN
    assert alert_text == '534645033455443650615463625441067356407'


def test_code_name_operation_immortal_cookies(driver_management):
    # GIVEN
    driver = driver_management
    wait = WebDriverWait(driver=driver, timeout=2, ignored_exceptions=(WebDriverException,))
    driver.get(config.settings.base_url + '/methods/5/index.html')

    # WHEN
    summ = 0
    cookies = driver.get_cookies()
    for cookie in cookies:
        num = int(cookie['name'].split('_')[-1])
        if num % 2 == 0:
            summ += int(cookie['value'])

    # THEN
    assert str(summ) == '1962101'