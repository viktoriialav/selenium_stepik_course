from selenium.webdriver.common.by import By


def size_increment(driver):
    ex_current_window_size = driver.get_window_size()
    in_current_width = driver.find_element(By.CSS_SELECTOR, '#width').text.split()[-1]
    in_current_height = driver.find_element(By.CSS_SELECTOR, '#height').text.split()[-1]
    d_width = ex_current_window_size['width'] - int(in_current_width)
    d_height = ex_current_window_size['height'] - int(in_current_height)
    return d_width, d_height

def next_tab(driver):
    tabs = driver.window_handles
    current = driver.current_window_handle
    current_index = tabs.index(current)
    return tabs[0] if current_index >= len(tabs) - 1 else tabs[current_index + 1]