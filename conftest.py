import pytest
from helpers.helper_file import TEST_DATA as data
from endpoints.create_object import CreateMeme
from endpoints.delete_object import DeleteMeme
from endpoints.get_object import GetMeme
from endpoints.update_object import UpdateMeme
from endpoints.authorization_endpoint import TokenAuthorize


@pytest.fixture()
def token(request):
    name_token, key_token = request.param
    token_manager = TokenAuthorize()
    token_manager.token_preparation(name_token, key_token)
    yield token_manager.token


@pytest.fixture()
def meme_id(token, create_meme, delete_meme):
    obj = create_meme
    obj.setup_meme(text=data['text'], tags=data['tags'], info=data['info'], token=token, url=create_meme.url_req)
    yield obj.meme_id
    if obj.meme_id:
        delete_meme.deleting_meme(id_meme=create_meme.meme_id, token=token)


@pytest.fixture()
def create_teardown(delete_meme, token):
    meme = CreateMeme()
    yield meme
    if meme.meme_id:
        delete_meme.deleting_without_step(id_meme=meme.meme_id, token=token)


@pytest.fixture()
def create_meme():
    yield CreateMeme()


@pytest.fixture()
def create_meme():
    yield CreateMeme()


@pytest.fixture()
def update_meme():
    return UpdateMeme()


@pytest.fixture()
def get_meme():
    return GetMeme()


@pytest.fixture()
def delete_meme():
    return DeleteMeme()


@pytest.fixture()
def is_token():
    return TokenAuthorize()
