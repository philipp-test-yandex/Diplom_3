import pytest
import allure
from selenium import webdriver
from helpers.data import generate_user_data
from helpers.api_client import register_user, delete_user, login_user
from helpers.browser_utils import get_browser


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    browser = get_browser(request.param)
    browser.implicitly_wait(5)
    yield browser
    browser.quit()



@pytest.fixture
def api_user():
    user_data = generate_user_data()

    with allure.step("Регистрация нового пользователя"):
        register_resp = register_user(user_data)
        assert register_resp.status_code == 200

    with allure.step("Логин нового пользователя"):
        login_resp = login_user(user_data)
        assert login_resp.status_code == 200

        access_token = login_resp.json()["accessToken"]
        user_data["access_token"] = access_token

    yield user_data

    with allure.step("Удаление пользователя"):
        delete_resp = delete_user(access_token)
        assert delete_resp.status_code == 202
