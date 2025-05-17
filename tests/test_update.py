import pytest
import allure
from conftest import token
from conftest import meme_id


@allure.title('Обновление мема')
@allure.feature('object manipulation')
@allure.story('full changing an object')
@pytest.mark.parametrize("token", [("SVS_Token", "TOKEN")], indirect=True)
def test_updating(meme_id, update_meme, token):
    update_meme.updating_meme(id_meme=meme_id, text='TEXT', tags='TAGS', info='INFO',
                              token=token, url='URL')  # Позитивный кейс
    update_meme.assert_status_code(200)
    update_meme.assert_any_param(param='text', value='TEXT')  # Проверка параметра text
    update_meme.assert_any_param(param='tags', value='TAGS')  # Проверка параметра tags
    update_meme.assert_any_param(param='info', value='INFO')  # Проверка параметра info
    update_meme.assert_any_param(param='url', value='URL')  # Проверка параметра url


@pytest.mark.parametrize("token", [("SVS_Token", "TOKEN")], indirect=True)
def test_token_is_empty(meme_id, update_meme, token):
    update_meme.updating_meme(id_meme=meme_id, text='TEXT', tags='TAGS', info='INFO',
                              token="", url='URL')  # без авторизации
    update_meme.assert_status_code(401)


@pytest.mark.parametrize("id_param", [
    "",  # id is empty string
    None,  # id is None
], ids=['id is empty', 'id is None'])
@pytest.mark.parametrize("token", [("SVS_Token", "TOKEN")], indirect=True)
def test_id_type_str(update_meme, token, meme_id, id_param):
    update_meme.updating_meme(id_meme=id_param, text='TEXT', tags='TAGS', info='INFO',
                              token=token,
                              url='URL')  # определенные тип данных "id"
    update_meme.assert_status_code(404)


@pytest.mark.parametrize('param', ['text', 'url', 'tags', 'info'],
                         ids=["no text", "no url", "no tags", "no info"])
@pytest.mark.parametrize("token", [("SVS_Token", "TOKEN")], indirect=True)
def test_without_param_text(update_meme, token, meme_id, param):
    update_meme.missing_parameter(method='put', param=param, token=token,
                                  meme_id=meme_id)  # без определенного параметра
    update_meme.assert_status_code(400)


@pytest.mark.parametrize('text', [1, [], {}, None],
                         ids=['text is int', 'text is list', 'text is dict', 'text is None'])
@pytest.mark.parametrize("token", [("SVS_Token", "TOKEN")], indirect=True)
def test_text_type_int(update_meme, token, meme_id, text):
    update_meme.updating_meme(id_meme=meme_id, text=text, tags='TAGS', info='INFO',
                              token=token, url='URL')  # определенный тип данных "text"
    update_meme.assert_status_code(400)


@pytest.mark.parametrize(
    "field, empty_value, assertion_param",
    [
        ("text", "", "text"),  # пустой текст
        ("url", "", "url"),  # пустой url
        ("tags", "", "tags"),  # пустые теги
        ("info", "", "info")  # пустое info
    ],
    ids=["empty text", "empty url", "empty tags", "empty info"]
)
@pytest.mark.parametrize("token", [("SVS_Token", "TOKEN")], indirect=True)
def test_empty_field_is_allowed(meme_id, update_meme, token,
                                field, empty_value, assertion_param):
    data = dict(id_meme=meme_id, text="TEXT", url="URL", tags="TAGS", info="INFO", token=token)
    data[field] = empty_value

    update_meme.updating_meme(**data)  # пустое значение определенного параметра
    update_meme.assert_status_code(200)
    update_meme.assert_any_param(param=assertion_param, value=empty_value)


@pytest.mark.parametrize('url', [1, [], {}, None],
                         ids=['url is int', 'url is list', 'url is dict', 'url is None'])
@pytest.mark.parametrize("token", [("SVS_Token", "TOKEN")], indirect=True)
def test_url_type_int(update_meme, token, meme_id, url):
    update_meme.updating_meme(id_meme=meme_id, text='TEXT', tags='TAGS', info='INFO',
                              token=token, url=url)  # определенные тип данных "url"
    update_meme.assert_status_code(400)


@pytest.mark.parametrize('tags', ['str', 1, {}, None],
                         ids=['url is int', 'url is list', 'url is dict', 'url is None'])
@pytest.mark.parametrize("token", [("SVS_Token", "TOKEN")], indirect=True)
def test_tags_type_str(update_meme, token, meme_id, tags):
    update_meme.replace_body_parameter(method='put', param='tags', value=tags, token=token,
                                       id_meme=meme_id)  # определенный тип данных "tags"
    update_meme.assert_status_code(400)


@pytest.mark.parametrize('info', ['str', 1, [], None],
                         ids=['url is int', 'url is list', 'url is dict', 'url is None'])
@pytest.mark.parametrize("token", [("SVS_Token", "TOKEN")], indirect=True)
def test_info_type_str(update_meme, token, meme_id, info):
    update_meme.replace_body_parameter(method='put', param='info', value=info, token=token,
                                       id_meme=meme_id)  # определенный тип данных "info"
    update_meme.assert_status_code(400)
