from selenium.webdriver.common.by import By

ORDERS_FEED_BUTTON = (By.CSS_SELECTOR, 'a[href="/feed"]')

ORDER_HISTORY_CARD = (By.CSS_SELECTOR, "a.OrderHistory_link__1iNby")

ORDER_MODAL_NUMBER = (By.CSS_SELECTOR, "p.text.text_type_digits-default.mb-10.mt-5")

ORDER_HISTORY_NUMBER = (By.CSS_SELECTOR, "a.OrderHistory_link__1iNby p.text_type_digits-default")

ORDER_LIST_ITEMS = (By.CSS_SELECTOR, "ul.OrderFeed_orderList__cBvyi li")

ALL_TIME_ORDERS_COUNTER = (By.CSS_SELECTOR, "p.OrderFeed_number__2MbrQ")

TODAY_ORDERS_COUNTER = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p")

IN_PROGRESS_ORDERS = (By.CSS_SELECTOR, "ul.OrderFeed_orderListReady__1YFem li")
