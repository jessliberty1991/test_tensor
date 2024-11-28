from pages.sbis_contact_page import SbisContactsPage
from pages.sbis_page import SbisPage
from pages.tensor_page import TensorPage
from pages.tensor_about_page import TensorAboutPage
from tests.utils import check_size_image

SBIS_PAGE = 'https://sbis.ru/'
CONTACTS_SBIS_PAGE = 'https://sbis.ru/contacts'
TENSOR_PAGE = 'https://tensor.ru/'
TENSOR_ABOUT_PAGE = 'https://tensor.ru/about'


def test_contacts(driver, setup_logging):

    log = setup_logging
    log.info(f"Заходим на страницу {SBIS_PAGE}")

    # Открытие главной страницы и кнопки контактов
    start_page = SbisPage(driver, setup_logging)
    log.info(f"Получаем кнопку контактов")
    contacts = start_page.get_contacts_button()
    contacts.click()

    start_page.get_contacts_popup()
    your_location_link = start_page.get_your_region_link()
    your_location_link.click()

    sbis_page = SbisContactsPage(driver, setup_logging)

    # Ожидание баннера и клика по нему
    log.info(f"Получаем баннер тензора")
    tensor_banner = sbis_page.get_tensor_banner()
    log.info(f"Кликаем по баннеру")
    tensor_banner.click()

    # Переход на страницу Tensor
    log.info(f"Переходим на страницу {TENSOR_PAGE}")
    tensor_page = TensorPage(driver,setup_logging)

    # Ожидание страницы, прокрутка
    log.info(f"Находим баннер 'Сила в людях'")

    tensor_page.switch_to_tab(1)
    tensor_page.move_to_news()
    sila_v_liudiah = tensor_page.get_block_sila_v_liudiah()

    log.info(f"Получаем кнопку 'Подробнее'")
    details = tensor_page.get_detail_link()
    log.info(f"Кликаем по кнопке 'Подробнее'")
    details.click()


    # Переход на страницу о компании Tensor
    log.info(f"Переходим на страницу {TENSOR_ABOUT_PAGE}")
    tensor_about = TensorAboutPage(driver, setup_logging)
    log.info(f"Получаем блок 'Работаем'")
    work_block = tensor_about.get_work_block()

    log.info(f"Получаем картинки блока 'Работаем'")
    tensor_about.switch_to_tab(1)
    tensor_about.move_to_work_block()

    images_work_block = tensor_about.get_images_in_work_block()

    # Проверка URL страницы
    expected_result = TENSOR_ABOUT_PAGE
    log.info(f"Получаем текущий URL")
    current_title = start_page.get_page_url()
    log.info(f"Текущий URL: {current_title}")

    try:
        assert current_title == expected_result, f"Ожидаемый заголовок: {expected_result}, Текущий: {current_title}"
    except AssertionError as e:
        log.error(f"Ошибка в проверке URL: {e}")

    # Проверка изображений на одинаковый размер

    result = check_size_image(images_work_block)
    try:
        assert result, "Картинки неодинаковы"
    except AssertionError as e:
        log.error(f"Ошибка при проверке размеров изображений: {e}")