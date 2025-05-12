import pytest
import allure
from testing_project.conftest import token
from testing_project.conftest import meme_id


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
