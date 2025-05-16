from pages.base_page import BasePage
from constants.base_url_constants import *
from locators.main_functionality_locators import *
from selenium.webdriver.support import expected_conditions as EC
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
        assert self.driver.current_url == BASE_URL, \
            f"[Ошибка!] Ожидался URL страницы конструктора бургера, но был: {self.driver.current_url}"

    @allure.step("Проверить заголовок конструктора")
    def check_header_constructor(self):
        header = self.wait.until(EC.visibility_of_element_located(HEADER_BURGER_CONSTRUCTOR))
        assert header.text == "Соберите бургер", \
            f"[Ошибка!] Ожидался заголовок 'Соберите бургер', но был: '{header.text}'"

    @allure.step("Проверить, что открыта страница ленты заказов")
    def check_on_orders_feed_page(self):
        self.wait_for_url_to_be(ORDERS_FEED_URL)
        assert self.driver.current_url == ORDERS_FEED_URL, \
            f"[Ошибка!] Ожидался URL страницы 'лента заказов', но был: {self.driver.current_url}"

    @allure.step("Проверить заголовок на странице ленты заказов")
    def check_header_orders_feed(self):
        header = self.wait.until(EC.visibility_of_element_located(HEADER_ORDERS_FEED))
        assert header.text == "Лента заказов", \
            f"[Ошибка!] Ожидался заголовок 'Лента заказов', но был: '{header.text}'"

    @allure.step("Клик по первому ингредиенту")
    def click_first_ingredient(self):
        self.click(FIRST_INGREDIENT)

    @allure.step("Проверить, что открылось модальное окно ингредиента")
    def check_ingredient_modal_opened(self):
        header = self.wait.until(EC.visibility_of_element_located(MODAL_HEADER_INGREDIENT))
        assert header.text == "Детали ингредиента", \
            f"[Ошибка!] Ожидался заголовок 'Детали ингредиента', но был: '{header.text}'"


    @allure.step("Закрыть модальное окно ингредиента")
    def click_icon_close(self):
        self.click(MODAL_CLOSE_BUTTON)

    @allure.step("Проверить, что модальное окно закрыто")
    def check_ingredient_modal_closed(self):
        modal = self.driver.find_element(*MODAL_SECTION)
        classes = modal.get_attribute("class")
        assert "Modal_modal_opened__3ISw4" not in classes, \
            "[Ошибка!] Модальное окно не было закрыто"

    @allure.step("Нажать кнопку 'Оформить заказ'")
    def click_confirm_order_button(self):
        self.click(CONFIRM_ORDER_BUTTON)
        self.wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, "div.Modal_modal_opened_3ISw4")))

    @allure.step("Проверить заголовок подтверждения заказа")
    def check_order_confirmation_header(self):
        header = self.wait.until(EC.visibility_of_element_located(HEADER_ORDER_CREATED))
        assert header.text == "Ваш заказ начали готовить", \
            f"[Ошибка!] Ожидался текст 'Ваш заказ начали готовить' но был: '{header.text}'"

    @allure.step("Перетащить первый ингредиент в корзину")
    def drag_and_drop_first_ingredient_to_cart(self):
        ingredient = self.wait.until(EC.visibility_of_element_located(FIRST_INGREDIENT_FOR_DRAG_DROP))
        target = self.wait.until(EC.visibility_of_element_located(DROP_TARGET))
        ActionChains(self.driver).drag_and_drop(ingredient, target).perform()

    @allure.step("Получить текущее значение счётчика ингредиента")
    def get_ingredient_counter_value(self):
        counter = self.wait.until(EC.visibility_of_element_located(INGREDIENT_COUNTER))
        return int(counter.text)



