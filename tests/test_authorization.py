import allure
import pytest

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


@pytest.mark.parametrize('value', [1, [], {}, None],
                         ids=['name is int', 'name is list', 'name is dict', 'name is None'])
def test_create_token_with_int_name(is_token, value):
    is_token.new_token(name=value)  # создание токена с типом данных 'name' int
    is_token.assert_status_code(400)
