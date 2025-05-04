import pytest
from final_project.Endpoints.token_authorize import TokenAuthorize


@pytest.fixture()
def meme_teardown(request):
    name_token, key_token = request.param
    token_manager = TokenAuthorize()
    token_manager.token_preparation(name_token, key_token)
    yield token_manager
