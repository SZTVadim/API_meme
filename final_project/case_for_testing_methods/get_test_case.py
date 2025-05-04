from final_project.Endpoints.create_meth import CreateMeme
from final_project.Endpoints.delete_meth import DeleteMeme
from final_project.Endpoints.get_meth import GetMeme


def get_testing(token=None):
    obj = CreateMeme()
    del_obj = DeleteMeme()
    get_obj = GetMeme()
    obj.create_meme(text='test', tags=['test'], info={'param': 'test'}, token=token, url=obj.url_req)
    get_obj.get_all_meme(token=token)  # позитивный кейс, все мемы
    get_obj.assert_status_code(200)
    get_obj.assert_get_all()

    get_obj.get_one_meme(id_meme=obj.meme_id, token=token)
    get_obj.assert_status_code(200)
    obj.assert_any_param(param='id', value=obj.meme_id)

    if get_obj.get_one_meme(id_meme=obj.meme_id, token=token).status_code == 200:
        del_obj.delete_meme(id_meme=obj.meme_id, token=token)  # Удаление созданного мема
