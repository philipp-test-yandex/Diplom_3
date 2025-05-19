import time

import allure
from conftest import *
from pages.main_functionality_page import MainFunctionlity


class TestMainFunctionlity:
    @allure.title("Переход на страницу конструктора")
    def test_go_to_constructor_page(self, driver):
        page = MainFunctionlity(driver)
        page.open_login_form()
        page.click_constuctor_button()
        page.check_header_constructor()
        page.check_on_constructor_page()

    @allure.title("Переход на страницу ленты заказов")
    def test_to_go_orders_feed_page(self, driver):
        page = MainFunctionlity(driver)
        page.open_main_page()
        page.click_orders_feed_button()
        page.check_on_orders_feed_page()
        page.check_header_orders_feed()

    @allure.title("Открытие модального окна ингредиента")
    def test_open_modal_window_with_ingridient(self, driver):
        page = MainFunctionlity(driver)
        page.open_main_page()
        page.click_first_ingredient()
        page.check_ingredient_modal_opened()

    @allure.title("Закрытие модального окна ингредиента")
    def test_closed_window_with_ingridient(self, driver):
        page = MainFunctionlity(driver)
        page.open_main_page()
        page.click_first_ingredient()
        page.click_icon_close()
        page.check_ingredient_modal_closed()

    @allure.title("Увеличение счётчика ингредиентов после перетаскивания")
    def test_raising_order_amount(self, driver):
        page = MainFunctionlity(driver)
        page.open_main_page()

        current = page.get_ingredient_counter_value()
        page.drag_and_drop_first_ingredient_to_cart()
        updated = page.get_ingredient_counter_value()

        assert updated > current, "[Ошибка!] Счётчик не увеличился"

    @allure.title("Оформление заказа авторизованным пользователем")
    def test_confirm_order(self, driver, api_user):
        page = MainFunctionlity(driver)

        page.open_login_form()
        page.enter_email(api_user["email"])
        page.enter_password(api_user["password"])
        page.click_login_button()

        page.click_confirm_order_button()
        page.check_order_confirmation_header()
