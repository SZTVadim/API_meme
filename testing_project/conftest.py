import pytest
from testing_project.helpers.helper_file import TEST_DATA as data
from testing_project.endpoints.create_object import CreateMeme
from testing_project.endpoints.delete_object import DeleteMeme
from testing_project.endpoints.get_object import GetMeme
from testing_project.endpoints.update_object import UpdateMeme
from testing_project.endpoints.authorization_endpoint import TokenAuthorize


@pytest.fixture()
def token(request):
    name_token, key_token = request.param
    token_manager = TokenAuthorize()
    token_manager.token_preparation(name_token, key_token)
    yield token_manager.token


@pytest.fixture()
def meme_id(create_meme, token, delete_meme):
    create_meme.new_meme(text=data['text'], tags=data['tags'], info=data['info'], token=token,
                         url=create_meme.url_req)
    yield create_meme.meme_id
    delete_meme.deleting_meme(id_meme=create_meme.meme_id, token=token)


@pytest.fixture()
def create_meme():
    return CreateMeme()


@pytest.fixture()
def update_meme():
    return UpdateMeme()


@pytest.fixture()
def get_meme():
    return GetMeme()


@pytest.fixture()
def delete_meme():
    return DeleteMeme()
