from conftest import *
from pages.orders_feed_page import OrdersFeed
from pages.main_functionality_page import MainFunctionlity
from pages.personal_account_page import PersonalAccount
from helpers.api_client import create_order_and_get_number
class TestOrdersFeed:
    def test_modal_window_of_order_feed(self, driver):
        page = OrdersFeed(driver)
        MainFunctionlity(driver).open_main_page()
        page.click_order_feed_button()
        page.click_order_history_card()
        page.check_order_number_format()
        page.check_url_contains_order_hash()


    def test_users_orders_show_on_feed_page(self, driver, api_user):
        PersonalAccount(driver).open_main_page()
        PersonalAccount(driver).click_button_personal_account()
        PersonalAccount(driver).enter_email(api_user["email"])
        PersonalAccount(driver).enter_password(api_user["password"])
        PersonalAccount(driver).click_login_button()
        MainFunctionlity(driver).drag_and_drop_first_ingredient_to_cart()

        MainFunctionlity(driver).click_confirm_order_button()
        MainFunctionlity(driver).click_icon_close()

        PersonalAccount(driver).click_button_personal_account()
        PersonalAccount(driver).click_orders_history_button()

        order_number = OrdersFeed(driver).get_first_order_number()

        OrdersFeed(driver).click_order_feed_button()
        OrdersFeed(driver).check_order_is_in_feed(order_number)

    def test_counter_all_the_time(self, driver, api_user):
        MainFunctionlity(driver).open_login_form()
        PersonalAccount(driver).enter_email(api_user["email"])
        PersonalAccount(driver).enter_password(api_user["password"])
        OrdersFeed(driver).click_order_feed_button()

        count_before = OrdersFeed(driver).get_all_time_order_count()

        create_order_and_get_number(api_user["access_token"])

        count_after = OrdersFeed(driver).get_all_time_order_count()

        assert count_after > count_before, "[Ошибка!] Счётчик заказов не увеличился!"


    def test_counter_today(self, driver, api_user):
        MainFunctionlity(driver).open_login_form()
        PersonalAccount(driver).enter_email(api_user["email"])
        PersonalAccount(driver).enter_password(api_user["password"])
        OrdersFeed(driver).click_order_feed_button()

        count_before = OrdersFeed(driver).get_complate_order_today()

        create_order_and_get_number(api_user["access_token"])

        OrdersFeed(driver).wait_for_today_counter_to_increase(count_before)

        count_after = OrdersFeed(driver).get_complate_order_today()
        assert count_after > count_before, "[Ошибка!] Счётчик заказов не увеличился!"

    def test_order_in_progress_list(self, driver, api_user):
        MainFunctionlity(driver).open_login_form()
        PersonalAccount(driver).enter_email(api_user["email"])
        PersonalAccount(driver).enter_password(api_user["password"])

        OrdersFeed(driver).click_order_feed_button()

        order_number = create_order_and_get_number(api_user["access_token"])
        in_progress_orders = OrdersFeed(driver).wait_for_order_in_progress(order_number)

        assert str(order_number).zfill(7) in in_progress_orders, \
            f"[Ошибка!] Заказ {order_number} не найден в разделе 'В работе'"



