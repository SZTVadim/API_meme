import pytest
import allure
from testing_project.conftest import token
from testing_project.conftest import create_meme
from testing_project.conftest import delete_meme


@allure.title('Создание мема')
@allure.feature('object manipulation')
@allure.story('creating an object')
@pytest.mark.parametrize("token", [("SVS_Token", "TOKEN")], indirect=True)
def test_create_meme(token, create_meme, delete_meme):
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
