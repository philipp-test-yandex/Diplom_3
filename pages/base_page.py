from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver, timeout=5):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open_page(self, url):
        self.driver.get(url)

    def click(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def fill_input(self, locator, value):
        input_element = self.wait.until(EC.visibility_of_element_located(locator))
        input_element.clear()
        input_element.send_keys(value)

    def wait_for_url_to_be(self, expected_url):
        self.wait.until(EC.url_to_be(expected_url))

    def wait_for_element_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_for_element_invisible(self, locator):
        return self.wait.until(EC.invisibility_of_element_located(locator))

    def get_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def get_element_text(self, locator):
        return self.wait_for_element_visible(locator).text

    def get_current_url(self):
        return self.driver.current_url

    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    def get_visible_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def get_all_elements(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def wait_until(self, condition, timeout=10):
        return WebDriverWait(self.driver, timeout).until(condition)

    def get_element_attribute(self, locator, attribute):
        return self.get_element(locator).get_attribute(attribute)
