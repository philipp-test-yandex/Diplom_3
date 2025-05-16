import allure
from pages.base_page import BasePage
from constants.base_url_constants import *
from locators.orders_feed_locators import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class OrdersFeed(BasePage):

    @allure.step("Открытие страницы ленты заказов по URL")
    def open_feed_page(self):
        self.open_page(FEED_URL)

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
        number_elem = self.wait.until(EC.visibility_of_element_located(ORDER_MODAL_NUMBER))
        order_text = number_elem.text.strip()
        assert order_text.startswith("#"), f"[Ошибка!] Номер заказа должен начинаться с #, но был: {order_text}"
        digits = order_text.lstrip("#")
        assert digits.isdigit() and len(digits) == 7, f"[Ошибка!] Ожидалось 7 цифр после #, но было: {digits}"

    @allure.step("Проверка, что URL содержит хэш заказа")
    def check_url_contains_order_hash(self):
        current_url = self.driver.current_url
        assert "/feed/" in current_url and current_url.split("/feed/")[-1], \
            f"[Ошибка!] URL не содержит хэш заказа: {current_url}"

    @allure.step("Получение номера первого из истории заказа")
    def get_first_order_number(self):
        element = self.wait.until(EC.visibility_of_element_located(ORDER_HISTORY_NUMBER))
        order_text = element.text.strip()
        return order_text

    @allure.step("Проверка, что заказ с номером {order_number} отображается в ленте заказов")
    def check_order_is_in_feed(self, order_number):
        number_to_check = order_number.lstrip("#")
        elements = self.wait.until(EC.presence_of_all_elements_located(ORDER_LIST_ITEMS))
        numbers = [el.text.strip() for el in elements]
        assert number_to_check in numbers, f"[Ошибка!] Заказ {number_to_check} не найден в ленте заказов!"

    @allure.step("Получение общего количества заказов за всё время")
    def get_all_time_order_count(self):
        element = self.wait.until(EC.visibility_of_element_located(ALL_TIME_ORDERS_COUNTER))
        return int(element.text.strip())

    @allure.step("Получение количества заказов за сегодня")
    def get_complate_order_today(self):
        element = self.wait.until(EC.visibility_of_element_located(TODAY_ORDERS_COUNTER))
        return int(element.text.strip())

    @allure.step("Получение номеров заказов в статусе 'В работе'")
    def get_orders_in_progress(self):
        elements = self.wait.until(EC.visibility_of_all_elements_located(IN_PROGRESS_ORDERS))
        return [el.text.strip() for el in elements]

    @allure.step("Ожидание появления заказа {order_number} в списке 'В работе'")
    def wait_for_order_in_progress(self, order_number, timeout=10):
        order_str = str(order_number).zfill(7)

        def order_appears(driver):
            elements = driver.find_elements(*IN_PROGRESS_ORDERS)
            texts = [el.text.strip() for el in elements]

            if "Все текущие заказы готовы!" in texts:
                return False

            return order_str in texts

        WebDriverWait(self.driver, timeout).until(order_appears)

        return self.get_orders_in_progress()

    @allure.step("Ожидание увеличения счётчика заказов за сегодня")
    def wait_for_today_counter_to_increase(self, previous_count, timeout=10):
        def counter_updated(driver):
            current = self.get_complate_order_today()
            return current > previous_count

        WebDriverWait(self.driver, timeout).until(counter_updated)

