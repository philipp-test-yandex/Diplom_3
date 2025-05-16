import time

import allure
from pages.base_page import BasePage
from constants.base_url_constants import *
from locators.personal_account_locators import *
from locators.restore_password_locators import EMAIL_INPUT, PASSWORD_INPUT
from selenium.webdriver.support import expected_conditions as EC

class PersonalAccount(BasePage):

    @allure.step("Открыть главную страницу")
    def open_main_page(self):
        self.open_page(BASE_URL)

    @allure.step("Клик по кнопке 'Личный Кабинет'")
    def click_button_personal_account(self):
        self.click(PERSONAL_ACCOUNT_BUTTON)

    @allure.step("Ввести email: {email}")
    def enter_email(self, email):
        self.fill_input(EMAIL_INPUT, email)

    @allure.step("Ввести пароль")
    def enter_password(self, password):
        self.fill_input(PASSWORD_INPUT, password)

    @allure.step("Нажать кнопку 'Войти'")
    def click_login_button(self):
        self.click(LOGIN_BUTTON)

    @allure.step("Проверить, что открыта страница профиля")
    def check_on_account_profile_page(self):
        self.wait_for_url_to_be(PROFILE_URL)
        assert self.driver.current_url == PROFILE_URL, \
            f"[Ошибка!] Ожидался URL '{PROFILE_URL}', но был: '{self.driver.current_url}'"

    @allure.step("Клик по кнопке 'История заказов' и дождаться появление заказа")
    def click_orders_history_button(self):
        self.click(ORDER_HISTORY_BUTTON)
        self.wait.until(EC.visibility_of_element_located(ORDER_NUMBER_IN_HISTORY))
        time.sleep(3)

    @allure.step("Просто клик по кнопке 'История заказов'")
    def just_click_orders_history_button(self):
        self.click(ORDER_HISTORY_BUTTON)

    @allure.step("Проверить, что открыта история заказов")
    def check_on_orders_history_page(self):
        self.wait_for_url_to_be(ORDERS_HISTORY_URL)
        assert self.driver.current_url == ORDERS_HISTORY_URL, \
            f"[Ошибка!] Ожидался URL '{ORDERS_HISTORY_URL}', но был: '{self.driver.current_url}'"

    @allure.step("Нажать кнопку 'Выход'")
    def click_log_out_button(self):
        self.click(LOGOUT_BUTTON)

    @allure.step("Проверить, что произошёл выход (редирект на логин)")
    def check_on_log_out_page(self):
        self.wait_for_url_to_be(LOGIN_URL)
        assert self.driver.current_url == LOGIN_URL, \
            f"[Ошибка!] Ожидался URL '{LOGIN_URL}', но был: '{self.driver.current_url}'"
