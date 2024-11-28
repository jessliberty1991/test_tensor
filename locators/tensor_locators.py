from selenium.webdriver.common.by import By

class TensorLocators:
    TENSOR_LOGO = (By.CSS_SELECTOR,"[name='headerLogo']")
    BLOCK_SILA_V_LIUDIAH= (By.CSS_SELECTOR, ".tensor_ru-Index__block4-content .tensor_ru-Index__card-title")
    DETAILS=(By.CSS_SELECTOR,"a[href='/about']")
    BLOCK_NEWS = (By.CSS_SELECTOR,'.tensor_ru-Index__block4-bg')

