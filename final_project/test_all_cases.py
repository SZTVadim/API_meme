import pytest
from final_project.case_for_testing_methods.post_test_case import post_testing
from final_project.case_for_testing_methods.put_test_case import put_testing
from final_project.case_for_testing_methods.delete_test_case import delete_testing
from final_project.case_for_testing_methods.get_test_case import get_testing
from final_project.case_for_testing_methods.token_test_case import token_testing
from final_project.conftest import meme_teardown


@pytest.mark.parametrize("meme_teardown", [("SVS_Token", "TOKEN")], indirect=True)
def test_sute(meme_teardown):
    post_testing(text='Test', tags=['test_tag'], info={'info': 'test_info'}, token=meme_teardown.token, url='test_url')
    put_testing(text='TEST', tags=['TEST_TAG'], info={'param': 'TEST_INFO'}, token=meme_teardown.token, url='TEST_URL')
    delete_testing(token=meme_teardown.token)
    get_testing(token=meme_teardown.token)
    token_testing(token_name='SVS_TOKEN')