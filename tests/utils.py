import os
import time


def check_size_image(images):
    """
    Проверяет, одинакова ли ширина и высота переданных изображений.

    :param images: Список объектов изображений, поддерживающих метод `getAttribute`.
    :return: True, если ширина и высота всех изображений совпадают, иначе False.
    """
    # Проверяем размеры первого изображения
    width = images[0].get_attribute("width")
    height = images[0].get_attribute("height")

    # Сравниваем размеры с остальными изображениями
    for i in range(1, len(images)):
        if width != images[i].get_attribute("width") or height != images[i].get_attribute("height"):
            return False
    return True


def wait_for_download(file_path, size, timeout=30):
    """
    Проверяет, загрузился ли файл за указанное время.

    :param file_path: Путь к файлу, который необходимо проверить.
    :param size: Размер файла в мегабайтах (MB), который ожидается.
    :param timeout: Время ожидания в секундах (по умолчанию 30 секунд).
    :return: True, если файл загрузился и его размер соответствует ожиданиям.
    :raises TimeoutError: Если файл не загрузился или размер не совпадает.
    """
    start_time = time.time()

    while time.time() - start_time < timeout:
        if os.path.exists(file_path):
            file_size_mb = bites_to_MB(os.path.getsize(file_path))

            # Допускаем небольшую разницу в размере (до 0.5 MB)
            if abs(file_size_mb - size) <= 0.5:
                return True

        time.sleep(0.5)


    raise TimeoutError(f"За {timeout} секунд файл не скачался или его размер не соответствует ожиданиям.")


def bites_to_MB(size):
    """
    Переводит байты в мегабайты (MB).

    :param size: Размер в байтах.
    :return: Размер в мегабайтах (MB).
    """
    return size / 1048576  # 1 MB = 1024 * 1024 байт

