from conftest import *
from pages.personal_account_page import PersonalAccount

@allure.feature("Личный кабинет")
class TestPersonalAccount:

    def test_go_to_personal_account(self, driver, api_user):
        page = PersonalAccount(driver)
        page.open_main_page()
        page.click_button_personal_account()
        page.enter_email(api_user["email"])
        page.enter_password(api_user["password"])
        page.click_login_button()
        page.click_button_personal_account()
        page.check_on_account_profile_page()

    def test_go_to_orders_history(self, driver, api_user):
        page = PersonalAccount(driver)
        page.open_main_page()
        page.click_button_personal_account()
        page.enter_email(api_user["email"])
        page.enter_password(api_user["password"])
        page.click_login_button()
        page.click_button_personal_account()


        page.just_click_orders_history_button()

        page.check_on_orders_history_page()

    def test_log_out(self, driver, api_user):
        page = PersonalAccount(driver)
        page.open_main_page()
        page.click_button_personal_account()
        page.enter_email(api_user["email"])
        page.enter_password(api_user["password"])
        page.click_login_button()
        page.click_button_personal_account()
        page.click_log_out_button()
        page.check_on_log_out_page()
