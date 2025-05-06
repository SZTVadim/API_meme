import pytest
from final_project.helpers.helpers import TEST_DATA as data
from final_project.Endpoints.create_meth import CreateMeme
from final_project.Endpoints.delete_meth import DeleteMeme
from final_project.Endpoints.get_meth import GetMeme
from final_project.Endpoints.put_meth import UpdateMeme
from final_project.Endpoints.token_authorize import TokenAuthorize


@pytest.fixture()
def only_token(request):
    name_token, key_token = request.param
    token_manager = TokenAuthorize()
    token_manager.token_preparation(name_token, key_token)
    yield token_manager.token


@pytest.fixture()
def token_create_meme(create_meme, token_auth):
    token = token_auth.token_preparation(name_token='SVS_TOKEN', key_token='TOKEN')
    obj = create_meme
    obj.new_meme(text=data['text'], tags=data['tags'], info=data['info'], token=token,
                 url=create_meme.url_req)
    obj.token = token
    yield obj


@pytest.fixture()
def setup_teardown(create_meme, delete_meme, token_auth):
    token = token_auth.token_preparation(name_token='SVS_TOKEN', key_token='TOKEN')
    obj = create_meme
    obj.new_meme(text=data['text'], tags=data['tags'], info=data['info'], token=token,
                 url=create_meme.url_req)
    obj.token = token
    yield obj
    delete_meme.deleting_meme(id_meme=obj.meme_id,
                              token=token)


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


@pytest.fixture()
def token_auth():
    return TokenAuthorize()
