import pytest
import allure

from testing_project.conftest import token
from testing_project.conftest import get_meme
from testing_project.conftest import meme_id


@allure.title('Получение мема')
@allure.feature('getting information')
@allure.story('get an object')
@pytest.mark.parametrize("token", [("SVS_Token", "TOKEN")], indirect=True)
def test_method_get(token, get_meme, meme_id):
    get_meme.get_all_meme(token=token)  # позитивный кейс, все мемы
    get_meme.assert_status_code(200)
    get_meme.assert_get_all()

    get_meme.get_one_meme(id_meme=meme_id, token=token)
    get_meme.assert_status_code(200)
    get_meme.assert_any_param(param='id', value=meme_id)

    get_meme.get_one_meme(id_meme=meme_id, token='xxx')
    get_meme.assert_status_code(401)
