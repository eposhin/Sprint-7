import generators

class DataForOrder:
    order_data = {
        "firstName": "Evgeniy",
        "lastName": "Poshin",
        "address": "Kirova, 37",
        "metroStation": 4,
        "phone": "+7 999 123 45 67",
        "rentTime": 5,
        "deliveryDate": "2025-06-07",
        "comment": "Call me before deliver"
    }
    scooter_color = [['BLACK'], ['GREY'], (['BLACK'], ['GREY']), ['']]

class DataForRegistration:
    reg_data = [
        {'login': generators.login_generator(),'password': generators.password_generator(), 'firstName': generators.name_generator()}
    ]

class ResponseBody:
    COURIER_CREATION_SUCCESS = {'ok': True}
    COURIER_NAME_ALREADY_EXIST = {'code': 409, 'message': "Этот логин уже используется"}
    COURIER_REGISTRATION_NOT_ENOUGH_DATA = {'code': 400,   "message": "Недостаточно данных для создания учетной записи"}
    COURIER_ACCOUNT_NOT_FOUND = {'code': 404,   "message": "Учетная запись не найдена"}
    COURIER_LOGIN_NOT_ENOUGH_DATA = {'code': 400,   "message":  "Недостаточно данных для входа"}

class Flags:
    SUCCESSFUL_ORDER_CREATION = 'track'
    SUCCESSFUL_GET_ORDER_LIST = 'orders'