from selenium.webdriver.common.by import By

class SbisContactsLocators:
    TENSOR_BANNER = (By.CSS_SELECTOR, ".sbisru-Contacts__logo-tensor")
    MY_REGION = (By.CSS_SELECTOR, "span.sbis_ru-Region-Chooser__text.sbis_ru-link")
    PARTNERS = (By.CSS_SELECTOR, "#contacts_list [data-qa='items-container']")
    REGION_CHOOSER = (By.CSS_SELECTOR, "div[name='dialog']")