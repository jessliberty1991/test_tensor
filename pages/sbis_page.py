from pages.base_page import BasePage
from locators.sbis_locators import SbisLocators


class SbisPage(BasePage):
    """
    Класс для работы с основной страницей SBIS.
    """

    def __init__(self, driver, setup_logging):
        """
        Инициализация страницы.

        :param driver: Веб-драйвер Selenium.
        """
        super().__init__(driver, setup_logging)
        self.driver = driver

    def get_contacts_button(self):
        """
        Получение кнопки "Контакты".

        :return: Веб-элемент кнопки.
        :raises TimeoutException: Если элемент не найден.
        """
        return self.find_element(SbisLocators.CONTACTS_BUTTON, name="Кнопка контакты")

    def get_contacts_popup(self):
        """
        Получение всплывающего окна с контактами.

        :return: Веб-элемент всплывающего окна.
        :raises TimeoutException: Если элемент не найден.
        """
        return self.find_element(SbisLocators.CONTACTS_POPUP, name="Всплывающее окно с контактами")

    def get_your_region_link(self):
        """
        Получение ссылки на регион пользователя во всплывающем окне.

        :return: Веб-элемент ссылки.
        :raises TimeoutException: Если элемент не найден.
        """
        contacts_popup = self.get_contacts_popup()
        return contacts_popup.find_element(
            SbisLocators.YOUR_LOCATION_LINK[0],
            SbisLocators.YOUR_LOCATION_LINK[1]
        )

    def get_your_link_region(self):
        """
        Получение элемента текущего региона пользователя.

        :return: Веб-элемент текущего региона.
        :raises TimeoutException: Если элемент не найден.
        """
        contacts_popup = self.get_contacts_popup()
        return contacts_popup.find_element(
            SbisLocators.YOUR_LOCATION[0],
            SbisLocators.YOUR_LOCATION[1]
        )

    def get_downloads_link(self):
        """
        Получение ссылки на страницу загрузок.

        :return: Веб-элемент ссылки.
        :raises TimeoutException: Если элемент не найден.
        """
        return self.find_element(SbisLocators.DOWNLOADS, name="Cсылка на страницу загрузок")








