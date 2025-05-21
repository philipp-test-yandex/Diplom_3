import time

import allure
from pages.base_page import BasePage
from constants.base_url_constants import *
from locators.personal_account_locators import *

class PersonalAccount(BasePage):

    @allure.step("Открыть форму входа (страницу логина)")
    def open_login_form(self):
        self.open_page(LOGIN_URL)
    @allure.step("Ввести email")
    def enter_email(self, email):
        self.fill_input(EMAIL_INPUT, email)

    @allure.step("Ввести пароль")
    def enter_password(self, password):
        self.fill_input(PASSWORD_INPUT, password)

    @allure.step("Нажать кнопку 'Войти'")
    def click_login_button(self):
        self.click(LOGIN_BUTTON)

    @allure.step("Клик по кнопке 'Личный Кабинет'")
    def click_button_personal_account(self):
        self.click(PERSONAL_ACCOUNT_BUTTON)

    @allure.step("Авторизовать юзера")
    def auth_user_on_login_page(self, user_data):
        self.enter_email(user_data["email"])
        self.enter_password(user_data["password"])
        self.click_login_button()
        self.get_visible_element(CONFIRM_ORDER_BUTTON)


    @allure.step("Клик по кнопке 'Личный Кабинет'")
    def click_button_personal_account(self):
        self.wait_for_element_visible(PERSONAL_ACCOUNT_BUTTON)
        self.click(PERSONAL_ACCOUNT_BUTTON)

    @allure.step("Проверить, что открыта страница профиля")
    def check_on_account_profile_page(self):
        self.wait_for_url_to_be(PROFILE_URL)
        current_url = self.get_current_url()
        assert current_url == PROFILE_URL, \
            f"[Ошибка!] Ожидался URL '{PROFILE_URL}', но был: '{current_url}'"

    @allure.step("Просто клик по кнопке 'История заказов'")
    def just_click_orders_history_button(self):
        self.click(ORDER_HISTORY_BUTTON)

    @allure.step("Проверить, что открыта история заказов")
    def check_on_orders_history_page(self):
        self.wait_for_url_to_be(ORDERS_HISTORY_URL)
        current_url = self.get_current_url()
        assert current_url == ORDERS_HISTORY_URL, \
            f"[Ошибка!] Ожидался URL '{ORDERS_HISTORY_URL}', но был: '{current_url}'"

    @allure.step("Нажать кнопку 'Выход'")
    def click_log_out_button(self):
        self.wait_for_element_visible(LOGOUT_BUTTON)
        self.click(LOGOUT_BUTTON)

    @allure.step("Проверить, что произошёл выход (редирект на логин)")
    def check_on_log_out_page(self):
        self.wait_for_url_to_be(LOGIN_URL)
        current_url = self.get_current_url()
        assert current_url == LOGIN_URL, \
            f"[Ошибка!] Ожидался URL '{LOGIN_URL}', но был: '{current_url}'"
