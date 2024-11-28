from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from locators.tensor_locators import TensorLocators
from locators.tensor_about_locators import TensorAboutLocators


class TensorAboutPage(BasePage):
    """
    Класс для работы со страницей "О компании" Tensor.
    """

    def __init__(self, driver,setup_logging):
        """
        Инициализация страницы.

        :param driver: Веб-драйвер Selenium.
        """
        super().__init__(driver, setup_logging)
        self.driver = driver

    def get_work_block(self):
        """
        Получение блока с описанием работы.

        :return: Веб-элемент блока работы.
        :raises TimeoutException: Если элемент не найден.
        """
        return self.find_element(TensorAboutLocators.WORK_BLOCK, name="Блок Работаем")

    def get_images_in_work_block(self):
        """
        Получение изображений внутри блока работы.

        :return: Список веб-элементов изображений.
        :raises TimeoutException: Если блок работы или изображения не найдены.
        """
        work_block = self.get_work_block()
        return work_block.find_elements(TensorAboutLocators.WORK_BLOCK_IMAGES[0], TensorAboutLocators.WORK_BLOCK_IMAGES[1])

    def move_to_work_block(self):
        """
        Скролл к блоку работы.

        """
        self.move_to(TensorAboutLocators.WORK_BLOCK, name = "Блок работаем")

