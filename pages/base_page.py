from functools import lru_cache
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait as webdw
from selenium import webdriver


class BasePage:
    def __init__(self, driver, setup_logging):
        self.driver = driver
        self.log = setup_logging

    def switch_to_tab(self,num):
        """
              Переключается на вкладку браузера с указанным индексом.

              :param num: Индекс вкладки, на которую нужно переключиться (начиная с 0).
        """
        self.log.info(f"Переключаемся на вкладку {num}")
        tabs = self.driver.window_handles
        self.driver.switch_to.window(tabs[num])

    def move_to(self, locator, name="Element"):
        """
        Скроллит страницу и наводит курсор мыши на указанный элемент.

        :param locator: Локатор элемента, к которому нужно скроллить (например, (By.ID, "example")).
        :param name: Имя элемента, используемое для логирования (по умолчанию "Element").
        """
        self.log.info(f"Скролимся к {name}")
        action_chains = ActionChains(self.driver)
        action_chains.move_to_element(
            self.find_element(locator))
        action_chains.perform()

    def find_element(self, locator, time=11, name="Element"):
        """
        Поиск элемента на странице с ожиданием.

        :param locator: Локатор элемента (кортеж (By, "value")).
        :param time: Время ожидания в секундах (по умолчанию 11).
        :return: Найденный элемент.
        """
        try:
            self.log.info(f"Ищем элемент {name}")
            element = webdw(self.driver, timeout=time).until(
                ec.presence_of_element_located(locator),
                message=f"Can not find element by locator {locator}"
            )
            return element
        except TimeoutException as e:
            self.log.error(f"Не смогли получить {name}")
            raise

    def find_element_by_text(self, locator, text, time=10):
        """
        Поиск элемента по тексту с ожиданием.

        :param locator: Локатор элемента (кортеж (By, "value")).
        :param text: Текст, который должен присутствовать в элементе.
        :param time: Время ожидания в секундах (по умолчанию 10).
        :return: Найденный элемент.
        """
        try:
            self.log.info(f"Ищем элемент c тексстом {text}")
            webdw(self.driver, timeout=time).until(
                ec.text_to_be_present_in_element(locator, text),
                message=f"Нельзя найти элемент по локатору {locator} с текстом {text}"
            )
            return self.find_element(locator)
        except TimeoutException as e:
            self.log.error(f"Не нашли элемент c текстом {text}")
            raise

    def find_elements(self, locator, time=9):
        """
        Поиск нескольких элементов на странице с ожиданием.

        :param locator: Локатор элементов (кортеж (By, "value")).
        :param time: Время ожидания в секундах (по умолчанию 9).
        :return: Список найденных элементов.
        """
        try:
            elements = webdw(self.driver, timeout=time).until(
                ec.presence_of_elements_located(locator),
                message=f"Can not find elements by locator {locator}"
            )
            return elements
        except TimeoutException as e:
            self.log.error(f"Не нашли элементы по локатору {locator}")
            raise

    def get_page_url(self) -> str:
        """
        Получение текущего URL страницы.

        :return: URL страницы в виде строки.
        """
        return self.driver.current_url

    def get_title(self) -> str:
        """
        Получение заголовка текущей страницы.

        :return: Заголовок страницы в виде строки.
        """
        return self.driver.title