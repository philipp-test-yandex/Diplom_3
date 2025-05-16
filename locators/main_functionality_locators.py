from selenium.webdriver.common.by import By

CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']/ancestor::a[@href='/']")

HEADER_BURGER_CONSTRUCTOR = (By.XPATH, "//h1[text()='Соберите бургер']")

ORDERS_FEED_BUTTON = (By.XPATH, "//p[text()='Лента Заказов']/ancestor::a")

HEADER_ORDERS_FEED = (By.XPATH, "//h1[text()='Лента заказов']")

FIRST_INGREDIENT = (By.XPATH, "//div[contains(@class, 'BurgerIngredient_ingredient__priceBox')]")

MODAL_HEADER_INGREDIENT = (By.XPATH, "//h2[text()='Детали ингредиента']")

MODAL_CLOSE_BUTTON = (By.XPATH, "//button[contains(@class, 'modal__close')]")

HEAFER_ORDER_STARTED_COOK = (By.XPATH, "//p[contains(text(), 'Ваш заказ начали готовить')]")

MODAL_SECTION = (By.CLASS_NAME, "Modal_modal__P3_V5")

ORDER_COUNTER = (By.XPATH, "//div[contains(@class, 'basket')]/p")

CONFIRM_ORDER_BUTTON = (By.XPATH, '//button[text()="Оформить заказ"]')

HEADER_ORDER_CREATED = (By.XPATH, '//p[text()="Ваш заказ начали готовить"]')


FIRST_INGREDIENT_FOR_DRAG_DROP = (By.CSS_SELECTOR, 'a[href^="/ingredient/"]')

DROP_TARGET = (By.CSS_SELECTOR, '.BurgerConstructor_basket__list__l9dp_')
INGREDIENT_COUNTER = (By.CSS_SELECTOR, '.counter_counter__num__3nue1')

MODAL_OVERLAY = (By.CLASS_NAME, "Modal_modal_overlay__x2ZCr")

MODAL_TICK_IMAGE = (By.CLASS_NAME, "Modal_modal__image__2nh17")

