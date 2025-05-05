from final_project.Endpoints.token_authorize import TokenAuthorize
from final_project.helpers.helpers import delete_from_dotenv
import allure


@allure.title('Создание токена авторизации')
@allure.feature('object authorization')
@allure.story('authorization')
def token_testing(token_name):
    obj = TokenAuthorize()
    obj.new_token(token_name)  # создание токена, валидный кейс
    obj.assert_status_code(200)
    obj.assert_any_param(param='user', value=token_name)

    obj.validate_token(obj.token)  # проверка, работает ли токен
    obj.assert_status_code(200)

    obj.new_token(name=1)  # создание токена с типом данных 'name' int
    obj.assert_status_code(400)

    obj.new_token(name=[])  # создание токена с типом данных 'name' list
    obj.assert_status_code(400)

    obj.new_token(name={})  # создание токена с типом данных 'name' dict
    obj.assert_status_code(400)

    obj.new_token(name=None)  # создание токена с типом данных 'name' None
    obj.assert_status_code(400)

    obj.delete_params(method='post', param='name', token=None)  # создание токена без 'name'
    obj.assert_status_code(400)

    delete_from_dotenv('TOKEN')  # удаляет тестовый токен из файла .env
