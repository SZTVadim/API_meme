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


@pytest.mark.parametrize('param', ['text', 'url', 'tags', 'info'],
                         ids=['no text', 'no url', 'no tags', 'no info'])
@pytest.mark.parametrize("token", [("SVS_Token", "TOKEN")], indirect=True)
def test_without_param_text(token, create_teardown, param):
    create_teardown.missing_parameter(method='post', param=param, token=token)  # без определенного параметра
    create_teardown.assert_status_code(400)


@pytest.mark.parametrize(
    "field, empty_value, assertion_param",
    [
        ("text", "", "text"),  # пустой text
        ("url", "", "url"),  # пустой url
        ("tags", "", "tags"),  # пустые tags
        ("info", "", "info")  # пустое info
    ],
    ids=["empty text", "empty url", "empty tags", "empty info"])
@pytest.mark.parametrize("token", [("SVS_Token", "TOKEN")], indirect=True)
def test_empty_field_is_allowed_on_create(token, create_teardown, delete_meme,
                                          field, empty_value, assertion_param):
    data = dict(text="TEXT", url="URL", tags="TAGS", info="INFO", token=token)
    data[field] = empty_value

    create_teardown.new_meme(**data)
    create_teardown.assert_status_code(200)
    create_teardown.assert_any_param(param=assertion_param, value=empty_value)


@pytest.mark.parametrize('text', [1, [], {}, None],
                         ids=['text is int', 'text is list', 'text is dict', 'text is None'])
@pytest.mark.parametrize("token", [("SVS_Token", "TOKEN")], indirect=True)
def test_text_type_int(token, create_teardown, text):
    create_teardown.new_meme(text=text, tags='tags', info='info', token=token,
                             url='url')  # определенный тип данных "text"
    create_teardown.assert_status_code(400)


@pytest.mark.parametrize('url', [1, [], {}, None],
                         ids=['url is int', 'url is list', 'url is dict', 'url is None'])
@pytest.mark.parametrize("token", [("SVS_Token", "TOKEN")], indirect=True)
def test_url_type_int(token, create_teardown, url):
    create_teardown.new_meme(text='text', tags='tags', info='info', token=token,
                             url=url)  # определенный тип данных "url"
    create_teardown.assert_status_code(400)


@pytest.mark.parametrize('tags', ['str', 1, {}, None],
                         ids=['tags is str', 'tags is int', 'tags is dict', 'tags is None'])
@pytest.mark.parametrize("token", [("SVS_Token", "TOKEN")], indirect=True)
def test_tags_type_str(token, create_teardown, tags):
    create_teardown.replace_body_parameter(method='post', param='tags', value=tags,
                                           token=token)  # определенный тип данных "tags"
    create_teardown.assert_status_code(400)


@pytest.mark.parametrize('info', ['str', 1, {}, None],
                         ids=['info is str', 'info is int', 'info is dict', 'info is None'])
@pytest.mark.parametrize("token", [("SVS_Token", "TOKEN")], indirect=True)
def test_info_type_str(token, create_teardown, info):
    create_teardown.replace_body_parameter(method='post', param='info', value=info,
                                           token=token)  # определенный тип данных "info"
    create_teardown.assert_status_code(400)
