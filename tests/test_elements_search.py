from selenium.common import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

import config


def test_form_filling_wizard(driver_management):
    # GIVEN
    driver = driver_management
    wait = WebDriverWait(driver=driver, timeout=2, ignored_exceptions=(WebDriverException,))
    driver.get(config.settings.base_url + '/selenium/1/1.html')

    # WHEN
    all_forms = wait.until(lambda driver: driver.find_elements(By.CSS_SELECTOR, '.form'))

    for form in all_forms:
        form.send_keys('Text')

    wait.until(lambda driver: driver.find_element(By.CSS_SELECTOR, '.btn')).click()
    answer = wait.until(lambda driver: driver.find_element(By.CSS_SELECTOR, '#result').text)

    # THEN
    assert answer == '1123581321345589144233377610987'


def test_treasure_hunter(driver_management):
    # GIVEN
    driver = driver_management
    wait = WebDriverWait(driver=driver, timeout=2, ignored_exceptions=(WebDriverException,))
    driver.get(config.settings.base_url + '/selenium/2/2.html')
    text = '16243162441624'

    # WHEN
    link = wait.until(lambda driver: driver.find_element(By.LINK_TEXT, text)).get_attribute('href')
    driver.get(link)
    answer = wait.until(lambda driver: driver.find_element(By.CSS_SELECTOR, '#result')).text

    # THEN
    assert answer == '324165465463156465'


def test_codex_of_numbers_hunter(driver_management):
    # GIVEN
    driver = driver_management
    wait = WebDriverWait(driver=driver, timeout=2, ignored_exceptions=(WebDriverException,))
    driver.get(config.settings.base_url + '/selenium/3/3.html')

    elems = wait.until(lambda driver: driver.find_elements(By.CSS_SELECTOR, '.text p'))
    summ = sum(int(elem.text) for elem in elems)

    # THEN
    assert summ == 450384194300


def test_treasure_hunt_in_numbers_labyrinth(driver_management):
    # GIVEN
    driver = driver_management
    wait = WebDriverWait(driver=driver, timeout=2, ignored_exceptions=(WebDriverException,))
    driver.get(config.settings.base_url + '/selenium/3/3.html')

    # WHEN
    elems = wait.until(lambda driver: driver.find_elements(By.CSS_SELECTOR, 'div.text p:nth-child(2)'))
    '''или 
    elems = wait.until(lambda driver: driver.find_elements(By.XPATH, '//div[@class="text"]/p[2]'))
    '''
    summ = sum(int(elem.text) for elem in elems)
    print(summ)

    # THEN
    assert summ == 149494128600


def test_operation_combination_lock(driver_management):
    # GIVEN
    driver = driver_management
    wait = WebDriverWait(driver=driver, timeout=2, ignored_exceptions=(WebDriverException,))
    driver.get(config.settings.base_url + '/selenium/4/4.html')

    # WHEN
    k = 1
    while True:
        try:
            wait.until(lambda driver: driver.find_element(By.CSS_SELECTOR, f'.check[value="{k}"]')).click()
            k += 1
        except WebDriverException:
            break
        except Exception as ex:
            raise ex

    wait.until(lambda driver: driver.find_element(By.CSS_SELECTOR, '.btn')).click()
    answer = wait.until(lambda driver: driver.find_element(By.CSS_SELECTOR, '#result')).text

    # THEN
    assert answer == '3,1415926535897932384626433832795028841971'


def test_code_odyssey(driver_management):
    # GIVEN
    driver = driver_management
    wait = WebDriverWait(driver=driver, timeout=2, ignored_exceptions=(WebDriverException,))
    driver.get(config.settings.base_url + '/selenium/5/5.html')
    numbers = {1, 2, 3, 4, 8, 9, 11, 12, 13, 14, 15, 16, 17, 22, 23, 28, 29, 33, 34, 38,
               39, 43, 44, 48, 49, 51, 52, 53, 54, 55, 56, 57, 58, 61, 62, 63, 64, 68, 69, 73,
               74, 78, 79, 83, 84, 88, 89, 91, 92, 97, 98, 101, 104, 108, 109, 113, 114, 118,
               119, 123, 124, 128, 129, 131, 132, 137, 138, 140, 141, 144, 145, 148, 149, 153,
               154, 158, 159, 163, 164, 165, 168, 169, 171, 172, 177, 178, 180, 181, 184, 185,
               187, 188, 189, 190, 192, 193, 194, 195, 197, 198, 199, 200, 204, 205, 206, 207,
               208, 209, 211, 212, 217, 218, 220, 221, 224, 225, 227, 228, 229, 230, 232, 233,
               234, 235, 237, 238, 239, 240, 245, 246, 247, 248, 249, 251, 252, 253, 254, 255,
               256, 257, 258, 260, 261, 264, 265, 268, 269, 273, 274, 278, 279, 288, 289, 291,
               292, 293, 294, 295, 296, 297, 300, 301, 302, 303, 304, 305, 308, 309, 313, 314,
               318, 319, 328, 329, 331, 332, 339, 340, 341, 342, 343, 344, 345, 346, 348, 349,
               353, 354, 358, 359, 368, 369, 371, 372, 379, 380, 385, 386, 408, 409, 411, 412,
               419, 420, 425, 426, 428, 429, 433, 434, 438, 439, 444, 445, 446, 447, 448, 451,
               452, 459, 460, 465, 466, 467, 468, 469, 470, 472, 473, 474, 475, 477, 478, 479,
               480, 485, 486, 487, 488, 491, 492, 499, 500, 505, 506, 508, 509, 513, 514, 518, 519}

    # WHEN
    elems = wait.until(lambda driver: driver.find_elements(By.CSS_SELECTOR, '.check'))

    for elem in elems:
        if int(elem.get_attribute('value')) in numbers:
            elem.click()

    wait.until(lambda driver: driver.find_element(By.CSS_SELECTOR, '.btn')).click()
    answer = wait.until(lambda driver: driver.find_element(By.CSS_SELECTOR, '#result')).text

    # THEN
    assert answer == '932169874631968746874987464354'


def test_operation_drop_down_lists(driver_management):
    # GIVEN
    driver = driver_management
    wait = WebDriverWait(driver=driver, timeout=2, ignored_exceptions=(WebDriverException,))
    driver.get(config.settings.base_url + '/selenium/7/7.html')

    # WHEN
    elems = wait.until(lambda driver: driver.find_elements(By.CSS_SELECTOR, '#opt option'))
    summ = sum(int(elem.text) for elem in elems)
    wait.until(lambda driver: driver.find_element(By.CSS_SELECTOR, '#input_result')).click()
    wait.until(lambda driver: driver.find_element(By.CSS_SELECTOR, '#input_result')).send_keys(str(summ))
    wait.until(lambda driver: driver.find_element(By.CSS_SELECTOR, '.btn')).click()
    answer = wait.until(lambda driver: driver.find_element(By.CSS_SELECTOR, '#result')).text

    # THEN
    assert answer == '321687416587463168743416874641687'


def test_mysterious_trail_mission(driver_management):
    # GIVEN
    driver = driver_management
    wait = WebDriverWait(driver=driver, timeout=2, ignored_exceptions=(WebDriverException,))
    driver.get(config.settings.base_url + '/selenium/6/6.html')
    number = ((12434107696 * 3) * 2) + 1

    # WHEN
    wait.until(lambda driver: driver.find_element(By.CSS_SELECTOR, '#selectId')).click()
    wait.until(lambda driver: driver.find_element(By.XPATH, f'//option[.="{number}"]')).click()
    wait.until(lambda driver: driver.find_element(By.CSS_SELECTOR, '.btn')).click()
    answer = wait.until(lambda driEver: driver.find_element(By.CSS_SELECTOR, '#result')).text

    # THEN
    assert answer == '98763216843164361841357461685743168461'






