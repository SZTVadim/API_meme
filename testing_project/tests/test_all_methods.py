import pytest
import allure

from testing_project.endpoints.authorization_endpoint import TokenAuthorize
from testing_project.helpers.helper_file import delete_last_from_dotenv


@allure.title('Создание мема')
@allure.feature('object manipulation')
@allure.story('creating an object')
@pytest.mark.parametrize("token", [("SVS_Token", "TOKEN")], indirect=True)
def test_creation(token, create_meme, delete_meme):
    create_meme.new_meme(text='test', tags='tags', info='info', token=token,
                         url='url')  # Позитивный кейс
    create_meme.assert_any_param(param='text', value='test')
    create_meme.assert_any_param(param='tags', value='tags')
    create_meme.assert_any_param(param='info', value='info')
    create_meme.assert_any_param(param='url', value='url')
    create_meme.assert_status_code(200)
    delete_meme.deleting_meme(id_meme=create_meme.meme_id, token=token)
    create_meme.new_meme(text='', tags='tags', info='info', token=token,
                         url='url')
    create_meme.assert_status_code(200)
    delete_meme.deleting_meme(id_meme=create_meme.meme_id, token=token)
    create_meme.new_meme(text='Test', tags='tags', info='info', token='',
                         url='url')  # без токена авторизации
    create_meme.assert_status_code(401)

    create_meme.missing_parameter(method='post', param='text', token=token)  # без параметра "text"
    create_meme.assert_status_code(400)

    create_meme.new_meme(text=1, tags='tags', info='info', token=token,
                         url='url')  # тип данных "text" int
    create_meme.assert_status_code(400)

    create_meme.new_meme(text=[], tags='tags', info='info', token=token,
                         url='url')  # тип данных "text" list
    create_meme.assert_status_code(400)

    create_meme.new_meme(text={}, tags='tags', info='info', token=token,
                         url='url')  # тип данных "text" dict
    create_meme.assert_status_code(400)

    create_meme.new_meme(text=None, tags='tags', info='info', token=token,
                         url='url')  # значение параметра "text" None
    create_meme.assert_status_code(400)

    create_meme.missing_parameter(method='post', param='url', token=token)  # без параметра "url"
    create_meme.assert_status_code(400)

    create_meme.new_meme(text='text', tags='tags', info='info', token=token,
                         url='')  # пустое значение "url"
    create_meme.assert_status_code(200)
    delete_meme.deleting_meme(id_meme=create_meme.meme_id, token=token)

    create_meme.new_meme(text='text', tags='tags', info='info', token=token,
                         url=1)  # тип данных "url" int
    create_meme.assert_status_code(400)

    create_meme.new_meme(text='text', tags='tags', info='info', token=token,
                         url=[])  # тип данных "url" list
    create_meme.assert_status_code(400)

    create_meme.new_meme(text='text', info='info', token=token, url={},
                         tags='tags')  # тип данных "url" dict
    create_meme.assert_status_code(400)

    create_meme.new_meme(text='text', info='info', token=token, url=None,
                         tags='tags')  # значение параметра "url" None
    create_meme.assert_status_code(400)

    create_meme.missing_parameter(method='post', param='tags', token=token)  # без параметра "tags"
    create_meme.assert_status_code(400)

    create_meme.new_meme(text='Text', tags='', info='', url='Url', token=token)  # пустое значение "tags"
    create_meme.assert_status_code(200)
    delete_meme.deleting_meme(id_meme=create_meme.meme_id, token=token)

    create_meme.replace_body_parameter(method='post', param='tags', value='', token=token)  # тип данных "tags" str
    create_meme.assert_status_code(400)

    create_meme.replace_body_parameter(method='post', param='tags', value=1, token=token)  # тип данных "tags" int
    create_meme.assert_status_code(400)

    create_meme.replace_body_parameter(method='post', param='tags', value={},
                                       token=token)  # тип данных "tags" dict
    create_meme.assert_status_code(400)

    create_meme.replace_body_parameter(method='post', param='tags', value=None,
                                       token=token)  # значение параметра "tags" None
    create_meme.assert_status_code(400)

    create_meme.missing_parameter(method='post', param='info', token=token)  # без параметра "info"
    create_meme.assert_status_code(400)

    create_meme.new_meme(text='Text', tags='Tags', info='', url='Url', token=token)  # пустое значение "info"
    create_meme.assert_status_code(200)
    delete_meme.deleting_meme(id_meme=create_meme.meme_id, token=token)

    create_meme.replace_body_parameter(method='post', param='info', value='info',
                                       token=token)  # тип данных "info" str
    create_meme.assert_status_code(400)

    create_meme.replace_body_parameter(method='post', param='info', value=1, token=token)  # тип данных "info" int
    create_meme.assert_status_code(400)

    create_meme.replace_body_parameter(method='post', param='info', value=[],
                                       token=token)  # тип данных "info" list
    create_meme.assert_status_code(400)

    create_meme.replace_body_parameter(method='post', param='info', value=None,
                                       token=token)  # значение параметра "info" None
    create_meme.assert_status_code(400)


@allure.title('Обновление мема')
@allure.feature('object manipulation')
@allure.story('full changing an object')
@pytest.mark.parametrize("token", [("SVS_Token", "TOKEN")], indirect=True)
def test_updating(meme_id, update_meme, token):
    update_meme.updating_meme(id_meme=meme_id, text='TEXT', tags='TAGS', info='INFO',
                              token=token, url='URL')  # Позитивный кейс
    update_meme.assert_any_param(param='text', value='TEXT')
    update_meme.assert_any_param(param='tags', value='TAGS')
    update_meme.assert_any_param(param='info', value='INFO')
    update_meme.assert_any_param(param='url', value='URL')
    update_meme.assert_status_code(200)
    update_meme.updating_meme(id_meme=meme_id, text='TEXT', tags='TAGS', info='INFO',
                              token="xxx", url='URL')  # без авторизации
    update_meme.assert_status_code(401)

    update_meme.updating_meme(id_meme='', text='TEXT', tags='TAGS', info='INFO',
                              token=token,
                              url='URL')  # тип данных "id" str
    update_meme.assert_status_code(404)

    update_meme.updating_meme(id_meme=None, text='TEXT', tags='TAGS', info='INFO',
                              token=token, url='URL')  # тип данных "id" None
    update_meme.assert_status_code(404)
    update_meme.updating_meme(id_meme=meme_id, text='', tags='TAGS', info='INFO',
                              token=token, url='URL')  # пустое значение "text"
    update_meme.assert_status_code(200)

    update_meme.missing_parameter(method='put', param='text', token=token)  # без параметра "text"
    update_meme.assert_status_code(400)

    update_meme.updating_meme(id_meme=meme_id, text=1, tags='TAGS', info='INFO',
                              token=token, url='URL')  # тип данных "text" int
    update_meme.assert_status_code(400)

    update_meme.updating_meme(id_meme=meme_id, text=[], tags='TAGS', info='INFO',
                              token=token, url='URL')  # тип данных "text" list
    update_meme.assert_status_code(400)

    update_meme.updating_meme(id_meme=meme_id, text={}, tags='TAGS', info='INFO',
                              token=token, url='URL')  # тип данных "text" dict
    update_meme.assert_status_code(400)

    update_meme.updating_meme(id_meme=meme_id, text=None, tags='TAGS', info='INFO',
                              token=token, url='URL')  # значение "text" None
    update_meme.assert_status_code(400)

    update_meme.updating_meme(id_meme=meme_id, text='TEXT', tags='TAGS', info='INFO',
                              token=token, url='')  # пустое значение "url"
    update_meme.assert_status_code(200)

    update_meme.missing_parameter(method='put', param='url', token=token)  # без параметра "url"
    update_meme.assert_status_code(400)

    update_meme.updating_meme(id_meme=meme_id, text='TEXT', tags='TAGS', info='INFO',
                              token=token, url=1)  # тип данных "url" int
    update_meme.assert_status_code(400)

    update_meme.updating_meme(id_meme=meme_id, text='TEXT', tags='TAGS', info='INFO',
                              token=token, url=['URL'])  # тип данных "url" list
    update_meme.assert_status_code(400)

    update_meme.updating_meme(id_meme=meme_id, text='TEXT', tags='TAGS', info='INFO',
                              token=token, url={1: 1})  # тип данных "url" dict
    update_meme.assert_status_code(400)

    update_meme.updating_meme(id_meme=meme_id, text='TEXT', tags='TAGS', info='INFO',
                              token=token, url=None)  # значение "url" None
    update_meme.assert_status_code(400)

    update_meme.updating_meme(id_meme=meme_id, text='TEXT', tags='', info='INFO',
                              token=token, url='URL')  # пустое значение "tags"
    update_meme.assert_status_code(200)
    #
    update_meme.missing_parameter(method='put', param='tags', token=token)  # без параметра "tags"
    update_meme.assert_status_code(400)

    update_meme.replace_body_parameter(method='put', param='tags', value='STR', token=token,
                                       id_meme=meme_id)  # тип данных "tags" str
    update_meme.assert_status_code(400)

    update_meme.replace_body_parameter(method='put', param='tags', value=13, token=token,
                                       id_meme=meme_id)  # тип данных "tags" int
    update_meme.assert_status_code(400)

    update_meme.replace_body_parameter(method='put', param='tags', value={'param': 'TAGS'}, token=token,
                                       id_meme=meme_id)  # тип данных "tags" dict
    update_meme.assert_status_code(400)

    update_meme.replace_body_parameter(method='put', param='tags', value=None, token=token,
                                       id_meme=meme_id)  # значение "tags" None
    update_meme.assert_status_code(400)

    update_meme.updating_meme(id_meme=meme_id, text='TEXT', tags='TAGS', info='',
                              token=token, url='URL')  # пустое значение "info"
    update_meme.assert_status_code(200)

    update_meme.missing_parameter(method='put', param='info', token=token)  # без параметра "info"
    update_meme.assert_status_code(400)

    update_meme.replace_body_parameter(method='put', param='info', value='STR', token=token,
                                       id_meme=meme_id)  # тип данных "info" str
    update_meme.assert_status_code(400)

    update_meme.replace_body_parameter(method='put', param='info', value=13, token=token,
                                       id_meme=meme_id)  # тип данных "info" int
    update_meme.assert_status_code(400)

    update_meme.replace_body_parameter(method='put', param='info', value=['LIST'], token=token,
                                       id_meme=meme_id)  # тип данных "info" list
    update_meme.assert_status_code(400)

    update_meme.replace_body_parameter(method='put', param='info', value=None, token=token,
                                       id_meme=meme_id)  # значение "info" None
    update_meme.assert_status_code(400)


@allure.title('Получение мема')
@allure.feature('getting information')
@allure.story('get an object')
@pytest.mark.parametrize("token", [("SVS_Token", "TOKEN")], indirect=True)
def test_mathod_get(token, get_meme, meme_id):
    get_meme.get_all_meme(token=token)  # позитивный кейс, все мемы
    get_meme.assert_status_code(200)
    get_meme.assert_get_all()

    get_meme.get_one_meme(id_meme=meme_id, token=token)
    get_meme.assert_status_code(200)
    get_meme.assert_any_param(param='id', value=meme_id)

    get_meme.get_one_meme(id_meme=meme_id, token='xxx')
    get_meme.assert_status_code(401)


@allure.title('Удаление мема')
@allure.feature('object manipulation')
@allure.story('deleting an object')
@pytest.mark.parametrize("token", [("SVS_Token", "TOKEN")], indirect=True)
def test_deleting(token, delete_meme, get_meme, create_meme):
    mem_id = create_meme.new_meme(text='test', tags='tags', info='info', token=token,
                                  url='url')
    delete_meme.deleting_meme(id_meme=mem_id, token=token)  # позитивный кейс
    delete_meme.assert_status_code(200)
    delete_meme.deleting_meme(id_meme=mem_id, token='xxx')  # Удаление без авторизации
    delete_meme.assert_status_code(401)
    get_meme.get_one_meme(id_meme=mem_id, token=token)
    get_meme.assert_status_code(404)  # проверяем 404 статус при запросе удаленного мема


@allure.title('Создание токена авторизации')
@allure.feature('object authorization')
@allure.story('authorization')
def test_authorization():
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
