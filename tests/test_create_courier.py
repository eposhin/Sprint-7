import requests
import pytest
import allure
from data import ResponseBody, DataForRegistration
from curl import Url

class TestsCreateNewCourier:

    @allure.title('Тест успешное создание нового курьера. Handle: /api/v1/courier')
    def test_creation_courier_success(self, generate_courier_data):
        registration = requests.post(f'{Url.MAIN_URL}{Url.CREATE_COURIER}', json=generate_courier_data[0])
        assert registration.status_code == 201 and (registration.json() == ResponseBody.COURIER_CREATION_SUCCESS)

    @allure.title('Тест нельзя создать двух одинаковых курьеров. Handle: /api/v1/courier')
    def test_creation_courier_clone_error(self, generate_courier_data):
        response = requests.post(f'{Url.MAIN_URL}{Url.CREATE_COURIER}', json=generate_courier_data[0])
        assert response.status_code == 409 and (response.json() == ResponseBody.COURIER_NAME_ALREADY_EXIST)

    @allure.title('Тест с недостающими данными при регистрации курьера - пропущен логин или пароль. Handle: /api/v1/courier')
    @pytest.mark.parametrize('data_setup', DataForRegistration.reg_data)
    def test_creation_courier_deficit_data_error(self, data_setup):
        response = requests.post(f'{Url.MAIN_URL}{Url.CREATE_COURIER}',data_setup)
        assert response.status_code == 400 and (response.json() == ResponseBody.COURIER_REGISTRATION_NOT_ENOUGH_DATA)