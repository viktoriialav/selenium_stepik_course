from selenium.common import WebDriverException
from selenium.webdriver import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

import config


def test_numbers_search(driver_management):
    # GIVEN
    driver = driver_management
    wait = WebDriverWait(driver=driver, timeout=2.0, ignored_exceptions=(WebDriverException,))
    driver.get(config.settings.base_url + '/scroll/2/index.html')

    # WHEN
    summ = 0
    elems = wait.until(lambda driver: driver.find_elements(By.CSS_SELECTOR, '.item'))

    for elem in elems:
        elem.find_element(By.CSS_SELECTOR, '.checkbox_class').click()
        text = elem.find_element(By.CSS_SELECTOR, 'span').text
        if text:
            summ += int(text)

    # THEN
    assert str(summ) == '13310'


def test_infinite_scroll_1(driver_management):
    # GIVEN
    driver = driver_management
    wait = WebDriverWait(driver=driver, timeout=2.0, ignored_exceptions=(WebDriverException,))
    driver.get(config.settings.base_url + '/infiniti_scroll_1/')

    # WHEN
    summ = 0
    input_list = []
    flag = True

    while flag:
        elems = wait.until(
            lambda driver: driver.find_elements(By.CSS_SELECTOR, '#scroll-container [id^="__InfiScroll_"]'))

        for elem in elems:
            if elem not in input_list:
                driver.execute_script("return arguments[0].scrollIntoView(true);", elem)
                input_list.append(elem)
                text = elem.text
                if text:
                    summ += int(text)
                if elem.get_attribute('class') == 'last-of-list':
                    flag = False

    # THEN
    assert str(summ) == '86049950'


def test_infinite_scroll_2(driver_management):
    # GIVEN
    driver = driver_management
    wait = WebDriverWait(driver=driver, timeout=2.0, ignored_exceptions=(WebDriverException,))
    driver.get(config.settings.base_url + '/infiniti_scroll_1/')

    # WHEN
    summ = 0
    input_list = []
    flag = True

    while flag:
        elems = wait.until(
            lambda driver: driver.find_elements(By.CSS_SELECTOR, '#scroll-container [id^="__InfiScroll_"]'))

        for elem in elems:
            if elem not in input_list:
                elem.find_element(By.CSS_SELECTOR, 'input').send_keys(Keys.DOWN)
                input_list.append(elem)
                text = elem.text
                if text:
                    summ += int(text)
                if elem.get_attribute('class') == 'last-of-list':
                    flag = False

    # THEN
    assert str(summ) == '86049950'


def test_treasure_hunt_among_hidden_items(driver_management):
    # GIVEN
    driver = driver_management
    wait = WebDriverWait(driver=driver, timeout=2.0, ignored_exceptions=(WebDriverException,))
    driver.get(config.settings.base_url + '/infiniti_scroll_2/')

    # WHEN
    class_attr = False
    container = driver.find_element(By.CSS_SELECTOR, '#scroll-container')
    scroll_origin = ScrollOrigin.from_element(container)

    while not class_attr:
        ActionChains(driver).scroll_from_origin(scroll_origin, 1, 400).perform()
        wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, 'spinner')))
        class_attr = sum(elem.get_attribute('class') == 'last-of-list' for elem in
                         driver.find_elements(By.CSS_SELECTOR, '#scroll-container p'))

    summ = sum(int(elem.text) for elem in driver.find_elements(By.CSS_SELECTOR, '#scroll-container p') if elem.text)

    # THEN
    assert str(summ) == '499917600'


def test_simultaneous_deep_scrolling(driver_management):
    # GIVEN
    driver = driver_management
    wait = WebDriverWait(driver=driver, timeout=2.0, ignored_exceptions=(WebDriverException,))
    driver.get(config.settings.base_url + '/infiniti_scroll_3/')

    # WHEN
    summ = 0

    for i in range(1, 6):
        class_attr = False
        container = wait.until(lambda driver: driver.find_element(By.CSS_SELECTOR, f'#scroll-container_{i}'))
        scroll_origin = ScrollOrigin.from_element(container)

        while not class_attr:
            ActionChains(driver).scroll_from_origin(scroll_origin, delta_x=0, delta_y=500).perform()
            class_attr = sum(elem.get_attribute('class') == 'last-of-list' for elem in
                             wait.until(
                                 lambda driver: driver.find_elements(By.CSS_SELECTOR, f'#scroll-container_{i} span')))

        summ += sum(int(elem.text) for elem in driver.find_elements(By.CSS_SELECTOR, f'#scroll-container_{i} span') if
                    elem.text)

    print(summ)

    # THEN
    assert str(summ) == '159858750'


def test_code_name_space_cleaning_of_uranium(driver_management):
    # GIVEN
    driver = driver_management
    wait = WebDriverWait(driver=driver, timeout=2.0, ignored_exceptions=(WebDriverException,))
    driver.get(config.settings.base_url + '/selenium/5.7/1/index.html')

    # WHEN
    height = driver.execute_script('return document.body.scrollHeight')
    driver.execute_script(f'window.scrollTo(0, {height});')
    buttons = wait.until(lambda driver: driver.find_elements(By.CSS_SELECTOR, 'button.clickMe'))

    for button in buttons:
        driver.execute_script('return arguments[0].scrollIntoView(true);', button)
        button.click()

    text = driver.switch_to.alert.text

    # THEN
    assert text == 'JKf9-034D-DE02-PB2G-QB8Z-81VN-30GK-IO90-UT89'


def test_operation_green_lotus(driver_management):
    # GIVEN
    driver = driver_management
    wait = WebDriverWait(driver=driver, timeout=2.0, ignored_exceptions=(WebDriverException,))
    driver.get(config.settings.base_url + '/selenium/5.7/5/index.html')

    # WHEN
    buttons = wait.until(lambda driver: driver.find_elements(By.CSS_SELECTOR, '.timer_button'))

    for button in buttons:
        time = button.get_attribute('value')
        ActionChains(driver).click_and_hold(button).pause(float(time)).release(button).perform()

    text = driver.switch_to.alert.text

    # THEN
    assert text == 'GFL4-ED40-F32F-HJ24-0BXS-235N-PIRE-123VD-123F'


def test_even_choice_endless_checkbox_list_1(driver_management):
    # GIVEN
    driver = driver_management
    wait = WebDriverWait(driver=driver, timeout=2.0, ignored_exceptions=(WebDriverException,))
    driver.get(config.settings.base_url + '/selenium/5.7/4/index.html')

    # WHEN
    container = driver.find_element(By.CSS_SELECTOR, '#main_container')
    scroll_origin = ScrollOrigin.from_element(container)

    for _ in range(20):
        ActionChains(driver).scroll_from_origin(scroll_origin, delta_x=0, delta_y=500).perform()

    checkboxes = wait.until(lambda driver: driver.find_elements(By.CSS_SELECTOR, '.child_container'))

    for checkbox in checkboxes:
        for child in checkbox.find_elements(By.CSS_SELECTOR, 'input'):
            if not int(child.get_attribute('value')) % 2:
                child.click()

    wait.until(lambda driver: driver.find_element(By.CSS_SELECTOR, '.alert_button')).click()
    text = driver.switch_to.alert.text

    # THEN
    assert text == '5402f04236450f263540jk406504l506'
