from selenium.webdriver.common.by import By

class SbisLocators:
    CONTACTS_BUTTON = (By.CSS_SELECTOR, ".sbisru-Header-ContactsMenu")
    CONTACTS_POPUP = (By.CSS_SELECTOR, ".sbisru-Header-ContactsMenu .sbisru-Header-ContactsMenu__items-visible")
    YOUR_LOCATION_LINK = (By.CSS_SELECTOR, "a[href='/contacts']")
    YOUR_LOCATION = (By.CSS_SELECTOR, ".sbisru-Header__menu .sbis_ru-Region-Chooser")
    DOWNLOADS =(By.CSS_SELECTOR,".sbisru-Footer__container a[href='/download']")


