import json
import time
from operator import itemgetter

from selenium.common import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

import config
from project_tests.utils.path import abs_path_from_root


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
    max_expiry = 0
    link_max = None
    links = wait.until(lambda driver: driver.find_elements(By.CSS_SELECTOR, '.urls a'))
    for link in links:
        driver.get(link.get_attribute('href'))
        cookie = driver.get_cookies()
        expiry = cookie[0]['expiry']
        if max_expiry < expiry:
            max_expiry = expiry
            link_max = link
        driver.back()

    driver.get(link_max.get_attribute('href'))
    answer = wait.until(lambda driver: driver.find_element(By.CSS_SELECTOR, '#result')).text

    # THEN
    assert answer == '563244506345412334251234560541'


def test_code_name_operation_liberation_way(driver_management):
    # GIVEN
    driver = driver_management
    wait = WebDriverWait(driver=driver, timeout=2, ignored_exceptions=(WebDriverException,))
    driver.get(config.settings.base_url + '/scroll/4/index.html')

    # WHEN
    summ = 0
    buttons = wait.until(lambda driver: driver.find_elements(By.CSS_SELECTOR, '.btn'))
    for button in buttons:
        driver.execute_script("return arguments[0].scrollIntoView(true);", button)
        button.click()
        num = wait.until(lambda driver: driver.find_element(By.CSS_SELECTOR, '#result')).text
        summ += int(num)

    # THEN
    assert str(summ) == '4479945576993'


def test_numeric_prey_operation_checkbox_version_1(driver_management):
    # GIVEN
    driver = driver_management
    wait = WebDriverWait(driver=driver, timeout=2, ignored_exceptions=(WebDriverException,))
    driver.get(config.settings.base_url + '/selenium/5.5/3/1.html')

    # WHEN
    summ = 0
    text_areas = wait.until(lambda driver: driver.find_elements(By.CSS_SELECTOR, '.parent textarea'))
    for text_area in text_areas:
        num = text_area.text
        # checkbox = wait.until(lambda driver: driver.find_element(By.XPATH, f'//*[@class="parent"]/textarea[.="{num}"]/../input[@class="checkbox"]'))
        checkbox = text_area.find_element(By.XPATH, '../input[@class="checkbox"]')
        if checkbox.is_selected():
            summ += int(num)

    # THEN
    assert str(summ) == '25903'


def test_numeric_prey_operation_checkbox_version_2(driver_management):
    # GIVEN
    driver = driver_management
    wait = WebDriverWait(driver=driver, timeout=2, ignored_exceptions=(WebDriverException,))
    driver.get(config.settings.base_url + '/selenium/5.5/3/1.html')

    # WHEN
    summ = 0
    elems = wait.until(lambda driver: driver.find_elements(By.CSS_SELECTOR, '.parent'))
    for elem in elems:
        if elem.find_element(By.CSS_SELECTOR, '.checkbox').is_selected():
            num = elem.find_element(By.CSS_SELECTOR, 'textarea').text
            summ += int(num)

    # THEN
    assert str(summ) == '25903'


def test_operation_colour_synchronization(driver_management):
    # GIVEN
    driver = driver_management
    wait = WebDriverWait(driver=driver, timeout=2, ignored_exceptions=(WebDriverException,))
    driver.get(config.settings.base_url + '/selenium/5.5/4/1.html')

    # WHEN
    summ = 0
    elems = wait.until(lambda driver: driver.find_elements(By.CSS_SELECTOR, '.parent'))

    for elem in elems:
        num = elem.find_element(By.CSS_SELECTOR, 'textarea[color="gray"]').text
        elem.find_element(By.CSS_SELECTOR, 'textarea[color="gray"]').clear()
        elem.find_element(By.CSS_SELECTOR, 'textarea[color="blue"]').send_keys(num)
        elem.find_element(By.CSS_SELECTOR, 'button').click()

    driver.find_element(By.CSS_SELECTOR, '#checkAll').click()
    answer = wait.until(lambda driver: driver.find_element(By.CSS_SELECTOR, '#congrats')).text

    # THEN
    assert answer == 'FGFF-D546-DF31-34SQ-4346-93PF'


def test_quest_hell_of_colour_codes(driver_management):
    # GIVEN
    driver = driver_management
    wait = WebDriverWait(driver=driver, timeout=2, ignored_exceptions=(WebDriverException,))
    driver.get(config.settings.base_url + '/selenium/5.5/5/1.html')

    # WHEN
    colours = wait.until(lambda driver: driver.find_elements(By.CSS_SELECTOR, '#main-container>div'))

    for colour in colours:
        name = colour.find_element(By.CSS_SELECTOR, 'span').text
        colour.find_element(By.CSS_SELECTOR, f'select').click()
        colour.find_element(By.CSS_SELECTOR, f'option[value="{name}"]').click()
        colour.find_element(By.CSS_SELECTOR, f'button[data-hex="{name}"]').click()
        colour.find_element(By.CSS_SELECTOR, '[type="checkbox"]').click()
        colour.find_element(By.CSS_SELECTOR, '[type="text"]').send_keys(name)
        colour.find_element(By.XPATH, '//button[.="Проверить"]').click()

    wait.until(lambda driver: driver.find_element(By.XPATH, '//button[.="Проверить все элементы"]')).click()
    alert = wait.until(lambda driver: driver.switch_to.alert)
    alert_text = alert.text
    alert.accept()

    # THEN
    assert alert_text == '532344023354423035345134503454510'


def test_code_name_secret_cookies(driver_management):
    # GIVEN
    driver = driver_management
    wait = WebDriverWait(driver=driver, timeout=2, ignored_exceptions=(WebDriverException,))
    driver.get(config.settings.base_url + '/methods/3/index.html')

    # WHEN
    summ = 0
    cookies = driver.get_cookies()
    for cookie in cookies:
        name = cookie['name']
        if name.startswith('secret_cookie_'):
            summ += int(cookie['value'])

    # THEN
    assert str(summ) == '4901217'


def test_code_name_operation_junior_virtuoso(driver_management):
    # GIVEN
    driver = driver_management
    wait = WebDriverWait(driver=driver, timeout=5, ignored_exceptions=(WebDriverException,))
    driver.get(config.settings.base_url + '/selenium/5.6/1/index.html')

    # WHEN
    with open(abs_path_from_root('resources/data.json'), encoding='utf-8') as file:
        data = json.load(file)

    temp = []
    for elem in data:
        driver.delete_all_cookies()
        driver.add_cookie({'name': f'{elem['name']}', 'value': f'{elem['value']}'})
        driver.refresh()

        skills = wait.until(lambda driver: driver.find_elements(By.CSS_SELECTOR, '#skillsList>li'))
        num_skills = len(skills)

        age = wait.until(lambda driver: driver.find_element(By.CSS_SELECTOR, '#age')).text
        age = -int(age.split()[-1])

        temp.append((elem['value'], age, num_skills))

    sorted_list = sorted(temp, key=itemgetter(1, 2))
    answer = sorted_list[-1][0]

    # THEN
    assert answer == 'ibyAZPfXAsPqptPaNyL'