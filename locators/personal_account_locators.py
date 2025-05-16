from selenium.webdriver.common.by import By


PERSONAL_ACCOUNT_BUTTON = (By.LINK_TEXT, "Личный Кабинет")
LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")
ORDER_HISTORY_BUTTON = (By.XPATH, "//a[@href='/account/order-history' and text()='История заказов']")
LOGOUT_BUTTON = (By.XPATH, "//button[contains(text(), 'Выход')]")
ORDER_NUMBER_IN_HISTORY = (By.CSS_SELECTOR, "p.text.text_type_digits-default")


