import pytest
from selenium import webdriver
from selenium.webdriver.ie.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

import config


@pytest.fixture(scope='function')
def driver_management():
    driver_options = config.settings.driver_options

    if config.settings.driver_name == 'chrome':
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                                  options=driver_options)
    else:
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()),
                                   options=driver_options)

    driver.set_window_size(width=config.settings.window_width,
                           height=config.settings.window_height)

    yield driver

    driver.quit()