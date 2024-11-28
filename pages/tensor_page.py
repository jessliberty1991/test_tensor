from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage
from locators.tensor_locators import TensorLocators


class TensorPage(BasePage):
    """
    Класс для работы с основной страницей Tensor.
    """

    def __init__(self, driver ,setup_logging):
        """
        Инициализация страницы.

        :param driver: Веб-драйвер Selenium.
        """
        super().__init__(driver ,setup_logging)
        self.driver = driver
    def move_to_news(self):
        self.move_to(TensorLocators.BLOCK_NEWS, name="блок новостей")

    def get_block_sila_v_liudiah(self):
        """
        Получение блока 'Сила в людях'.

        :return: Веб-элемент блока.
        :raises TimeoutException: Если элемент не найден.
        """
        return self.find_element(TensorLocators.BLOCK_SILA_V_LIUDIAH, name="блок сила в людях")

    def get_detail_link(self):
        """
        Получение ссылки с деталями из блока 'Сила в людях'.

        :return: Веб-элемент ссылки с деталями.
        :raises TimeoutException: Если элемент не найден.
        :raises IndexError: Если не найдено элементов с деталями.
        """
        block = self.get_block_sila_v_liudiah()
        container = block.find_element(By.XPATH, "./..")
        try:
            details = WebDriverWait(container, timeout=10).until(lambda el: el.find_element(TensorLocators.DETAILS[0], TensorLocators.DETAILS[1]),message="Не найден элемент")
            return details
        except TimeoutException as e:
            print(e.msg)
            raise

