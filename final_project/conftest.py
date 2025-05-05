import pytest
from final_project.Endpoints.token_authorize import TokenAuthorize
from final_project.helpers.helpers import delete_from_dotenv


@pytest.fixture()
def meme_teardown(request):
    name_token, key_token = request.param
    token_manager = TokenAuthorize()
    token_manager.token_preparation(name_token, key_token)
    yield token_manager
    # delete_from_dotenv(token_manager.token)
