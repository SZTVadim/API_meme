import pytest
import allure
from final_project.helpers.helpers import delete_last_from_dotenv


@allure.title('Создание мема')
@allure.feature('object manipulation')
@allure.story('creating an object')
@pytest.mark.parametrize("only_token", [("SVS_Token", "TOKEN")], indirect=True)
def test_post(only_token, create_meme, delete_meme):
    create_meme.new_meme(text='test', tags='tags', info='info', token=only_token,
                         url='url')  # Позитивный кейс
    create_meme.assert_any_param(param='text', value='test')
    create_meme.assert_any_param(param='tags', value='tags')
    create_meme.assert_any_param(param='info', value='info')
    create_meme.assert_any_param(param='url', value='url')
    create_meme.assert_status_code(200)
    delete_meme.deleting_meme(id_meme=create_meme.meme_id, token=only_token)
    create_meme.new_meme(text='', tags='tags', info='info', token=only_token,
                         url='url')
    create_meme.assert_status_code(200)
    delete_meme.deleting_meme(id_meme=create_meme.meme_id, token=only_token)

    create_meme.new_meme(text='Test', tags='tags', info='info', token='',
                         url='url')  # без токена авторизации
    create_meme.assert_status_code(401)

    create_meme.missing_parameter(method='post', param='text', token=only_token)  # без параметра "text"
    create_meme.assert_status_code(400)

    create_meme.new_meme(text=1, tags='tags', info='info', token=only_token,
                         url='url')  # тип данных "text" int
    create_meme.assert_status_code(400)

    create_meme.new_meme(text=[], tags='tags', info='info', token=only_token,
                         url='url')  # тип данных "text" list
    create_meme.assert_status_code(400)

    create_meme.new_meme(text={}, tags='tags', info='info', token=only_token,
                         url='url')  # тип данных "text" dict
    create_meme.assert_status_code(400)

    create_meme.new_meme(text=None, tags='tags', info='info', token=only_token,
                         url='url')  # значение параметра "text" None
    create_meme.assert_status_code(400)

    create_meme.missing_parameter(method='post', param='url', token=only_token)  # без параметра "url"
    create_meme.assert_status_code(400)

    create_meme.new_meme(text='text', tags='tags', info='info', token=only_token,
                         url='')  # пустое значение "url"
    create_meme.assert_status_code(200)
    delete_meme.deleting_meme(id_meme=create_meme.meme_id, token=only_token)

    create_meme.new_meme(text='text', tags='tags', info='info', token=only_token,
                         url=1)  # тип данных "url" int
    create_meme.assert_status_code(400)

    create_meme.new_meme(text='text', tags='tags', info='info', token=only_token,
                         url=[])  # тип данных "url" list
    create_meme.assert_status_code(400)

    create_meme.new_meme(text='text', info='info', token=only_token, url={},
                         tags='tags')  # тип данных "url" dict
    create_meme.assert_status_code(400)

    create_meme.new_meme(text='text', info='info', token=only_token, url=None,
                         tags='tags')  # значение параметра "url" None
    create_meme.assert_status_code(400)

    create_meme.missing_parameter(method='post', param='tags', token=only_token)  # без параметра "tags"
    create_meme.assert_status_code(400)

    create_meme.new_meme(text='Text', tags='', info='', url='Url', token=only_token)  # пустое значение "tags"
    create_meme.assert_status_code(200)

    create_meme.replace_body_parameter(method='post', param='tags', value='', token=only_token)  # тип данных "tags" str
    create_meme.assert_status_code(400)

    create_meme.replace_body_parameter(method='post', param='tags', value=1, token=only_token)  # тип данных "tags" int
    create_meme.assert_status_code(400)

    create_meme.replace_body_parameter(method='post', param='tags', value={},
                                       token=only_token)  # тип данных "tags" dict
    create_meme.assert_status_code(400)

    create_meme.replace_body_parameter(method='post', param='tags', value=None,
                                       token=only_token)  # значение параметра "tags" None
    create_meme.assert_status_code(400)

    create_meme.missing_parameter(method='post', param='info', token=only_token)  # без параметра "info"
    create_meme.assert_status_code(400)

    create_meme.new_meme(text='Text', tags='Tags', info='', url='Url', token=only_token)  # пустое значение "info"
    create_meme.assert_status_code(200)
    delete_meme.deleting_meme(id_meme=create_meme.meme_id, token=only_token)

    create_meme.replace_body_parameter(method='post', param='info', value='info',
                                       token=only_token)  # тип данных "info" str
    create_meme.assert_status_code(400)

    create_meme.replace_body_parameter(method='post', param='info', value=1, token=only_token)  # тип данных "info" int
    create_meme.assert_status_code(400)

    create_meme.replace_body_parameter(method='post', param='info', value=[],
                                       token=only_token)  # тип данных "info" list
    create_meme.assert_status_code(400)

    create_meme.replace_body_parameter(method='post', param='info', value=None,
                                       token=only_token)  # значение параметра "info" None
    create_meme.assert_status_code(400)


@allure.title('Обновление мема')
@allure.feature('object manipulation')
@allure.story('full changing an object')
@pytest.mark.parametrize("setup_teardown", [("SVS_Token", "TOKEN")], indirect=True)
def test_sute_put(setup_teardown, update_meme):
    update_meme.updating_meme(id_meme=setup_teardown.meme_id, text='TEXT', tags='TAGS', info='INFO',
                              token=setup_teardown.token, url='URL')  # Позитивный кейс
    update_meme.assert_any_param(param='id', value=update_meme.meme_id)
    update_meme.assert_any_param(param='text', value='TEXT')
    update_meme.assert_any_param(param='tags', value='TAGS')
    update_meme.assert_any_param(param='info', value='INFO')
    update_meme.assert_any_param(param='url', value='URL')
    update_meme.assert_status_code(200)
    update_meme.updating_meme(id_meme=setup_teardown.meme_id, text='TEXT', tags='TAGS', info='INFO',
                              token="xxx", url='URL')  # без авторизации
    update_meme.assert_status_code(401)

    update_meme.updating_meme(id_meme='', text='TEXT', tags='TAGS', info='INFO',
                              token=setup_teardown.token,
                              url='URL')  # тип данных "id" str
    update_meme.assert_status_code(404)

    update_meme.updating_meme(id_meme=None, text='TEXT', tags='TAGS', info='INFO',
                              token=setup_teardown.token, url='URL')  # тип данных "id" None
    update_meme.assert_status_code(404)
    update_meme.updating_meme(id_meme=setup_teardown.meme_id, text='', tags='TAGS', info='INFO',
                              token=setup_teardown.token, url='URL')  # пустое значение "text"
    update_meme.assert_status_code(200)

    setup_teardown.missing_parameter(method='put', param='text', token=setup_teardown.token)  # без параметра "text"
    setup_teardown.assert_status_code(400)

    update_meme.updating_meme(id_meme=setup_teardown.meme_id, text=1, tags='TAGS', info='INFO',
                              token=setup_teardown.token, url='URL')  # тип данных "text" int
    update_meme.assert_status_code(400)

    update_meme.updating_meme(id_meme=setup_teardown.meme_id, text=[], tags='TAGS', info='INFO',
                              token=setup_teardown.token, url='URL')  # тип данных "text" list
    update_meme.assert_status_code(400)

    update_meme.updating_meme(id_meme=setup_teardown.meme_id, text={}, tags='TAGS', info='INFO',
                              token=setup_teardown.token, url='URL')  # тип данных "text" dict
    update_meme.assert_status_code(400)

    update_meme.updating_meme(id_meme=setup_teardown.meme_id, text=None, tags='TAGS', info='INFO',
                              token=setup_teardown.token, url='URL')  # значение "text" None
    update_meme.assert_status_code(400)

    update_meme.updating_meme(id_meme=setup_teardown.meme_id, text='TEXT', tags='TAGS', info='INFO',
                              token=setup_teardown.token, url='')  # пустое значение "url"
    update_meme.assert_status_code(200)

    setup_teardown.missing_parameter(method='put', param='url', token=setup_teardown.token)  # без параметра "url"
    setup_teardown.assert_status_code(400)

    update_meme.updating_meme(id_meme=setup_teardown.meme_id, text='TEXT', tags='TAGS', info='INFO',
                              token=setup_teardown.token, url=1)  # тип данных "url" int
    update_meme.assert_status_code(400)

    update_meme.updating_meme(id_meme=setup_teardown.meme_id, text='TEXT', tags='TAGS', info='INFO',
                              token=setup_teardown.token, url=['URL'])  # тип данных "url" list
    update_meme.assert_status_code(400)

    update_meme.updating_meme(id_meme=setup_teardown.meme_id, text='TEXT', tags='TAGS', info='INFO',
                              token=setup_teardown.token, url={1: 1})  # тип данных "url" dict
    update_meme.assert_status_code(400)

    update_meme.updating_meme(id_meme=setup_teardown.meme_id, text='TEXT', tags='TAGS', info='INFO',
                              token=setup_teardown.token, url=None)  # значение "url" None
    update_meme.assert_status_code(400)

    update_meme.updating_meme(id_meme=setup_teardown.meme_id, text='TEXT', tags='', info='INFO',
                              token=setup_teardown.token, url='URL')  # пустое значение "tags"
    update_meme.assert_status_code(200)
    #
    setup_teardown.missing_parameter(method='put', param='tags', token=setup_teardown.token)  # без параметра "tags"
    setup_teardown.assert_status_code(400)

    update_meme.replace_body_parameter(method='put', param='tags', value='STR', token=setup_teardown.token,
                                       id_meme=setup_teardown.meme_id)  # тип данных "tags" str
    update_meme.assert_status_code(400)

    update_meme.replace_body_parameter(method='put', param='tags', value=13, token=setup_teardown.token,
                                       id_meme=setup_teardown.meme_id)  # тип данных "tags" int
    update_meme.assert_status_code(400)

    update_meme.replace_body_parameter(method='put', param='tags', value={'param': 'TAGS'}, token=setup_teardown.token,
                                       id_meme=setup_teardown.meme_id)  # тип данных "tags" dict
    update_meme.assert_status_code(400)

    update_meme.replace_body_parameter(method='put', param='tags', value=None, token=setup_teardown.token,
                                       id_meme=setup_teardown.meme_id)  # значение "tags" None
    update_meme.assert_status_code(400)

    update_meme.updating_meme(id_meme=setup_teardown.meme_id, text='TEXT', tags='TAGS', info='',
                              token=setup_teardown.token, url='URL')  # пустое значение "info"
    update_meme.assert_status_code(200)

    setup_teardown.missing_parameter(method='put', param='info', token=setup_teardown.token)  # без параметра "info"
    setup_teardown.assert_status_code(400)

    update_meme.replace_body_parameter(method='put', param='info', value='STR', token=setup_teardown.token,
                                       id_meme=setup_teardown.meme_id)  # тип данных "info" str
    update_meme.assert_status_code(400)

    update_meme.replace_body_parameter(method='put', param='info', value=13, token=setup_teardown.token,
                                       id_meme=setup_teardown.meme_id)  # тип данных "info" int
    update_meme.assert_status_code(400)

    update_meme.replace_body_parameter(method='put', param='info', value=['LIST'], token=setup_teardown.token,
                                       id_meme=setup_teardown.meme_id)  # тип данных "info" list
    update_meme.assert_status_code(400)

    update_meme.replace_body_parameter(method='put', param='info', value=None, token=setup_teardown.token,
                                       id_meme=setup_teardown.meme_id)  # значение "info" None
    update_meme.assert_status_code(400)


@allure.title('Получение мема')
@allure.feature('getting information')
@allure.story('get an object')
@pytest.mark.parametrize("setup_teardown", [("SVS_Token", "TOKEN")], indirect=True)
def test_sute_get(setup_teardown, get_meme):
    get_meme.get_all_meme(token=setup_teardown.token)  # позитивный кейс, все мемы
    get_meme.assert_status_code(200)
    get_meme.assert_get_all()

    get_meme.get_one_meme(id_meme=setup_teardown.meme_id, token=setup_teardown.token)
    get_meme.assert_status_code(200)
    get_meme.assert_any_param(param='id', value=setup_teardown.meme_id)

    get_meme.get_one_meme(id_meme=setup_teardown.meme_id, token='xxx')
    get_meme.assert_status_code(401)


@allure.title('Удаление мема')
@allure.feature('object manipulation')
@allure.story('deleting an object')
@pytest.mark.parametrize("token_create_meme", [("SVS_Token", "TOKEN")], indirect=True)
def test_sute_delete(token_create_meme, delete_meme, get_meme):
    delete_meme.deleting_meme(id_meme=token_create_meme.meme_id, token=token_create_meme.token)  # позитивный кейс
    delete_meme.assert_status_code(200)
    delete_meme.deleting_meme(id_meme=token_create_meme.meme_id, token='xxx')  # Удаление без авторизации
    delete_meme.assert_status_code(401)
    get_meme.get_one_meme(id_meme=token_create_meme.meme_id, token=token_create_meme.token)
    get_meme.assert_status_code(404)  # проверяем 404 статус при запросе удаленного мема


@allure.title('Создание токена авторизации')
@allure.feature('object authorization')
@allure.story('authorization')
def test_sute_toket(token_auth):
    token_auth.new_token('SVS_TOKEN')  # создание токена, валидный кейс
    token_auth.assert_status_code(200)
    token_auth.assert_any_param(param='user', value='SVS_TOKEN')

    token_auth.validate_token(token_auth.token)  # проверка, работает ли токен
    token_auth.assert_status_code(200)

    token_auth.new_token(name=1)  # создание токена с типом данных 'name' int
    token_auth.assert_status_code(400)

    token_auth.new_token(name=[])  # создание токена с типом данных 'name' list
    token_auth.assert_status_code(400)

    token_auth.new_token(name={})  # создание токена с типом данных 'name' dict
    token_auth.assert_status_code(400)

    token_auth.new_token(name=None)  # создание токена с типом данных 'name' None
    token_auth.assert_status_code(400)

    token_auth.missing_parameter(method='post', param='name', token=None)  # создание токена без 'name'
    token_auth.assert_status_code(400)

    delete_last_from_dotenv('TOKEN')  # удаление тесового токена из файла .env
