import math
from itertools import product

from selenium.common import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

import config
from project_tests.utils.window import size_increment, next_tab


def test_search_for_secret_code_1(driver_management):
    # GIVEN
    driver = driver_management
    wait = WebDriverWait(driver=driver, timeout=2.0, ignored_exceptions=(WebDriverException,))
    driver.get(config.settings.base_url + '/selenium/5.8/1/index.html')

    # WHEN
    result = wait.until(lambda driver: driver.find_element(By.CSS_SELECTOR, '#result'))

    for i in range(1, 101):
        button = wait.until(lambda driver: driver.find_element(By.CSS_SELECTOR, f'.buttons[onclick="clickNumber({i})"]'))
        button.click()
        driver.switch_to.alert.accept()
        if result.text:
            break

    # THEN
    assert result.text == '321968541687435564865796413874'


def test_search_for_secret_code(driver_management):
    # GIVEN
    driver = driver_management
    wait = WebDriverWait(driver=driver, timeout=2.0, ignored_exceptions=(WebDriverException,))
    driver.get(config.settings.base_url + '/selenium/5.8/1/index.html')

    # WHEN
    result = wait.until(lambda driver: driver.find_element(By.CSS_SELECTOR, '#result'))
    buttons = wait.until(lambda driver: driver.find_elements(By.CSS_SELECTOR, '.buttons'))

    for button in buttons:
        button.click()
        driver.switch_to.alert.accept()
        if result.text:
            break

    # THEN
    assert result.text == '321968541687435564865796413874'


def test_search_for_secret_pin_codes(driver_management):
    # GIVEN
    driver = driver_management
    wait = WebDriverWait(driver=driver, timeout=2.0, ignored_exceptions=(WebDriverException,))
    driver.get(config.settings.base_url + '/selenium/5.8/2/index.html')

    # WHEN
    result = wait.until(lambda driver: driver.find_element(By.CSS_SELECTOR, '#result'))
    input_field = wait.until(lambda driver: driver.find_element(By.CSS_SELECTOR, '#input'))
    button_check = wait.until(lambda driver: driver.find_element(By.CSS_SELECTOR, '#check'))

    for i in range(1, 101):
        button = wait.until(lambda driver: driver.find_element(By.CSS_SELECTOR, f'.buttons[value="{i}"]'))
        button.click()

        alert = driver.switch_to.alert
        text = alert.text
        alert.accept()

        input_field.clear()
        input_field.send_keys(text)
        button_check.click()

        if result.text and  result.text != 'Неверный пин-код':
            break

    # THEN
    assert result.text == '867413857416874163897546183542'

def test_search_for_secret_pin_codes_2(driver_management):
    # GIVEN
    driver = driver_management
    wait = WebDriverWait(driver=driver, timeout=2.0, ignored_exceptions=(WebDriverException,))
    driver.get(config.settings.base_url + '/selenium/5.8/2/index.html')

    # WHEN
    answer = ''
    for button in driver.find_elements(By.CSS_SELECTOR, '.buttons'):
        button.click()

        alert = driver.switch_to.alert
        text = alert.text
        alert.accept()

        input_field = wait.until(lambda driver: driver.find_element(By.CSS_SELECTOR, '#input'))
        input_field.clear()
        input_field.send_keys(text)
        wait.until(lambda driver: driver.find_element(By.CSS_SELECTOR, '#check')).click()

        result = wait.until(lambda driver: driver.find_element(By.CSS_SELECTOR, '#result'))
        if result.text and  result.text != 'Неверный пин-код':
            answer = result.text
            break

    # THEN
    assert answer == '867413857416874163897546183542'


def test_secret_code_cyber_investigation(driver_management):
    # GIVEN
    driver = driver_management
    wait = WebDriverWait(driver=driver, timeout=2.0, ignored_exceptions=(WebDriverException,))
    driver.get(config.settings.base_url + '/selenium/5.8/3/index.html')

    # WHEN
    answer = ''
    for btn in wait.until(lambda driver: driver.find_elements(By.CSS_SELECTOR,'.pin')):
        pin = btn.text
        wait.until(lambda driver: driver.find_element(By.CSS_SELECTOR, '#check')).click()
        alert = driver.switch_to.alert
        alert.send_keys(pin)
        alert.accept()

        result = wait.until(lambda driver: driver.find_element(By.CSS_SELECTOR, '#result'))
        if result.text and result.text != 'Неверный пин-код':
            answer = result.text
            break

    # THEN
    assert answer =='1261851212132345456274632'


def test_browser_viewport_configuration(driver_management):
    # GIVEN
    driver = driver_management
    wait = WebDriverWait(driver=driver, timeout=2.0, ignored_exceptions=(WebDriverException,))
    driver.get(config.settings.base_url + '/window_size/1/')
    in_new_width = in_new_height = 555

    # WHEN
    d_width, d_height = size_increment(driver)
    driver.set_window_size(width=(in_new_width + d_width),height=(in_new_height + d_height))

    result = wait.until(lambda driver: driver.find_element(By.CSS_SELECTOR, '#result')).text

    # THEN
    assert result == '1684163857416385746374'


def test_search_of_secret_window_size_combination(driver_management):
    # GIVEN
    driver = driver_management
    wait = WebDriverWait(driver=driver, timeout=5.0, ignored_exceptions=(WebDriverException,))
    driver.get(config.settings.base_url + '/window_size/2/index.html')
    window_size_x = [616, 648, 680, 701, 730, 750, 805, 820, 855, 890, 955, 1000]
    window_size_y = [300, 330, 340, 388, 400, 421, 474, 505, 557, 600, 653, 1000]

    # WHEN
    d_width, d_height = size_increment(driver)

    for width, height in product(window_size_x, window_size_y):
        driver.set_window_size(width=(width + d_width), height=(height + d_height))
        result = wait.until(lambda driver: driver.find_element(By.CSS_SELECTOR, '#result'))
        if result.text:
            break

    # THEN
    assert result.text == '9874163854135461654'


def test_mysterious_window_size(driver_management):
    # GIVEN
    driver = driver_management
    wait = WebDriverWait(driver=driver, timeout=2.0, ignored_exceptions=(WebDriverException,))
    driver.get(config.settings.base_url + '/window_size/2/index.html')
    window_size_x = [516, 648, 680, 701, 730, 750, 805, 820, 855, 890, 955, 1000]
    window_size_y = [270, 300, 340, 388, 400, 421, 474, 505, 557, 600, 653, 1000]

    # WHEN
    d_width, d_height = size_increment(driver)

    for width, height in product(window_size_x, window_size_y):
        driver.set_window_size(width=(width + d_width), height=(height + d_height))
        result = wait.until(lambda driver: driver.find_element(By.CSS_SELECTOR, '#result'))
        if result.text and result.text.isdigit():
            break

    # THEN
    assert width == 955 and height == 600


def test_hunter_of_mysterious_numbers_1(driver_management):
    # GIVEN
    driver = driver_management
    wait = WebDriverWait(driver=driver, timeout=5.0, ignored_exceptions=(WebDriverException,))
    driver.get(config.settings.base_url + '/blank/3/index.html')

    # WHEN
    original_tab = driver.current_window_handle
    summ = 0

    for button in wait.until(lambda driver: driver.find_elements(By.CSS_SELECTOR, '.buttons')):
        button.click()
        driver.switch_to.window(next_tab(driver))
        if driver.title.isdigit():
            summ += int(driver.title)
        driver.close()
        driver.switch_to.window(original_tab)

    # THEN
    assert str(summ) == '77725787998028643152187739088279'


def test_hunter_of_mysterious_numbers_2(driver_management):
    # GIVEN
    driver = driver_management
    wait = WebDriverWait(driver=driver, timeout=5.0, ignored_exceptions=(WebDriverException,))
    driver.get(config.settings.base_url + '/blank/3/index.html')

    # WHEN
    summ = 0

    for button in wait.until(lambda driver: driver.find_elements(By.CSS_SELECTOR, '.buttons')):
        button.click()

    all_tabs = driver.window_handles

    for tab in all_tabs:
        driver.switch_to.window(tab)
        if driver.title.isdigit():
            summ += int(driver.title)

    # THEN
    assert str(summ) == '77725787998028643152187739088279'


def test_discover_internet_threasures_1(driver_management):
    # GIVEN
    driver = driver_management
    wait = WebDriverWait(driver=driver, timeout=2.0, ignored_exceptions=(WebDriverException,))
    sites = ['http://parsinger.ru/blank/1/1.html',
             'http://parsinger.ru/blank/1/2.html',
             'http://parsinger.ru/blank/1/3.html',
             'http://parsinger.ru/blank/1/4.html',
             'http://parsinger.ru/blank/1/5.html',
             'http://parsinger.ru/blank/1/6.html', ]

    # WHEN
    summ = 0
    driver.get(sites[0])
    for i in range(1, len(sites)):
        driver.switch_to.new_window()
        driver.get(sites[i])

    import time
    time.sleep(2)

    for window_handle in driver.window_handles:
        driver.switch_to.window(window_handle)
        wait.until(lambda driver: driver.find_element(By.CSS_SELECTOR, '.checkbox_class')).click()
        text = wait.until(lambda driver: driver.find_element(By.CSS_SELECTOR, '#result')).text
        summ += math.sqrt(int(text))

    # THEN
    assert str(round(summ, 9)) == '334703.720482347'


def test_discover_internet_threasures(driver_management):
    # GIVEN
    driver = driver_management
    wait = WebDriverWait(driver=driver, timeout=2.0, ignored_exceptions=(WebDriverException,))
    sites = ['http://parsinger.ru/blank/1/1.html',
             'http://parsinger.ru/blank/1/2.html',
             'http://parsinger.ru/blank/1/3.html',
             'http://parsinger.ru/blank/1/4.html',
             'http://parsinger.ru/blank/1/5.html',
             'http://parsinger.ru/blank/1/6.html', ]

    # WHEN
    summ = 0

    for i in range(0, len(sites)):
        driver.execute_script(f'window.open("{sites[i]}", "_blank{i+1}");')
    driver.close()

    import time
    time.sleep(2)

    for window_handle in driver.window_handles:
        driver.switch_to.window(window_handle)
        wait.until(lambda driver: driver.find_element(By.CSS_SELECTOR, '.checkbox_class')).click()
        text = wait.until(lambda driver: driver.find_element(By.CSS_SELECTOR, '#result')).text
        summ += math.sqrt(int(text))

    # THEN
    assert str(round(summ, 9)) == '334703.720482347'


def test_immersion_in_frames(driver_management):
    # GIVEN
    driver = driver_management
    wait = WebDriverWait(driver=driver, timeout=2.0, ignored_exceptions=(WebDriverException,))
    driver.get(config.settings.base_url + '/selenium/5.8/5/index.html')

    # WHEN
    answer = ''
    input_field = driver.find_element(By.CSS_SELECTOR, '#guessInput')

    for i in range(1, 10):
        frame = wait.until(lambda driver: driver.find_element(By.CSS_SELECTOR, f'#iframe{i}'))
        driver.switch_to.frame(frame)
        wait.until(lambda driver: driver.find_element(By.CSS_SELECTOR, 'button[onclick="showNumber()"]')).click()
        text = wait.until(lambda driver: driver.find_element(By.CSS_SELECTOR, '#numberDisplay')).text
        driver.switch_to.default_content()

        input_field.send_keys(text)
        driver.find_element(By.CSS_SELECTOR, '#checkBtn').click()
        try:
            answer = driver.switch_to.alert.text
            break
        except:
            input_field.clear()

    # THEN
    assert answer == 'FD79-32DJ-79XB-124S-P3DX-2456-DFB-DSA9'