import unittest

from selenium import webdriver




START_PAGE = 'http://yandex.ru/'


class TestEnvironment(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get(START_PAGE)
        self.driver.set_page_load_timeout(10)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def tearDown(self) -> None:
        driver = self.driver
        if driver is not None:
            driver.close()
            driver.quit()