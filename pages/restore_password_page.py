import allure
from pages.base_page import BasePage
from constants.base_url_constants import *
from locators.restore_password_locators import *


class RestorePasswordPage(BasePage):

    @allure.step("Открыть форму авторизации")
    def open_login_form(self):
        self.open_page(LOGIN_URL)

    @allure.step("Ввести email: {email}")
    def enter_email(self, email):
        self.fill_input(EMAIL_INPUT, email)

    @allure.step("Ввести пароль: {password}")
    def enter_password(self, password):
        self.fill_input(PASSWORD_INPUT, password)

    @allure.step("Клик на ссылку 'Восстановить пароль'")
    def click_link_forgot_password(self):
        self.click(FORGOT_PASSWORD_LINK)

    @allure.step("Клик по кнопке 'Восстановить'")
    def click_restore_button(self):
        self.click(RESTORE_BUTTON)

    @allure.step("Проверка URL страницы восстановления пароля")
    def check_on_forgot_password_page(self):
        self.wait_for_url_to_be(FORGOT_PASSWORD_URL)
        current_url = self.get_current_url()
        assert current_url == FORGOT_PASSWORD_URL, \
            f"[Ошибка!] Ожидался URL восстановления пароля, но был: {current_url}"

    @allure.step("Проверка заголовка на странице восстановления")
    def check_header_forgot_password(self):
        header = self.wait_for_element_visible(HEADER_FORGOT_PASSWORD)
        assert header.text == "Восстановление пароля", \
            f"[Ошибка!] Ожидался заголовок 'Восстановление пароля', но был: '{header.text}'"

    @allure.step("Проверка перехода на страницу сброса пароля")
    def check_on_reset_password_page(self):
        self.wait_for_url_to_be(RESET_PASSWORD_URL)
        current_url = self.get_current_url()
        assert current_url == RESET_PASSWORD_URL, \
            f"[Ошибка!] Ожидался URL '{RESET_PASSWORD_URL}', но был: '{current_url}'"

    @allure.step("Ввод нового пароля")
    def enter_new_password(self, password):
        self.fill_input(NEW_PASSWORD_INPUT_HIDDEN, password)

    @allure.step("Проверка, что поле пароля скрыто (type='password')")
    def check_password_hidden(self):
        input_type = self.get_element(NEW_PASSWORD_INPUT_HIDDEN).get_attribute("type")
        assert input_type == "password", \
            f"[Ошибка!] Ожидался скрытый ввод пароля (type='password'), но получен: {input_type}"

    @allure.step("Клик на иконку показа пароля")
    def click_show_password(self):
        self.click(SHOW_PASSWORD_BUTTON)

    @allure.step("Проверка, что поле пароля стало видимым (type='text')")
    def check_password_visible(self):
        input_type = self.get_element(NEW_PASSWORD_INPUT_VIS).get_attribute("type")
        assert input_type == "text", \
            f"[Ошибка!] Ожидался отображаемый пароль (type='text'), но получен: {input_type}"
