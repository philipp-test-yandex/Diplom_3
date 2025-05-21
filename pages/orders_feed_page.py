import allure
from pages.base_page import BasePage
from constants.base_url_constants import *
from locators.orders_feed_locators import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import StaleElementReferenceException


class OrdersFeed(BasePage):
    @allure.step("Открыть главную страницу сайта")
    def open_main_page(self):
        self.open_page(BASE_URL)

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

    @allure.step("Авторизоваться юзера")
    def auth_user_on_login_page(self, user_data):
        self.enter_email(user_data["email"])
        self.enter_password(user_data["password"])
        self.click_login_button()
        self.get_visible_element(CONFIRM_ORDER_BUTTON)

    @allure.step("Клик по кнопке 'Лента заказов'")
    def click_order_feed_button(self):
        self.wait_for_element_visible(ORDERS_FEED_BUTTON)
        self.click(ORDERS_FEED_BUTTON)
        self.wait_for_element_visible(HEADER_ON_PAGE_FEED_ORDER)

    @allure.step("Клик по первому заказу в ленте")
    def click_first_order_card(self):
        self.get_all_elements(FIRST_CARD_IN_FEED_LIST)
        self.click(FIRST_CARD_IN_FEED_LIST)
        self.wait_for_element_visible(HEADER_IN_MODAL_OF_FEED_ORDER)

    @allure.step("Перетащить первый ингредиент в корзину и проверить, что сумма заказа увеличилась")
    def drag_and_drop_ingredient_and_check_price_increased(self):
        previous_price = self.get_order_total_price()
        self.drag_and_drop_first_ingredient_to_cart()
        self.check_order_price_increased(previous_price)

    @allure.step("Перетащить первый ингредиент в корзину")
    def drag_and_drop_first_ingredient_to_cart(self):
        ingredient = self.get_element(UNIVERS_FIRST_INGREDIENT_FOR_DRAG_DROP)
        target = self.get_element(DROP_TARGET)
        ActionChains(self.driver).drag_and_drop(ingredient, target).perform()

    @allure.step("Получить текущую сумму заказа")
    def get_order_total_price(self):
        price_text = self.get_element_text(ORDER_PRICE_TOTAL_ON_MAIN_PAGE)
        return int(price_text)

    @allure.step("Проверка, что сумма заказа увеличилась")
    def check_order_price_increased(self, previous_price):
        current_price = self.get_order_total_price()
        assert current_price > previous_price, (
            f"[Ошибка!] Сумма заказа не увеличилась: была {previous_price}, стала {current_price}")

    @allure.step("Проверка, что модальное окно заказа отображается")
    def check_order_modal_is_opened(self):
        order_number_in_modal = self.wait_for_element_visible(ORDER_NUMBER_IN_MODAL)
        assert order_number_in_modal.is_displayed(), "[Ошибка!] Номер заказа в модальном окне не отображается!"

    @allure.step("Нажать кнопку 'Оформить заказ'")
    def click_confirm_order_button(self):
        self.click(CONFIRM_ORDER_BUTTON)

    @allure.step("Ожидание, пока номер заказа станет отличным от '9999'")
    def wait_for_real_order_number(self, timeout=15):
        def number_is_real(_):
            number_text = self.get_element_text_if_present(HEADER_ORDER_CREATED)
            return number_text.isdigit() and number_text != "9999"

        self.wait_until(number_is_real, timeout=timeout)

    @allure.step("Закрыть модальное окно заказа")
    def click_icon_close(self):
        self.click(MODAL_CLOSE_BUTTON)

    @allure.step("Клик по кнопке 'История заказов'")
    def click_orders_history_button(self):
        self.click(ORDER_HISTORY_BUTTON)
        self.wait_for_element_visible(ORDER_NUMBER_IN_HISTORY)

    @allure.step("Получение номера первого из истории заказа")
    def get_first_order_number(self):
        element = self.get_visible_element(ORDER_HISTORY_NUMBER)
        return element.text.strip()

    @allure.step("Проверка, что заказ с номером {order_number} отображается в ленте заказов")
    def check_order_is_in_feed(self, order_number):
        number_to_check = order_number.lstrip("#")
        self.get_all_elements(ORDER_LIST_ITEMS)
        numbers = [
            el.text.strip()
            for el in self.get_all_elements(ORDER_LIST_ITEMS)
            if el.text.strip()
        ]
        assert number_to_check in numbers, f"[Ошибка!] Заказ {number_to_check} не найден в ленте заказов!"

    @allure.step("Получение общего количества заказов за всё время")
    def get_all_time_order_count(self):
        element = self.get_visible_element(ALL_TIME_ORDERS_COUNTER)
        return int(element.text.strip())

    @allure.step("Ожидание увеличения общего счётчика заказов")
    def wait_for_all_time_counter_to_increase(self, previous_count, timeout=10):
        self.wait_until(
            lambda _: self.get_all_time_order_count() > previous_count,
            timeout=timeout
        )

    @allure.step("Получение количества заказов за сегодня")
    def get_complate_order_today(self):
        element = self.get_visible_element(TODAY_ORDERS_COUNTER)
        return int(element.text.strip())

    @allure.step("Ожидание увеличения счётчика заказов за сегодня")
    def wait_for_today_counter_to_increase(self, previous_count, timeout=10):
        self.wait_until(
            lambda _: self.get_complate_order_today() > previous_count,
            timeout=timeout
        )

    @allure.step("Получение номеров заказов в статусе 'В работе'")
    def get_orders_in_progress(self):
        elements = self.get_all_elements(IN_PROGRESS_ORDERS)
        return [el.text.strip() for el in elements]

    @allure.step("Ожидание появления заказа в списке 'В работе'")
    def wait_for_order_in_progress(self, order_number, timeout=10):
        order_str = str(order_number).zfill(7)

        self.wait_until(
            lambda _: order_str in [el.text.strip() for el in self.find_elements(IN_PROGRESS_ORDERS)],
            timeout=timeout
        )
        return self.get_orders_in_progress()




