import allure
import pytest
import requests
from data import DataForOrder
from data import Flags
from curl import Url

class TestCreationOrder:

    @allure.title('Успешное создание заказа во всех цветовых вариациях. Handle:/api/v1/order')
    @pytest.mark.parametrize('scooter_color', DataForOrder.scooter_color)
    def test_create_order_with_diff_colors(self, scooter_color):
        order_data = DataForOrder.order_data
        order_data['color'] = scooter_color
        order = requests.post(f'{Url.MAIN_URL}{Url.CREATE_ORDER}', json=order_data)
        assert order.status_code == 201 and Flags.SUCCESSFUL_ORDER_CREATION in order.json()
        requests.put(f'{Url.MAIN_URL}{Url.ORDER_CANCEL}{order.json()['track']}')