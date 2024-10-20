from selenium.common import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

import config
from project_tests.conditions.text import text_to_be_present_in_element_, text_to_be_present_in_element_located_


def test_wait_title(driver_management):
    # GIVEN
    driver = driver_management
    wait_1 = WebDriverWait(driver=driver, timeout=5.0, poll_frequency=0.25, ignored_exceptions=(WebDriverException,))
    wait_2 = WebDriverWait(driver=driver, timeout=30.0, poll_frequency=0.1, ignored_exceptions=(WebDriverException,))
    driver.get(config.settings.base_url + '/expectations/3/index.html')
    necessary_title = '345FDG3245SFD'

    # WHEN
    wait_1.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#btn'))).click()

    if wait_2.until(EC.title_is(necessary_title)):
        answer = driver.find_element(By.CSS_SELECTOR, '#result').text

    # THEN
    assert answer == '82934401788.40141'


def test_secret_title(driver_management):
    # GIVEN
    driver = driver_management
    wait_1 = WebDriverWait(driver=driver, timeout=5.0, poll_frequency=0.25, ignored_exceptions=(WebDriverException,))
    wait_2 = WebDriverWait(driver=driver, timeout=30.0, poll_frequency=0.1, ignored_exceptions=(WebDriverException,))
    driver.get(config.settings.base_url + '/expectations/4/index.html')
    necessary_sentence = 'JK8HQ'

    # WHEN
    wait_1.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#btn'))).click()

    if wait_2.until(EC.title_contains(necessary_sentence)):
        answer = driver.title

    # THEN
    assert answer == '33GBK-98C3X-K8PKB-JK8HQ-DMXMQ'


def test_momentary_tags(driver_management):
    # GIVEN
    driver = driver_management
    wait_1 = WebDriverWait(driver=driver, timeout=5.0, poll_frequency=0.25, ignored_exceptions=(WebDriverException,))
    wait_2 = WebDriverWait(driver=driver, timeout=60.0, poll_frequency=0.1, ignored_exceptions=(WebDriverException,))
    driver.get(config.settings.base_url + '/expectations/6/index.html')
    class_name = 'BMH21YY'

    # WHEN
    wait_1.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#btn'))).click()
    answer = wait_2.until(EC.presence_of_element_located((By.CSS_SELECTOR, f'div.{class_name}'))).text

    # THEN
    assert answer == '688596737976'


def test_hunt_for_secret_block(driver_management):
    # GIVEN
    driver = driver_management
    wait = WebDriverWait(driver=driver, timeout=60.0, poll_frequency=0.2, ignored_exceptions=(WebDriverException,))
    driver.get(config.settings.base_url + '/selenium/5.9/2/index.html')
    block_id = 'qQm9y1rk'

    # WHEN
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, f'.box#{block_id}'))).click()
    answer = driver.switch_to.alert.text

    # THEN
    assert answer == 'tlprcp6S-kDbhujKo-uh7Rv9f9-irv26iU9-Zt2XZcIm'


def test_learning_of_attribute_display(driver_management):
    # GIVEN
    driver = driver_management
    wait = WebDriverWait(driver=driver, timeout=60.0, ignored_exceptions=(WebDriverException,))
    driver.get(config.settings.base_url + '/selenium/5.9/3/index.html')
    ids_to_find = ['xhkVEkgm', 'QCg2vOX7', '8KvuO5ja', 'CFoCZ3Ze', '8CiPCnNB', 'XuEMunrz', 'vmlzQ3gH', 'axhUiw2I',
                   'jolHZqD1', 'ZM6Ms3tw', '25a2X14r', 'aOSMX9tb', 'YySk7Ze3', 'QQK13iyY', 'j7kD7uIR']

    # WHEN
    for id_ in ids_to_find:
        wait.until(EC.visibility_of_element_located((By.ID, id_))).click()

    answer = driver.switch_to.alert.text

    # THEN
    assert answer == 'CFoCZ3Ze-8CiPCnNB-XuEMunrz-vmlzQ3gH-axhUiw2I-QQK13iyY-j7kD7uIR'


def test_triumph_over_ad_conspiracy(driver_management):
    # GIVEN
    driver = driver_management
    wait = WebDriverWait(driver=driver, timeout=20.0, ignored_exceptions=(WebDriverException,))
    driver.get(config.settings.base_url + '/selenium/5.9/4/index.html')

    # WHEN
    driver.find_element(By.CSS_SELECTOR, '.close').click()
    wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, '#ad')))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.box button'))).click()
    answer = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#message'))).text

    # THEN
    assert answer == 'FS03-R9R3-SVV9-3P05-DSS1-01VI'


def test_collector_of_secret_runes_1(driver_management):
    # GIVEN
    driver = driver_management
    wait_1 = WebDriverWait(driver=driver, timeout=10.0, ignored_exceptions=(WebDriverException,))
    wait_2 = WebDriverWait(driver=driver, timeout=10.0, ignored_exceptions=(WebDriverException,))
    driver.get(config.settings.base_url + '/selenium/5.9/5/index.html')

    # WHEN
    answer = []

    for i in range(9):
        box = wait_1.until(EC.visibility_of_element_located((By.CSS_SELECTOR, f'.box_button[data-index="{i}"]')))
        box.click()
        wait_1.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#close_ad'))).click()
        wait_2.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, '#ad_window')))
        wait_2.until(text_to_be_present_in_element_(box))
        answer.append(box.text)

    # THEN
    assert '-'.join(answer) == 'F34S-FFS3-56FGH-LKJ0-2E9D-440D-4Q0D-230S-D120'


def test_collector_of_secret_runes_2(driver_management):
    # GIVEN
    driver = driver_management
    wait_1 = WebDriverWait(driver=driver, timeout=10.0, ignored_exceptions=(WebDriverException,))
    wait_2 = WebDriverWait(driver=driver, timeout=10.0, ignored_exceptions=(WebDriverException,))
    driver.get(config.settings.base_url + '/selenium/5.9/5/index.html')

    # WHEN
    answer = []

    for i in range(9):
        box_locator = (By.CSS_SELECTOR, f'.box_button[data-index="{i}"]')
        box = wait_1.until(EC.visibility_of_element_located(box_locator))
        box.click()
        wait_1.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#close_ad'))).click()
        wait_2.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, '#ad_window')))
        wait_2.until(text_to_be_present_in_element_located_(box_locator))
        answer.append(box.text)

    # THEN
    assert '-'.join(answer) == 'F34S-FFS3-56FGH-LKJ0-2E9D-440D-4Q0D-230S-D120'


def test_collector_of_secret_runes_3(driver_management):
    # GIVEN
    driver = driver_management
    wait_1 = WebDriverWait(driver=driver, timeout=5.0, ignored_exceptions=(WebDriverException,))
    wait_2 = WebDriverWait(driver=driver, timeout=10.0, ignored_exceptions=(WebDriverException,))
    driver.get(config.settings.base_url + '/selenium/5.9/5/index.html')

    # WHEN
    answer = []

    for i in range(9):
        box = driver.find_element(By.CSS_SELECTOR, f'.box_button[data-index="{i}"]')
        box.click()
        wait_1.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#close_ad'))).click()
        wait_2.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, '#ad_window')))
        wait_2.until(lambda _: box.text != '')
        answer.append(box.text)

    # THEN
    assert '-'.join(answer) == 'F34S-FFS3-56FGH-LKJ0-2E9D-440D-4Q0D-230S-D120'


def test_flickering_mystery_checkbox(driver_management):
    # GIVEN
    driver = driver_management
    wait_1 = WebDriverWait(driver=driver, timeout=20.0, poll_frequency=0.01, ignored_exceptions=(WebDriverException,))
    wait_2 = WebDriverWait(driver=driver, timeout=2.0, ignored_exceptions=(WebDriverException,))
    driver.get(config.settings.base_url + '/selenium/5.9/6/index.html')

    # WHEN
    if wait_1.until(EC.element_located_to_be_selected((By.CSS_SELECTOR, '#myCheckbox'))):
        driver.find_element(By.CSS_SELECTOR, '#main_container>button').click()
    answer = wait_2.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#result'))).text

    # THEN
    assert answer == '34D0-3SCV-SCM0-654R-DVM9-42IU'


def test_garland_of_checkboxes(driver_management):
    # GIVEN
    driver = driver_management
    wait_1 = WebDriverWait(driver=driver, timeout=10.0, poll_frequency=0.05, ignored_exceptions=(WebDriverException,))
    wait_2 = WebDriverWait(driver=driver, timeout=2.0, ignored_exceptions=(WebDriverException,))
    driver.get(config.settings.base_url + '/selenium/5.9/7/index.html')

    # WHEN
    containers = driver.find_elements(By.CSS_SELECTOR, '.container')

    for container in containers:
        checkbox = container.find_element(By.CSS_SELECTOR, 'input')
        if wait_1.until(EC.element_to_be_selected(checkbox)):
            container.find_element(By.CSS_SELECTOR, 'button').click()

    answer = wait_2.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#result'))).text

    # THEN
    assert answer == 'GFD9-3SV0-3280-WEZC-23UN-Q921-3G5D'