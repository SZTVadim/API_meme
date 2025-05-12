import allure

from testing_project.endpoints.authorization_endpoint import TokenAuthorize
from testing_project.helpers.helper_file import delete_last_from_dotenv


@allure.title('Создание мема')
@allure.feature('object manipulation')
@allure.story('creating an object')
@allure.title('Создание токена авторизации')
@allure.feature('object authorization')
@allure.story('authorization')
def test_token_authorization():
    token = TokenAuthorize()
    token.new_token('SVS_TOKEN')  # создание токена, валидный кейс
    token.assert_status_code(200)
    token.assert_any_param(param='user', value='SVS_TOKEN')

    token.validate_token(token.token)  # проверка, работает ли токен
    token.assert_status_code(200)

    token.new_token(name=1)  # создание токена с типом данных 'name' int
    token.assert_status_code(400)

    token.new_token(name=[])  # создание токена с типом данных 'name' list
    token.assert_status_code(400)

    token.new_token(name={})  # создание токена с типом данных 'name' dict
    token.assert_status_code(400)

    token.new_token(name=None)  # создание токена с типом данных 'name' None
    token.assert_status_code(400)

    token.missing_parameter(method='post', param='name', token=None)  # создание токена без 'name'
    token.assert_status_code(400)

    delete_last_from_dotenv('TOKEN')  # удаление тесового токена из файла .env
