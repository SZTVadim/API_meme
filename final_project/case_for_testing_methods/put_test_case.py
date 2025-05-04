from final_project.Endpoints.create_meth import CreateMeme
from final_project.Endpoints.delete_meth import DeleteMeme
from final_project.Endpoints.put_meth import UpdateMeme


def put_testing(text, tags, info, token, url):
    obj = CreateMeme()
    upd_obj = UpdateMeme()
    del_obj = DeleteMeme()  # Экземпляр класса для удления мема после теста
    obj.create_meme(text, tags, info, token, url)  # Создание мема для обновления

    upd_obj.update_meme(id_meme=obj.meme_id, text=text, tags=tags, info=info, token=token, url=url)  # Позитивный кейс
    upd_obj.assert_status_code(200)
    obj.assert_any_param(param='id', value=obj.meme_id)
    obj.assert_any_param(param='text', value=text)
    obj.assert_any_param(param='tags', value=tags)
    obj.assert_any_param(param='info', value=info)
    obj.assert_any_param(param='url', value=url)

    upd_obj.update_meme(id_meme=obj.meme_id, text=text, tags=tags, info=info, token="xxx", url=url)  # без авторизации
    upd_obj.assert_status_code(401)

    upd_obj.update_meme(id_meme='', text=text, tags=tags, info=info, token=token, url=url)  # тип данных "id" str
    upd_obj.assert_status_code(404)

    upd_obj.update_meme(id_meme=None, text=text, tags=tags, info=info, token=token, url=url)  # тип данных "id" None
    upd_obj.assert_status_code(404)

    upd_obj.update_meme(id_meme=obj.meme_id, text='', tags=tags, info=info, token=token,
                        url=url)  # пустое значение "text"
    upd_obj.assert_status_code(200)

    obj.delete_params(method='put', param='text', token=token)  # без параметра "text"
    obj.assert_status_code(400)

    upd_obj.update_meme(id_meme=obj.meme_id, text=1, tags=tags, info=info, token=token,
                        url=url)  # тип данных "text" int
    upd_obj.assert_status_code(400)

    upd_obj.update_meme(id_meme=obj.meme_id, text=[], tags=tags, info=info, token=token,
                        url=url)  # тип данных "text" list
    upd_obj.assert_status_code(400)

    upd_obj.update_meme(id_meme=obj.meme_id, text={}, tags=tags, info=info, token=token,
                        url=url)  # тип данных "text" dict
    upd_obj.assert_status_code(400)

    upd_obj.update_meme(id_meme=obj.meme_id, text=None, tags=tags, info=info, token=token,
                        url=url)  # значение "text" None
    upd_obj.assert_status_code(400)

    upd_obj.update_meme(id_meme=obj.meme_id, text=text, tags=tags, info=info, token=token,
                        url='')  # пустое значение "url"
    upd_obj.assert_status_code(200)

    obj.delete_params(method='put', param='url', token=token)  # без параметра "url"
    obj.assert_status_code(400)

    upd_obj.update_meme(id_meme=obj.meme_id, text=text, tags=tags, info=info, token=token,
                        url=1)  # тип данных "url" int
    upd_obj.assert_status_code(400)

    upd_obj.update_meme(id_meme=obj.meme_id, text=text, tags=tags, info=info, token=token,
                        url=['url'])  # тип данных "url" list
    upd_obj.assert_status_code(400)

    upd_obj.update_meme(id_meme=obj.meme_id, text=text, tags=tags, info=info, token=token,
                        url={1: 1})  # тип данных "url" dict
    upd_obj.assert_status_code(400)

    upd_obj.update_meme(id_meme=obj.meme_id, text=text, tags=tags, info=info, token=token,
                        url=None)  # значение "url" None
    upd_obj.assert_status_code(400)

    upd_obj.update_meme(id_meme=obj.meme_id, text=text, tags=[], info=info, token=token,
                        url=url)  # пустое значение "tags"
    upd_obj.assert_status_code(200)

    obj.delete_params(method='put', param='tags', token=token)  # без параметра "tags"
    obj.assert_status_code(400)

    upd_obj.replace_body_parameter(method='put', param='tags', value='str', token=token,
                                   id_meme=obj.meme_id)  # тип данных "tags" str
    upd_obj.assert_status_code(400)

    upd_obj.replace_body_parameter(method='put', param='tags', value=13, token=token,
                                   id_meme=obj.meme_id)  # тип данных "tags" int
    upd_obj.assert_status_code(400)

    upd_obj.replace_body_parameter(method='put', param='tags', value={'param': 'tags'}, token=token,
                                   id_meme=obj.meme_id)  # тип данных "tags" dict
    upd_obj.assert_status_code(400)

    upd_obj.replace_body_parameter(method='put', param='tags', value=None, token=token,
                                   id_meme=obj.meme_id)  # значение "tags" None
    upd_obj.assert_status_code(400)

    upd_obj.update_meme(id_meme=obj.meme_id, text=text, tags=tags, info='', token=token,
                        url=url)  # пустое значение "info"
    upd_obj.assert_status_code(400)

    obj.delete_params(method='put', param='info', token=token)  # без параметра "info"
    obj.assert_status_code(400)

    upd_obj.replace_body_parameter(method='put', param='info', value='str', token=token,
                                   id_meme=obj.meme_id)  # пустое значение "info" str
    upd_obj.assert_status_code(400)

    upd_obj.replace_body_parameter(method='put', param='info', value=13, token=token,
                                   id_meme=obj.meme_id)  # тип данных "info" int
    upd_obj.assert_status_code(400)

    upd_obj.replace_body_parameter(method='put', param='info', value=['list'], token=token,
                                   id_meme=obj.meme_id)  # тип данных "info" list
    upd_obj.assert_status_code(400)

    upd_obj.replace_body_parameter(method='put', param='info', value=None, token=token,
                                   id_meme=obj.meme_id)  # значение "info" None
    upd_obj.assert_status_code(400)

    del_obj.delete_meme(id_meme=obj.meme_id, token=token)  # Удаление созданного мема
