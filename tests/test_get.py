import pytest
import allure

from conftest import token
from conftest import get_meme
from conftest import meme_id


@allure.title('Получение мема')
@allure.feature('getting information')
@allure.story('get an object')
@pytest.mark.parametrize("token", [("SVS_Token", "TOKEN")], indirect=True)
def test_get_all_meme_valid(token, get_meme, meme_id):
    get_meme.get_all_meme(token=token)  # позитивный кейс, все мемы
    get_meme.assert_status_code(200)
    get_meme.assert_get_all()  # проверка не нулевого количество объектов


@pytest.mark.parametrize("token", [("SVS_Token", "TOKEN")], indirect=True)
def test_get_object_returns_correct_id(get_meme, meme_id, token):
    get_meme.get_one_meme(id_meme=meme_id, token=token)  # проверка получение определенного объекта
    get_meme.assert_status_code(200)
    get_meme.assert_any_param(param='id', value=meme_id)  # проверка получения именно того, что запросили


@pytest.mark.parametrize("token", [("SVS_Token", "TOKEN")], indirect=True)
def test_get_without_token(get_meme, meme_id):
    get_meme.get_one_meme(id_meme=meme_id, token='xxx')
    get_meme.assert_status_code(401)
