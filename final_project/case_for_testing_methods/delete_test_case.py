from final_project.Endpoints.create_meth import CreateMeme
from final_project.Endpoints.delete_meth import DeleteMeme
from final_project.Endpoints.get_meth import GetMeme
import allure


@allure.title('Удаление мема')
@allure.feature('object manipulation')
@allure.story('deleting an object')
def delete_testing(token=None):
    obj = CreateMeme()
    get_obj = GetMeme()
    del_obj = DeleteMeme()
    obj.create_meme(text='test', tags=['test'], info={'param': 'test'}, token=token, url=obj.url_req)
    del_obj.delete_meme(id_meme=obj.meme_id, token=token)  # позитивный кейс
    del_obj.assert_status_code(200)

    obj.create_meme(text='test', tags=['test'], info={'param': 'test'}, token=token, url=obj.url_req)
    del_obj.delete_meme(id_meme=obj.meme_id, token='xxx')  # Удаление без авторизации
    del_obj.assert_status_code(401)

    del_obj.delete_meme(id_meme='', token=token)  # Удаление без ID мема
    del_obj.assert_status_code(404)

    if get_obj.get_one_meme(id_meme=obj.meme_id, token=token).status_code == 200:
        del_obj.delete_meme(id_meme=obj.meme_id, token=token)  # Удаление созданного мема
