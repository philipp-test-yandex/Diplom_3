from selenium.webdriver.common.by import By

ORDERS_FEED_BUTTON = (By.CSS_SELECTOR, 'a[href="/feed"]')

ORDER_HISTORY_CARD = (By.CSS_SELECTOR, "a.OrderHistory_link__1iNby")

ORDER_MODAL_NUMBER = (By.CSS_SELECTOR, "p.text.text_type_digits-default.mb-10.mt-5")

ORDER_HISTORY_NUMBER = (By.CSS_SELECTOR, "a.OrderHistory_link__1iNby p.text_type_digits-default")

ORDER_LIST_ITEMS = (By.CSS_SELECTOR, "ul.OrderFeed_orderList__cBvyi li")

ALL_TIME_ORDERS_COUNTER = (By.CSS_SELECTOR, "p.OrderFeed_number__2MbrQ")

TODAY_ORDERS_COUNTER = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p")

IN_PROGRESS_ORDERS = (By.CSS_SELECTOR, "ul.OrderFeed_orderListReady__1YFem li")

MODAL_CLOSE_BUTTON = (By.CSS_SELECTOR, "button.Modal_modal__close__TnseK")

FIRST_INGREDIENT_FOR_DRAG_DROP = (By.CSS_SELECTOR, 'a[href^="/ingredient/"]')
DROP_TARGET = (By.CSS_SELECTOR, '.BurgerConstructor_basket__list__l9dp_')
CONFIRM_ORDER_BUTTON = (By.XPATH, '//button[text()="Оформить заказ"]')
HEADER_ORDER_CREATED = (By.XPATH, '//p[text()="Ваш заказ начали готовить"]')
PERSONAL_ACCOUNT_BUTTON = (By.LINK_TEXT, "Личный Кабинет")

EMAIL_INPUT = (By.NAME, "name")
PASSWORD_INPUT = (By.NAME, "Пароль")
LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")
ORDER_HISTORY_BUTTON = (By.XPATH, "//a[@href='/account/order-history' and text()='История заказов']")
ORDER_NUMBER_IN_HISTORY = (By.CSS_SELECTOR, "p.text.text_type_digits-default")
MODAL_OVERLAY = (By.CLASS_NAME, "Modal_modal_overlay__x2ZCr")

MODAL_SECTION = (By.CLASS_NAME, "Modal_modal__P3_V5")

MODAL_CONTAINER = (By.CLASS_NAME, "Modal_modal__container__Wo2l_")

ORDER_NUMBER_TITLE = (By.CSS_SELECTOR, "h2.Modal_modal__title__2L34m")


