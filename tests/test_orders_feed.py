from conftest import *
from pages.orders_feed_page import OrdersFeed
from helpers.api_client import create_order_and_get_number
import allure

class TestOrdersFeed:

    @allure.title("Клик по заказу открывает всплывающее окно с деталями")
    def test_modal_window_of_order_feed(self, driver):
        page = OrdersFeed(driver)
        page.open_main_page()
        page.click_order_feed_button()
        page.click_first_order_card()
        page.check_order_modal_is_opened()


    @allure.title("Проверка отображения заказов пользователя в ленте заказов")
    def test_users_orders_show_on_feed_page(self, driver, api_user):
        page = OrdersFeed(driver)
        page.open_login_form()
        page.auth_user_on_login_page(api_user)

        page.drag_and_drop_ingredient_and_check_price_increased()

        page.click_confirm_order_button()
        page.wait_for_real_order_number()
        page.click_icon_close()

        page.click_button_personal_account()
        page.click_orders_history_button()

        order_number = page.get_first_order_number()
        page.click_order_feed_button()
        page.check_order_is_in_feed(order_number)


    @allure.title("Проверка увеличения счётчика всех заказов")
    def test_counter_all_the_time(self, driver, api_user):
        page = OrdersFeed(driver)
        page.open_login_form()
        page.auth_user_on_login_page(api_user)
        page.click_order_feed_button()
        count_before = page.get_all_time_order_count()
        create_order_and_get_number(api_user["access_token"])
        page.wait_for_all_time_counter_to_increase(count_before)
        count_after = page.get_all_time_order_count()

        assert count_after > count_before, "[Ошибка!] Счётчик заказов не увеличился!"

    @allure.title("Проверка увеличения счётчика заказов за сегодня")
    def test_counter_today(self, driver, api_user):
        page = OrdersFeed(driver)
        page.open_login_form()
        page.auth_user_on_login_page(api_user)
        page.click_order_feed_button()

        count_before = page.get_complate_order_today()
        create_order_and_get_number(api_user["access_token"])
        page.wait_for_today_counter_to_increase(count_before)
        count_after = page.get_complate_order_today()

        assert count_after > count_before, "[Ошибка!] Счётчик заказов за сегодня не увеличился!"

    @allure.title("Проверка появления нового заказа в разделе 'В работе'")
    def test_order_in_progress_list(self, driver, api_user):
        page = OrdersFeed(driver)
        page.open_login_form()
        page.auth_user_on_login_page(api_user)
        page.click_order_feed_button()

        order_number = create_order_and_get_number(api_user["access_token"])
        in_progress_orders = page.wait_for_order_in_progress(order_number)

        assert str(order_number).zfill(7) in in_progress_orders, \
            f"[Ошибка!] Заказ {order_number} не найден в разделе 'В работе'"
