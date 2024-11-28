import re
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait as webdw
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from locators.sbis_contacts_locators import SbisContactsLocators


class SbisContactsPage(BasePage):
    def __init__(self, driver,setup_logging):
        """
        Инициализация страницы контактов.

        :param driver: Веб-драйвер Selenium.
        """
        super().__init__(driver,setup_logging)
        self.driver = driver
        self.tensor_banner = None
        self.region_chooser = None
        self.region = None

    def get_tensor_banner(self):
        """
        Получение баннера Tensor.

        :return: Элемент баннера Tensor.
        """
        self.tensor_banner = self.find_element(SbisContactsLocators.TENSOR_BANNER, name="баннер Тензора")
        return self.tensor_banner

    def get_my_region(self, region_text):
        """
        Получение элемента региона с заданным текстом.

        :param region_text: Текст региона для поиска.
        :return: Элемент региона.
        """
        return self.find_element_by_text(SbisContactsLocators.MY_REGION, region_text)

    def get_partners(self):
        """
        Получение элемента блока партнеров.

        :return: Элемент блока партнеров.
        """
        return self.find_element(SbisContactsLocators.PARTNERS, name="блок партнеров")

    def get_region_in_list(self, region_number):
        """
        Получение элемента региона в списке по его номеру.

        :param region_number: Номер региона для поиска.
        :return: Элемент региона в списке.
        """
        self.region_chooser = self.find_element(SbisContactsLocators.REGION_CHOOSER)
        self.region = webdw(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, f"//li[.//*[contains(text(), '{region_number}')]]")
            )
        )
        return self.region

    def get_name_region_in_list(self):
        """
        Получение имени региона из списка.

        :return: Имя региона (строка).
        """
        if self.region_chooser is None:
            return ""

        region_name = re.sub(r'^\d+', '', self.region.text)  # Убираем цифры из начала строки
        return region_name.strip()  # Убираем лишние пробелы




