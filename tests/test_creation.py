import pytest
import allure
from conftest import token
from conftest import create_teardown
from conftest import delete_meme


@allure.title('Создание мема')
@allure.feature('object manipulation')
@allure.story('creating an object')
@pytest.mark.parametrize("token", [("SVS_Token", "TOKEN")], indirect=True)
def test_create_teardown_valid_case(token, create_teardown, delete_meme):
    create_teardown.new_meme(text='test', tags='tags', info='info', token=token, url='url')  # Позитивный кейс
    create_teardown.assert_status_code(200)
    create_teardown.assert_any_param(param='text', value='test')  # Проверка параметра text
    create_teardown.assert_any_param(param='tags', value='tags')  # Проверка параметра tags
    create_teardown.assert_any_param(param='info', value='info')  # Проверка параметра info
    create_teardown.assert_any_param(param='url', value='url')  # Проверка параметра url


@pytest.mark.parametrize("token", [("SVS_Token", "TOKEN")], indirect=True)
def test_token_is_empty(token, create_teardown):
    create_teardown.new_meme(text='Test', tags='tags', info='info', token='', url='url')  # без токена авторизации
    create_teardown.assert_status_code(401)


@pytest.mark.parametrize("token", [("SVS_Token", "TOKEN")], indirect=True)
def test_without_param_text(token, create_teardown):
    create_teardown.missing_parameter(method='post', param='text', token=token)  # без параметра "text"
    create_teardown.assert_status_code(400)


@pytest.mark.parametrize("token", [("SVS_Token", "TOKEN")], indirect=True)
def test_text_is_empty(token, create_teardown, delete_meme):
    create_teardown.new_meme(text='', tags='tags', info='info', token=token, url='url')  # пустое значение "text"
    create_teardown.assert_status_code(200)
    create_teardown.assert_any_param(param='text', value='')


@pytest.mark.parametrize("token", [("SVS_Token", "TOKEN")], indirect=True)
def test_text_type_int(token, create_teardown):
    create_teardown.new_meme(text=1, tags='tags', info='info', token=token, url='url')  # тип данных "text" int
    create_teardown.assert_status_code(400)


@pytest.mark.parametrize("token", [("SVS_Token", "TOKEN")], indirect=True)
def test_text_type_list(token, create_teardown):
    create_teardown.new_meme(text=[], tags='tags', info='info', token=token, url='url')  # тип данных "text" list
    create_teardown.assert_status_code(400)


@pytest.mark.parametrize("token", [("SVS_Token", "TOKEN")], indirect=True)
def test_text_type_dict(token, create_teardown):
    create_teardown.new_meme(text={}, tags='tags', info='info', token=token, url='url')  # тип данных "text" dict
    create_teardown.assert_status_code(400)


@pytest.mark.parametrize("token", [("SVS_Token", "TOKEN")], indirect=True)
def test_text_data_none(token, create_teardown):
    create_teardown.new_meme(text=None, tags='tags', info='info', token=token,
                             url='url')  # значение параметра "text" None
    create_teardown.assert_status_code(400)


@pytest.mark.parametrize("token", [("SVS_Token", "TOKEN")], indirect=True)
def test_without_param_url(token, create_teardown):
    create_teardown.missing_parameter(method='post', param='url', token=token)  # без параметра "url"
    create_teardown.assert_status_code(400)


@pytest.mark.parametrize("token", [("SVS_Token", "TOKEN")], indirect=True)
def test_url_is_empty(token, create_teardown, delete_meme):
    create_teardown.new_meme(text='text', tags='tags', info='info', token=token, url='')  # пустое значение "url"
    create_teardown.assert_status_code(200)
    create_teardown.assert_any_param(param='url', value='')


@pytest.mark.parametrize("token", [("SVS_Token", "TOKEN")], indirect=True)
def test_url_type_int(token, create_teardown):
    create_teardown.new_meme(text='text', tags='tags', info='info', token=token, url=1)  # тип данных "url" int
    create_teardown.assert_status_code(400)


@pytest.mark.parametrize("token", [("SVS_Token", "TOKEN")], indirect=True)
def test_url_type_list(token, create_teardown):
    create_teardown.new_meme(text='text', tags='tags', info='info', token=token, url=[])  # тип данных "url" list
    create_teardown.assert_status_code(400)


@pytest.mark.parametrize("token", [("SVS_Token", "TOKEN")], indirect=True)
def test_url_type_dict(token, create_teardown):
    create_teardown.new_meme(text='text', tags='tags', info='info', token=token, url={})  # тип данных "url" dict
    create_teardown.assert_status_code(400)


@pytest.mark.parametrize("token", [("SVS_Token", "TOKEN")], indirect=True)
def test_url_data_none(token, create_teardown):
    create_teardown.new_meme(text='text', tags='tags', info='info', token=token,
                             url=None)  # значение параметра "url" None
    create_teardown.assert_status_code(400)


@pytest.mark.parametrize("token", [("SVS_Token", "TOKEN")], indirect=True)
def test_without_param_tags(token, create_teardown):
    create_teardown.missing_parameter(method='post', param='tags', token=token)  # без параметра "tags"
    create_teardown.assert_status_code(400)


@pytest.mark.parametrize("token", [("SVS_Token", "TOKEN")], indirect=True)
def test_tags_is_empty(token, create_teardown, delete_meme):
    create_teardown.new_meme(text='Text', tags='', info='', token=token, url='Url')  # пустое значение "tags"
    create_teardown.assert_status_code(200)
    create_teardown.assert_any_param(param='tags', value='')


@pytest.mark.parametrize("token", [("SVS_Token", "TOKEN")], indirect=True)
def test_tags_type_str(token, create_teardown):
    create_teardown.replace_body_parameter(method='post', param='tags', value='', token=token)  # тип данных "tags" str
    create_teardown.assert_status_code(400)


@pytest.mark.parametrize("token", [("SVS_Token", "TOKEN")], indirect=True)
def test_tags_type_int(token, create_teardown):
    create_teardown.replace_body_parameter(method='post', param='tags', value=1, token=token)  # тип данных "tags" int
    create_teardown.assert_status_code(400)


@pytest.mark.parametrize("token", [("SVS_Token", "TOKEN")], indirect=True)
def test_tags_type_dict(token, create_teardown):
    create_teardown.replace_body_parameter(method='post', param='tags', value={},
                                           token=token)  # тип данных "tags" dict
    create_teardown.assert_status_code(400)


@pytest.mark.parametrize("token", [("SVS_Token", "TOKEN")], indirect=True)
def test_tags_data_none(token, create_teardown):
    create_teardown.replace_body_parameter(method='post', param='tags', value=None,
                                           token=token)  # значение параметра "tags" None
    create_teardown.assert_status_code(400)


@pytest.mark.parametrize("token", [("SVS_Token", "TOKEN")], indirect=True)
def test_without_param_info(token, create_teardown):
    create_teardown.missing_parameter(method='post', param='info', token=token)  # без параметра "info"
    create_teardown.assert_status_code(400)


@pytest.mark.parametrize("token", [("SVS_Token", "TOKEN")], indirect=True)
def test_info_is_empty(token, create_teardown, delete_meme):
    create_teardown.new_meme(text='Text', tags='Tags', info='', token=token, url='Url')  # пустое значение "info"
    create_teardown.assert_status_code(200)
    create_teardown.assert_any_param(param='info', value='')


@pytest.mark.parametrize("token", [("SVS_Token", "TOKEN")], indirect=True)
def test_info_type_str(token, create_teardown):
    create_teardown.replace_body_parameter(method='post', param='info', value='info',
                                           token=token)  # тип данных "info" str
    create_teardown.assert_status_code(400)


@pytest.mark.parametrize("token", [("SVS_Token", "TOKEN")], indirect=True)
def test_info_type_int(token, create_teardown):
    create_teardown.replace_body_parameter(method='post', param='info', value=1, token=token)  # тип данных "info" int
    create_teardown.assert_status_code(400)


@pytest.mark.parametrize("token", [("SVS_Token", "TOKEN")], indirect=True)
def test_info_type_list(token, create_teardown):
    create_teardown.replace_body_parameter(method='post', param='info', value=[],
                                           token=token)  # тип данных "info" list
    create_teardown.assert_status_code(400)


@pytest.mark.parametrize("token", [("SVS_Token", "TOKEN")], indirect=True)
def test_info_data_none(token, create_teardown):
    create_teardown.replace_body_parameter(method='post', param='info', value=None,
                                           token=token)  # значение параметра "info" None
    create_teardown.assert_status_code(400)
