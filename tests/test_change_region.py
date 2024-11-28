import time
from pages.sbis_contact_page import SbisContactsPage
from pages.sbis_page import SbisPage

SBIS_PAGE = 'https://sbis.ru/'
CONTACTS_SBIS_PAGE = 'https://sbis.ru/contacts'


def test_change_region(driver, setup_logging):

    log = setup_logging

    log.info(f"Переходим на страницу {SBIS_PAGE}")
    start_page = SbisPage(driver,setup_logging)

    # Ожидаем загрузку кнопки контактов
    log.info(f"Получаем кнопку меню Контакты")
    contacts = start_page.get_contacts_button()
    log.info(f"Кликаем по кнопке контакты")
    contacts.click()

    # Ожидаем загрузку попапа с контактами
    log.info(f"Открываем попап")
    contacts_popup = start_page.get_contacts_popup()

    # Ожидаем и кликаем по ссылке
    log.info(f"Получаем ссылку")
    link = start_page.get_your_region_link()
    log.info(f"Кликаем по ссылке")
    link.click()

    log.info(f"Переходим на страницу {CONTACTS_SBIS_PAGE}")
    sbis_contacts_page = SbisContactsPage(driver, setup_logging)

    log.info(f"Получаем название региона")
    my_region = sbis_contacts_page.get_my_region("г. Москва")
    my_region_text = my_region.text

    log.info(f"Получаем блок партнеров для данного региона")
    partners = sbis_contacts_page.get_partners()
    your_region_partners_list = partners.text

    # Проверка соответствия региона
    expected_result = "г. Москва"
    try:
        assert my_region_text == expected_result, f"Название региона не соответствует {expected_result}"
    except AssertionError as e:
        log.error(f"Ошибка при проверке региона: {str(e)}")
        raise

    log.info(f"Кликаем по ссылке с названием региона")
    my_region.click()

    # Проверка выбора региона
    log.info(f"Получаем ссылку на выбранный регион")
    elem = sbis_contacts_page.get_region_in_list(41)

    log.info(f"Кликаем по ссылке")
    time.sleep(3) # Можно заменить на ожидания явные для предотвращения использования time.sleep()
    elem.click()

    log.info(f"Получаем выбранный регион")
    expected_result = "Камчатский край"
    my_region = sbis_contacts_page.get_my_region(expected_result)
    my_region_text = my_region.text

    try:
        assert my_region_text == expected_result, f"Регион не соответствует {expected_result}"
    except AssertionError as e:
        log.error(f"Ошибка при проверке региона: {str(e)}")
        raise

    log.info(f"Получаем список партнеров для данного региона")
    partners_kamchatka = sbis_contacts_page.get_partners()
    partners_kamchatka_list = partners_kamchatka.text

    try:
        assert your_region_partners_list != partners_kamchatka_list, "Список партнеров одинаковый"
    except AssertionError as e:
        log.error(f"Ошибка при проверке партнеров: {str(e)}")
        raise

    log.info(f"Получаем текущий URL страницы")
    current_url = sbis_contacts_page.get_page_url()
    expected_result = "41-kamchatskij-kraj"
    try:
        assert expected_result in current_url, f"В урле отсутствует вхождение подстроки {expected_result}"
    except AssertionError as e:
        log.error(f"Ошибка при проверке URL: {str(e)}")
        raise

    # Проверка title страницы
    log.info(f"Получаем title страницы")
    title = sbis_contacts_page.get_title()
    expected_result = "Камчатский край"
    try:
        assert expected_result in title, f"Отсутствует информация о {expected_result} в title"
    except AssertionError as e:
        log.error(f"Ошибка при проверке title: {str(e)}")
        raise