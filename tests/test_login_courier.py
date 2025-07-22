import requests
import allure
import generators
from curl import Url
from data import ResponseBody


class TestLoginCourier:

    @allure.title('Успешный вход курьера с корректными данными. Hendle: /api/v1/courier/login')
    def test_successful_courier_login(self, create_courier):
        response = requests.post(f'{Url.MAIN_URL}{Url.COURIER_LOGIN}', json=create_courier[1])
        courier_id = response.json()
        assert response.status_code == 200 and courier_id != ''

    @allure.title('Вход несуществующего курьера. Hendle: /api/v1/courier/login')
    def test_unregistered_courier_login(self):
        login_data = {'login': generators.login_generator(), 'password': generators.password_generator()}
        response = requests.post(f'{Url.MAIN_URL}{Url.COURIER_LOGIN}', login_data)
        assert response.status_code == 404 and (response.json() == ResponseBody.COURIER_ACCOUNT_NOT_FOUND)

    @allure.title('Вход с пустым паролем. Hendle: /api/v1/courier/login')
    def test_courier_login_empty_password_error(self, create_courier):
        data_response = {'login': create_courier[2], 'password': ''}
        response = requests.post(f'{Url.MAIN_URL}{Url.COURIER_LOGIN}', json=data_response)
        assert response.status_code == 400 and (response.json() == ResponseBody.COURIER_LOGIN_NOT_ENOUGH_DATA)

    @allure.title('Вход с пустым логином. Hendle: /api/v1/courier/login')
    def test_courier_login_empty_login_error(self, create_courier):
        data_response = {'login': '', 'password': create_courier[2]}
        response = requests.post(f'{Url.MAIN_URL}{Url.COURIER_LOGIN}', json=data_response)
        assert response.status_code == 400 and (response.json() == ResponseBody.COURIER_LOGIN_NOT_ENOUGH_DATA)