import pytest
import allure

from conftest import token
from conftest import get_meme
from conftest import delete_meme


@allure.title('Удаление мема')
@allure.feature('object manipulation')
@allure.story('deleting an object')
@pytest.mark.parametrize("token", [("SVS_Token", "TOKEN")], indirect=True)
def test_deleting_meme(token, delete_meme, meme_id):
    delete_meme.deleting_meme(id_meme=meme_id, token=token)  # позитивный кейс
    delete_meme.assert_status_code(200)


@pytest.mark.parametrize("token", [("SVS_Token", "TOKEN")], indirect=True)
def test_deleting_without_token(delete_meme, meme_id):
    delete_meme.deleting_meme(id_meme=meme_id, token='xxx')  # Удаление без авторизации
    delete_meme.assert_status_code(401)


@pytest.mark.parametrize("token", [("SVS_Token", "TOKEN")], indirect=True)
def test_get_deleteng_mem(token, get_meme, delete_meme, meme_id):
    delete_meme.deleting_meme(id_meme=meme_id, token=token)
    get_meme.get_one_meme(id_meme=meme_id, token=token)
    get_meme.assert_status_code(404)  # проверяем 404 статус при запросе удаленного мема
