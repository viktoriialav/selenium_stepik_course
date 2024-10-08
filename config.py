from typing import Literal, Optional

from pydantic_settings import BaseSettings
from selenium.webdriver import ChromeOptions, FirefoxOptions

from project_tests.utils.path import abs_path_from_root

EnvContext = Literal['local_chrome', 'local_firefox']

class Settings(BaseSettings):
    context: EnvContext = 'local_chrome'

    base_url: str = 'https://parsinger.ru'
    driver_name: str = 'chrome'
    window_width: int = 1920
    window_height: int = 1080

    @property
    def driver_options(self):
        if self.driver_name == 'chrome':
            options = ChromeOptions()
        else:
            options = ChromeOptions()

        options.page_load_strategy = 'eager'

        return options

    @classmethod
    def in_context(cls, env: Optional[EnvContext] = None):
        env = env or cls().context
        return cls(_env_file=abs_path_from_root(f'.env.{env}'))


settings = Settings.in_context()
