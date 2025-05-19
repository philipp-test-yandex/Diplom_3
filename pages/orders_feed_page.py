import allure
from pages.base_page import BasePage
from constants.base_url_constants import *
from locators.orders_feed_locators import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import StaleElementReferenceException




class OrdersFeed(BasePage):
    @allure.step("Открытие страницы ленты заказов по URL")
    def open_feed_page(self):
        self.open_page(FEED_URL)

    @allure.step("Открыть форму входа (страницу логина)")
    def open_login_form(self):
        self.open_page(LOGIN_URL)

    @allure.step("Клик по кнопке 'Лента заказов'")
    def click_order_feed_button(self):
        self.wait_for_element_visible(ORDERS_FEED_BUTTON)
        self.click(ORDERS_FEED_BUTTON)

    @allure.step("Клик по карточке заказа в истории")
    def click_order_history_card(self):
        self.wait_for_element_visible(ORDER_HISTORY_CARD)
        self.click(ORDER_HISTORY_CARD)

    @allure.step("Проверка формата номера заказа")
    def check_order_number_format(self):
        number_elem = self.get_visible_element(ORDER_MODAL_NUMBER)
        order_text = number_elem.text.strip()
        assert order_text.startswith("#"), f"[Ошибка!] Номер заказа должен начинаться с #, но был: {order_text}"
        digits = order_text.lstrip("#")
        assert digits.isdigit() and len(digits) == 7, f"[Ошибка!] Ожидалось 7 цифр после #, но было: {digits}"

    @allure.step("Проверка, что URL содержит хэш заказа")
    def check_url_contains_order_hash(self):
        current_url = self.get_current_url()
        assert "/feed/" in current_url and current_url.split("/feed/")[-1], \
            f"[Ошибка!] URL не содержит хэш заказа: {current_url}"

    @allure.step("Получение номера первого из истории заказа")
    def get_first_order_number(self):
        element = self.get_visible_element(ORDER_HISTORY_NUMBER)
        return element.text.strip()

    @allure.step("Проверка, что заказ с номером {order_number} отображается в ленте заказов")
    def check_order_is_in_feed(self, order_number):
        number_to_check = order_number.lstrip("#")
        elements = self.get_all_elements(ORDER_LIST_ITEMS)
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

    @allure.step("Получение количества заказов за сегодня")
    def get_complate_order_today(self):
        element = self.get_visible_element(TODAY_ORDERS_COUNTER)
        return int(element.text.strip())

    @allure.step("Получение номеров заказов в статусе 'В работе'")
    def get_orders_in_progress(self):
        elements = self.get_all_elements(IN_PROGRESS_ORDERS)
        return [el.text.strip() for el in elements]

    @allure.step("Ожидание появления заказа в списке 'В работе'")
    def wait_for_order_in_progress(self, order_number, timeout=10):
        order_str = str(order_number).zfill(7)

        def order_appears(driver):
            try:
                elements = driver.find_elements(*IN_PROGRESS_ORDERS)
                texts = [el.text.strip() for el in elements]
                return order_str in texts and "Все текущие заказы готовы!" not in texts
            except StaleElementReferenceException:
                return False

        self.wait_until(order_appears, timeout)
        return self.get_orders_in_progress()

    @allure.step("Ожидание увеличения счётчика заказов за сегодня")
    def wait_for_today_counter_to_increase(self, previous_count, timeout=10):
        def counter_updated(driver):
            return self.get_complate_order_today() > previous_count

        self.wait_until(counter_updated, timeout)

    @allure.step("Открыть главную страницу сайта")
    def open_main_page(self):
        self.open_page(BASE_URL)

    @allure.step("Клик по кнопке 'Лента заказов'")
    def click_orders_feed_button(self):
        self.click(ORDERS_FEED_BUTTON)

    @allure.step("Закрыть модальное окно заказа после появления реального номера")
    def click_icon_close(self):
        self.wait_for_element_visible(HEADER_ORDER_CREATED)
        self.wait_for_order_number_change()
        self.wait_for_element_visible(MODAL_CLOSE_BUTTON)

        self.click(MODAL_CLOSE_BUTTON)

        self.wait_for_element_invisible(MODAL_CLOSE_BUTTON)

    @allure.step("Ожидание смены номера заказа с '9999' на реальный")
    def wait_for_order_number_change(self, timeout=10):
        self.wait_until(
            lambda d: (text := d.find_element(By.CSS_SELECTOR, "h2.Modal_modal__title__2L34m").text.strip()) != "9999" and text.isdigit(),
            timeout=timeout
        )

    @allure.step("Ожидание исчезновения кнопки закрытия модалки")
    def wait_until_modal_close_button_disappears(self, timeout=10):
        self.wait_until(
            lambda d: not d.find_elements(*MODAL_CLOSE_BUTTON) or not d.find_element(
                *MODAL_CLOSE_BUTTON).is_displayed(),
            timeout=timeout
        )


    @allure.step("Перетащить первый ингредиент в корзину")
    def drag_and_drop_first_ingredient_to_cart(self):
        ingredient = self.get_element(FIRST_INGREDIENT_FOR_DRAG_DROP)
        target = self.get_element(DROP_TARGET)
        ActionChains(self.driver).drag_and_drop(ingredient, target).perform()

    @allure.step("Нажать кнопку 'Оформить заказ'")
    def click_confirm_order_button(self):
        self.click(CONFIRM_ORDER_BUTTON)
        self.wait_for_element_visible(HEADER_ORDER_CREATED)

    @allure.step("Клик по кнопке 'Личный Кабинет'")
    def click_button_personal_account(self):
        self.click(PERSONAL_ACCOUNT_BUTTON)

    @allure.step("Ввести email")
    def enter_email(self, email):
        self.fill_input(EMAIL_INPUT, email)

    @allure.step("Ввести пароль")
    def enter_password(self, password):
        self.fill_input(PASSWORD_INPUT, password)

    @allure.step("Нажать кнопку 'Войти'")
    def click_login_button(self):
        self.click(LOGIN_BUTTON)

    @allure.step("Клик по кнопке 'История заказов'")
    def click_orders_history_button(self):
        self.click(ORDER_HISTORY_BUTTON)
        self.wait_for_element_visible(ORDER_NUMBER_IN_HISTORY)

    @allure.step("Ожидание увеличения счётчика заказов за всё время")
    def wait_for_all_time_counter_to_increase(self, previous_count, timeout=10):
        def counter_updated(driver):
            return self.get_all_time_order_count() > previous_count

        self.wait_until(counter_updated, timeout)




