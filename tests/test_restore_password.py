from conftest import *
from pages.restore_password_page import RestorePasswordPage
import allure

@allure.feature("Восстановление пароля")
class TestRestorePassword:

    @allure.title("Открытие страницы восстановления пароля")
    def test_open_forgot_password_page(self, driver):
        page = RestorePasswordPage(driver)
        page.open_login_form()
        page.click_link_forgot_password()
        page.check_on_forgot_password_page()
        page.check_header_forgot_password()

    @allure.title("Ввод email для восстановления пароля")
    def test_restore_password_email_input(self, driver, api_user):
        page = RestorePasswordPage(driver)
        page.open_login_form()
        page.click_link_forgot_password()
        page.enter_email(api_user["email"])
        page.click_restore_button()
        page.check_on_reset_password_page()

    @allure.title("Проверка показа/скрытия пароля при восстановлении")
    def test_password_field_focus(self, driver, api_user):
        page = RestorePasswordPage(driver)
        page.open_login_form()
        page.click_link_forgot_password()
        page.enter_email(api_user["email"])
        page.click_restore_button()
        page.enter_new_password(api_user["password"])
        page.check_password_hidden()
        page.click_show_password()
        page.check_password_visible()
