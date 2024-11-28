from pages.sbis_download_page import SbisDownloadPage
from pages.sbis_page import SbisPage
from tests.exceptions.exceptions import ElementIsNotFound
from tests.utils import wait_for_download

SBIS_PAGE = 'https://sbis.ru/'


def test_download(driver, downloaded_file, setup_logging):

    log = setup_logging
    log.info(f"Переходим на страницу {SBIS_PAGE}")
    start_page = SbisPage(driver,setup_logging)

    # Получаем ссылку из футера для перехода на страницу загрузки плагина
    log.info(f"Получаем ссылку из футера для перехода на страницу загрузки плагина")
    try:
        footer_download = start_page.get_downloads_link()
        if footer_download is None:
            raise ElementIsNotFound("Cсылка 'Cкачать локальные версии' не обнаружена на странице")
    except ElementIsNotFound as e:
        log.error(f"Ошибка получения ссылки из футера: {str(e)}")
        raise

    log.info(f"Наводим мышь на ссылку и кликаем по ней")
    footer_download.click()

    log.info(f"Переходим на страницу https://sbis.ru/download")
    sbis_download_page = SbisDownloadPage(driver,setup_logging)

    # Получаем ссылку для скачивания плагина
    try:
        log.info(f"Получаем ссылку для загрузки плагина")
        download_link = sbis_download_page.get_downloads_link()
        if download_link is None:
            raise ElementIsNotFound('Ссылка для скачивания плагина не обнаружена на странице')
    except ElementIsNotFound as e:
        log.error(f"Ошибка получения ссылки для скачивания плагина: {str(e)}")
        raise

    log.info(f"Кликаем по ссылке для скачивания плагина")
    download_link.click()

    # Получаем размер плагина для отслеживания загрузки
    try:
        plugin_size = sbis_download_page.get_plugin_size()
        if plugin_size is None:
            raise ValueError('Не смогли получить размер файла для скачивания')
    except ValueError as e:
        log.error(f"Ошибка при получении размера плагина: {str(e)}")
        raise

    log.info(f"Ждем загрузки файла размером {plugin_size} MB")

    # Ожидаем завершения загрузки файла
    wait_for_download(downloaded_file, plugin_size)
    log.info(f"Загрузка завершена")