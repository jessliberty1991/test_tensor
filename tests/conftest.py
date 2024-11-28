import os
import logging
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

SBIS_PAGE = 'https://sbis.ru/'

@pytest.fixture(scope="module")
def driver():
    """Фикстура для инициализации WebDriver."""
    chrome_options = Options()

    downloaded_folder = os.path.join(os.getcwd(), "tests")

    if not os.path.exists(downloaded_folder):
        os.makedirs(downloaded_folder)


    chrome_options.add_experimental_option("prefs", {
        "download.default_directory": downloaded_folder,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True  #
    })

    driver = webdriver.Chrome(options=chrome_options)
    driver.get(SBIS_PAGE)
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def downloaded_file():
    """Фикстура для работы с загруженным файлом."""
    # Путь к скачанному файлу
    downloaded_folder = os.path.join(os.getcwd(),"tests")
    downloaded_file_path = os.path.join(downloaded_folder, "sbisplugin-setup-web.exe")
    # Ожидаем, что файл будет скачан
    yield downloaded_file_path

    # После завершения теста удаляем файл
    if os.path.exists(downloaded_file_path):
        os.remove(downloaded_file_path)
        print(f"Файл {downloaded_file_path} удалён после теста.")


@pytest.fixture(scope="session", autouse=True)
def setup_logging():
    """Фикстура для настройки логирования для всех тестов."""
    logger = logging.getLogger("pytest-logger")
    logger.setLevel(logging.INFO)

    # Удаляем все существующие обработчики
    if logger.hasHandlers():
        logger.handlers.clear()

    # Добавляем обработчик для консоли
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
    logger.addHandler(console_handler)

    # Добавляем обработчик для файла
    file_handler = logging.FileHandler("test_run.log")
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
    logger.addHandler(file_handler)

    logger.info("Логирование настроено")
    logger.info("=====================================================================")
    yield logger
    logger.info("Тестовая сессия завершена")
    logger.info("=====================================================================")