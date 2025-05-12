import pytest
import allure

from testing_project.conftest import token
from testing_project.conftest import create_meme
from testing_project.conftest import get_meme
from testing_project.conftest import delete_meme


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
