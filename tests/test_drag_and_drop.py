from selenium.common import WebDriverException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.color import Color
from selenium.webdriver.support.wait import WebDriverWait

import config
from project_tests.conditions.text import text_to_be_present_in_element_


def test_moving_red_block_and_searching_for_secret_token(driver_management):
    # GIVEN
    driver = driver_management
    wait = WebDriverWait(driver=driver, timeout=2.0, ignored_exceptions=(WebDriverException,))
    driver.get(config.settings.base_url + '/draganddrop/1/index.html')

    # WHEN
    action = ActionChains(driver)
    source = driver.find_element(By.CSS_SELECTOR, '#field1')
    target = driver.find_element(By.CSS_SELECTOR, '#field2')
    action.drag_and_drop(source=source, target=target).perform()

    result = driver.find_element(By.CSS_SELECTOR, '#result')
    wait.until(text_to_be_present_in_element_(result))

    # THEN
    assert result.text == 'ODYzNDQ1MzM0NTE0MzQ2OTAwMA=='


def test_square_journey_and_test_points(driver_management):
    # GIVEN
    driver = driver_management
    wait = WebDriverWait(driver=driver, timeout=5.0, ignored_exceptions=(WebDriverException,))
    driver.get(config.settings.base_url + '/draganddrop/3/index.html')

    # WHEN
    block = driver.find_element(By.CSS_SELECTOR, '#block1')
    action = ActionChains(driver)
    action.click_and_hold(block)
    for point in driver.find_elements(By.CSS_SELECTOR, '.controlPoint'):
        action.move_to_element(point)
    action.release().perform()

    result = driver.find_element(By.CSS_SELECTOR, '#message')
    wait.until(text_to_be_present_in_element_(result))

    # THEN
    assert result.text == 'Ni44NTc4MTk2NzY4NTQ0NTZlKzIz'


def test_green_square_movement(driver_management):
    # GIVEN
    driver = driver_management
    wait = WebDriverWait(driver=driver, timeout=5.0, ignored_exceptions=(WebDriverException,))
    driver.get(config.settings.base_url + '/selenium/5.10/2/index.html')

    # WHEN
    target = driver.find_element(By.CSS_SELECTOR, '.draganddrop_end')
    action = ActionChains(driver)

    for block in driver.find_elements(By.CSS_SELECTOR, '.draganddrop'):
        action.drag_and_drop(block, target).perform()

    result = driver.find_element(By.CSS_SELECTOR, '#message')
    wait.until(text_to_be_present_in_element_(result))

    # THEN
    assert result.text == '39FG-3490-34F0-944S-34FV-80VX-F3GJ-349B'


def test_square_adventure(driver_management):
    # GIVEN
    driver = driver_management
    wait = WebDriverWait(driver=driver, timeout=5.0, ignored_exceptions=(WebDriverException,))
    driver.get(config.settings.base_url + '/draganddrop/2/index.html')

    # WHEN
    red_block = driver.find_element(By.CSS_SELECTOR, '#draggable')
    action = ActionChains(driver)

    for box in driver.find_elements(By.CSS_SELECTOR, '.box'):
        action.drag_and_drop(red_block, box).perform()

    result = driver.find_element(By.CSS_SELECTOR, '#message')
    wait.until(text_to_be_present_in_element_(result))

    # THEN
    assert result.text == 'NS4zNDUzMzU0NTQ2MzU0NDVlKzIx'


def test_find_pair(driver_management):
    # GIVEN
    driver = driver_management
    wait = WebDriverWait(driver=driver, timeout=5.0, ignored_exceptions=(WebDriverException,))
    driver.get(config.settings.base_url + '/selenium/5.10/3/index.html')

    # WHEN
    action = ActionChains(driver)

    for square in driver.find_elements(By.CSS_SELECTOR, '.draganddrop_end'):
        square_color = square.value_of_css_property('border-color')
        for box in driver.find_elements(By.CSS_SELECTOR, '.draganddrop'):
            box_color = Color.from_string(box.value_of_css_property('background-color')).rgb
            if square_color == box_color:
                action.drag_and_drop(box, square).perform()
                break

    result = driver.find_element(By.CSS_SELECTOR, '#message')
    wait.until(text_to_be_present_in_element_(result))

    # THEN
    assert result.text == 'F934-3902-2FH4-DV02-3454-9HCX-4F53-12FS'


def test_automatic_sorting_of_balls_1(driver_management):
    # GIVEN
    driver = driver_management
    wait = WebDriverWait(driver=driver, timeout=5.0, ignored_exceptions=(WebDriverException,))
    driver.get(config.settings.base_url + '/selenium/5.10/4/index.html')

    # WHEN
    action = ActionChains(driver)

    for ball in driver.find_elements(By.CSS_SELECTOR, '.ball_color'):
        ball_color = ball.get_attribute('class').split()[1].split('_')[0]
        for basket in driver.find_elements(By.CSS_SELECTOR, '.basket_color'):
            basket_color = basket.get_attribute('class').split()[1]
            if ball_color == basket_color:
                action.drag_and_drop(ball, basket).perform()
                break

    result = driver.find_element(By.CSS_SELECTOR, '.message')
    wait.until(text_to_be_present_in_element_(result))

    # THEN
    assert result.text == 'ER96-SVN0-34HX-ER3W-WHJ5-WHG4-SNJ1-12LO'


def test_automatic_sorting_of_balls_2(driver_management):
    # GIVEN
    driver = driver_management
    wait = WebDriverWait(driver=driver, timeout=5.0, ignored_exceptions=(WebDriverException,))
    driver.get(config.settings.base_url + '/selenium/5.10/4/index.html')

    # WHEN
    action = ActionChains(driver)
    colors = [basket.get_attribute('class').split()[1] for basket in
              driver.find_elements(By.CSS_SELECTOR, '.basket_color')]
    baskets = {color: driver.find_element(By.CSS_SELECTOR, f'.basket_color.{color}') for color in colors}

    for ball in driver.find_elements(By.CSS_SELECTOR, '.ball_color'):
        ball_color = ball.get_attribute('class').split()[1].split('_')[0]
        action.drag_and_drop(ball, baskets[ball_color]).perform()

    result = driver.find_element(By.CSS_SELECTOR, '.message')
    wait.until(text_to_be_present_in_element_(result))
    print(result.text)

    # THEN
    assert result.text == 'ER96-SVN0-34HX-ER3W-WHJ5-WHG4-SNJ1-12LO'


def test_throw_at_right_distance(driver_management):
    # GIVEN
    driver = driver_management
    wait = WebDriverWait(driver=driver, timeout=5.0, ignored_exceptions=(WebDriverException,))
    driver.get(config.settings.base_url + '/selenium/5.10/8/index.html')

    # WHEN
    action = ActionChains(driver)
    distances = [range_.get_attribute('id').split('_')[-1] for range_ in
                 driver.find_elements(By.CSS_SELECTOR, '.range')]

    for distance in distances:
        piece = driver.find_element(By.CSS_SELECTOR, f'#piece_{distance}')
        action.drag_and_drop_by_offset(source=piece, xoffset=int(distance), yoffset=0).perform()

    result = driver.find_element(By.CSS_SELECTOR, '#message')
    wait.until(text_to_be_present_in_element_(result))

    # THEN
    assert result.text == 'GD60-34JX-354F-3HJC-NXC0-54KO-W3B1-2DFH-23JG'


def test_sliders_movement_and_secret_code(driver_management):
    # GIVEN
    driver = driver_management
    wait = WebDriverWait(driver=driver, timeout=5.0, ignored_exceptions=(WebDriverException,))
    driver.get(config.settings.base_url + '/selenium/5.10/6/index.html')

    # WHEN
    for container in driver.find_elements(By.CSS_SELECTOR, '.slider-container'):
        target_value = int(container.find_element(By.CSS_SELECTOR, '.target-value').text)
        current_value = int(container.find_element(By.CSS_SELECTOR, '.current-value').text)
        slider = container.find_element(By.CSS_SELECTOR, '.volume-slider')
        if target_value > current_value:
            button = Keys.ARROW_RIGHT
        elif target_value < current_value:
            button = Keys.ARROW_LEFT
        else:
            continue
        for i in range(abs(target_value - current_value)):
            slider.send_keys(button)

    result = driver.find_element(By.CSS_SELECTOR, '#message')
    wait.until(text_to_be_present_in_element_(result))

    # THEN
    assert result.text == '3F9D-DVB0-EH46-96VB-JHJ5-34UK-2SSF-JKG0'
