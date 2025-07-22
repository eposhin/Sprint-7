import pytest
import requests
import generators
from curl import Url


@pytest. fixture
def create_courier():
    login = generators.login_generator()
    password = generators.password_generator()
    name = generators.name_generator()
    registration_data = {'login': login, 'password': password, 'first_name': name}
    login_data = {'login': login, 'password': password}
    requests.post(f'{Url.MAIN_URL}{Url.CREATE_COURIER}', json=registration_data)
    login_courier = requests.post( f' {Url.MAIN_URL}{Url. COURIER_LOGIN}', json=login_data)
    yield [registration_data, login_data, login, password]
    requests.delete(f'{Url.MAIN_URL}{Url.COURIER_DELETE}{login_courier.json()["id"]}')

@pytest. fixture
def generate_courier_data():
    login = generators.login_generator()
    password = generators.password_generator()
    name = generators.name_generator()
    registration_data = {'login': login, 'password': password, 'first_name': name}
    login_data = {'login': login, 'password': password}
    yield [registration_data, login_data]
    login_courier = requests.post(f'{Url.MAIN_URL}{Url.COURIER_LOGIN}', json=login_data)
    requests.delete(f'{Url.MAIN_URL}{Url.COURIER_DELETE}{login_courier.json()["id"]}')