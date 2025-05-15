import allure
from helpers.helper_file import delete_last_from_dotenv


@allure.title('Тестирование токена aвторизации')
@allure.story('creating an token')
@allure.title('Создание токена авторизации')
@allure.feature('object authorization')
@allure.story('authorization')
def test_create_token_valid(is_token):
    is_token.new_token('SVS_TOKEN')  # создание токена, валидный кейс
    is_token.assert_status_code(200)
    is_token.assert_any_param(param='user', value='SVS_TOKEN')


def test_create_token_with_int_name(is_token):
    is_token.new_token(name=1)  # создание токена с типом данных 'name' int
    is_token.assert_status_code(400)


def test_create_token_with_list_name(is_token):
    is_token.new_token(name=[])  # создание токена с типом данных 'name' list
    is_token.assert_status_code(400)


def test_create_token_with_dict_name(is_token):
    is_token.new_token(name={})  # создание токена с типом данных 'name' dict
    is_token.assert_status_code(400)


def test_create_token_with_none_name(is_token):
    is_token.new_token(name=None)  # создание токена с типом данных 'name' None
    is_token.assert_status_code(400)


def test_create_token_without_name(is_token):
    is_token.missing_parameter(method='post', param='name', token=None)  # создание токена без 'name'
    is_token.assert_status_code(400)


def test_deleting_token(is_token):
    delete_last_from_dotenv('TOKEN')  # удаление тесового токена из файла .env
