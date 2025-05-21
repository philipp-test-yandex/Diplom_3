from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

def browser_settings(browser_name):
    if browser_name == "chrome":
        options = ChromeOptions()
        options.add_argument("--start-maximized")
        return options
    elif browser_name == "firefox":
        options = FirefoxOptions()
        options.add_argument("--width=1920")
        options.add_argument("--height=1080")
        return options
    else:
        raise ValueError(f"[Ошибка!] Браузер '{browser_name}' не поддерживается")

def get_browser(browser_name):
    if browser_name == "chrome":
        return webdriver.Chrome(options=browser_settings("chrome"))
    elif browser_name == "firefox":
        return webdriver.Firefox(options=browser_settings("firefox"))
    else:
        raise ValueError(f"[Ошибка!] Тип браузера '{browser_name}' не поддерживается")
