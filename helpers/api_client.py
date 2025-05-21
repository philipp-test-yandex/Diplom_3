import requests
from locators.api_urls import *
import allure


@allure.step("Регистрация пользователя")
def register_user(user_data):
    return requests.post(REGISTER_NEW_USER, json=user_data)

@allure.step("Логин пользователя")
def login_user(user_data):
    return requests.post(AUTH_USER, json=user_data)

@allure.step("Удаление пользователя с токеном")
def delete_user(access_token):
    headers = {"Authorization": access_token}
    return requests.delete(DELETE_USER, headers=headers)

@allure.step("Создание заказа и получение номера")
def create_order_and_get_number(token: str):
    headers = {"Authorization": token}
    ingredient_ids = ['61c0c5a71d1f82001bdaaa6c']
    body = {"ingredients": ingredient_ids}

    response = requests.post(CREATE_ORDER, json=body, headers=headers)
    response.raise_for_status()
    data = response.json()
    return data["order"]["number"]

