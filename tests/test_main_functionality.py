import time

import allure
from conftest import *
from pages.main_functionality_page import MainFunctionlity
from pages.personal_account_page import PersonalAccount


class TestMainFunctionlity:
    def test_go_to_constructor_page(self, driver):
        page = MainFunctionlity(driver)
        page.open_login_form()
        page.click_constuctor_button()
        page.check_header_constructor()
        page.check_on_constructor_page()


    def test_to_go_orders_feed_page(self, driver):
        page = MainFunctionlity(driver)
        page.open_main_page()
        page.click_orders_feed_button()
        page.check_on_orders_feed_page()
        page.check_header_orders_feed()


    def test_open_modal_window_with_ingridient(self, driver):
        page = MainFunctionlity(driver)
        page.open_main_page()
        page.click_first_ingredient()
        page.check_ingredient_modal_opened()

    def test_closed_window_with_ingridient(self, driver):
        page = MainFunctionlity(driver)
        page.open_main_page()
        page.click_first_ingredient()
        page.click_icon_close()
        page.check_ingredient_modal_closed()

    def test_raising_order_amount(self, driver):
        page = MainFunctionlity(driver)
        page.open_main_page()

        current = page.get_ingredient_counter_value()
        page.drag_and_drop_first_ingredient_to_cart()

        updated = MainFunctionlity(driver).get_ingredient_counter_value()

        assert updated > current, \
            f"[Ошибка!] Счётчик не увеличился"

    def test_confirm_order(self, driver, api_user):
        MainFunctionlity(driver).open_login_form()
        PersonalAccount(driver).enter_email(api_user["email"])
        PersonalAccount(driver).enter_password(api_user["password"])
        PersonalAccount(driver).click_login_button()
        MainFunctionlity(driver).click_confirm_order_button()
        MainFunctionlity(driver).check_order_confirmation_header()