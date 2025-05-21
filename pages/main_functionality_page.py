from pages.base_page import BasePage
from constants.base_url_constants import *
from locators.main_functionality_locators import *
from selenium.webdriver.common.action_chains import ActionChains
import allure


class MainFunctionlity(BasePage):
    @allure.step("Открыть форму входа (страницу логина)")
    def open_login_form(self):
        self.open_page(LOGIN_URL)

    @allure.step("Открыть главную страницу сайта")
    def open_main_page(self):
        self.open_page(BASE_URL)

    @allure.step("Нажать кнопку 'Конструктор'")
    def click_constuctor_button(self):
        self.click(CONSTRUCTOR_BUTTON)

    @allure.step("Нажать кнопку 'Лента заказов'")
    def click_orders_feed_button(self):
        self.click(ORDERS_FEED_BUTTON)

    @allure.step("Проверить, что открыта страница конструктора")
    def check_on_constructor_page(self):
        self.wait_for_url_to_be(BASE_URL)
        assert self.get_current_url() == BASE_URL, \
            f"[Ошибка!] Ожидался URL страницы конструктора бургера, но был: {self.get_current_url()}"

    @allure.step("Проверить заголовок конструктора")
    def check_header_constructor(self):
        header_text = self.get_element_text(HEADER_BURGER_CONSTRUCTOR)
        assert header_text == "Соберите бургер", \
            f"[Ошибка!] Ожидался заголовок 'Соберите бургер', но был: '{header_text}'"

    @allure.step("Проверить, что открыта страница ленты заказов")
    def check_on_orders_feed_page(self):
        self.wait_for_url_to_be(ORDERS_FEED_URL)
        assert self.get_current_url() == ORDERS_FEED_URL, \
            f"[Ошибка!] Ожидался URL страницы 'лента заказов', но был: {self.get_current_url()}"

    @allure.step("Проверить заголовок на странице ленты заказов")
    def check_header_orders_feed(self):
        header_text = self.get_element_text(HEADER_ORDERS_FEED)
        assert header_text == "Лента заказов", \
            f"[Ошибка!] Ожидался заголовок 'Лента заказов', но был: '{header_text}'"

    @allure.step("Клик по первому ингредиенту")
    def click_first_ingredient(self):
        self.click(FIRST_INGREDIENT)

    @allure.step("Проверить, что открылось модальное окно ингредиента")
    def check_ingredient_modal_opened(self):
        header_text = self.get_element_text(MODAL_HEADER_INGREDIENT)
        assert header_text == "Детали ингредиента", \
            f"[Ошибка!] Ожидался заголовок 'Детали ингредиента', но был: '{header_text}'"

    @allure.step("Закрыть модальное окно ингредиента")
    def click_icon_close(self):
        self.click(MODAL_CLOSE_BUTTON)

    @allure.step("Проверить, что модальное окно закрыто")
    def check_ingredient_modal_closed(self):
        classes = self.get_element_attribute(MODAL_SECTION, "class")
        assert "Modal_modal_opened__3ISw4" not in classes, \
            "[Ошибка!] Модальное окно не было закрыто"

    @allure.step("Нажать кнопку 'Оформить заказ'")
    def click_confirm_order_button(self):
        self.click(CONFIRM_ORDER_BUTTON)
        self.wait_for_element_visible(HEADER_ORDER_CREATED)

    @allure.step("Проверить заголовок подтверждения заказа")
    def check_order_confirmation_header(self):
        header_text = self.get_element_text(HEADER_ORDER_CREATED)
        assert header_text == "Ваш заказ начали готовить", \
            f"[Ошибка!] Ожидался текст 'Ваш заказ начали готовить' но был: '{header_text}'"

    @allure.step("Перетащить первый ингредиент в корзину")
    def drag_and_drop_first_ingredient_to_cart(self):
        ingredient = self.get_element(FIRST_INGREDIENT_FOR_DRAG_DROP)
        target = self.get_element(DROP_TARGET)
        ActionChains(self.driver).drag_and_drop(ingredient, target).perform()

    @allure.step("Получить текущее значение счётчика ингредиента")
    def get_ingredient_counter_value(self):
        counter_text = self.get_element_text(INGREDIENT_COUNTER)
        return int(counter_text)


    @allure.step("Ввести email")
    def enter_email(self, email):
        self.fill_input(EMAIL_INPUT, email)

    @allure.step("Ввести пароль")
    def enter_password(self, password):
        self.fill_input(PASSWORD_INPUT, password)

    @allure.step("Нажать кнопку 'Войти'")
    def click_login_button(self):
        self.click(LOGIN_BUTTON)

