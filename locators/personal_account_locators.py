from selenium.webdriver.common.by import By

CONFIRM_ORDER_BUTTON = (By.XPATH, '//button[text()="Оформить заказ"]')

EMAIL_INPUT = (By.NAME, "name")
PASSWORD_INPUT = (By.NAME, "Пароль")
LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")

PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//a[contains(., 'Личный Кабинет')]")

ORDER_HISTORY_BUTTON = (By.XPATH, "//a[@href='/account/order-history' and text()='История заказов']")

LOGOUT_BUTTON = (By.XPATH, "//button[contains(text(), 'Выход')]")
