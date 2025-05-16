from selenium.webdriver.common.by import By

LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")

EMAIL_INPUT = (By.NAME, "name")
PASSWORD_INPUT = (By.NAME, "Пароль")
# PASSWORD_INPUT = (By.XPATH, "//input[@placeholder='Введите новый пароль']")

PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']/ancestor::a")

FORGOT_PASSWORD_LINK = (By.XPATH, "//a[@href='/forgot-password' and text()='Восстановить пароль']")

HEADER_FORGOT_PASSWORD = (By.TAG_NAME, "h2")

RESTORE_BUTTON = (By.XPATH, "//button[text()='Восстановить']")

NEW_PASSWORD_INPUT_HIDDEN = (By.CSS_SELECTOR, 'input[type="password"]')
NEW_PASSWORD_INPUT_VIS = (By.NAME, "Введите новый пароль")


SHOW_PASSWORD_BUTTON = (By.CSS_SELECTOR, "div.input__icon-action")



