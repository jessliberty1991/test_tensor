import re
from pages.base_page import BasePage
from locators.sbis_download_locators import SbisDownloadLocators


class SbisDownloadPage(BasePage):
    """
    Класс для работы со страницей загрузки SBIS.
    """

    def __init__(self, driver, setup_logging):
        """
        Инициализация страницы загрузки.

        :param driver: Веб-драйвер Selenium.
        """
        super().__init__(driver, setup_logging)
        self.driver = driver
        self.download_link = None

    def get_downloads_link(self):
        """
        Получение элемента ссылки для загрузки установщика.

        :return: Веб-элемент ссылки.
        :raises TimeoutException: Если элемент не найден.
        """
        self.download_link = self.find_element(SbisDownloadLocators.INSTALLER_DOWNLOAD, name="ссылка для загрузки плагина")
        return self.download_link

    def get_plugin_size(self):
        """
        Получение размера плагина из текста ссылки.

        :return: Размер плагина (float), округленный до одной цифры после запятой.
                 None, если ссылка отсутствует или размер не найден.
        """
        if self.download_link is not None:
            match = re.search(r"\d+\.\d+", self.download_link.text)
            if match:
                return round(float(match.group()), 1)
        return None









