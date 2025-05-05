from final_project.Endpoints.create_meth import CreateMeme
from final_project.Endpoints.delete_meth import DeleteMeme
import allure


@allure.title('Создание мема')
@allure.feature('object manipulation')
@allure.story('creating an object')
def post_testing(text=None, tags=None, info=None, token=None, url=None):
    obj = CreateMeme()
    obj.create_meme(text, tags, info, token, url)  # Позитивный кейс
    obj.assert_any_param(param='text', value=text)
    obj.assert_any_param(param='tags', value=tags)
    obj.assert_any_param(param='info', value=info)
    obj.assert_any_param(param='url', value=url)
    obj.assert_status_code(200)

    del_obj = DeleteMeme()  # Экземпляр класса для удления мема после теста
    del_obj.delete_meme(id_meme=obj.meme_id, token=token)

    obj.create_meme(text=text, tags=tags, info=info, token='xxx', url=url)  # без токена авторизации
    obj.assert_status_code(401)

    obj.create_meme(text='', info=info, token=token, url=url, tags=tags)  # пустое значение "text"
    obj.assert_status_code(200)
    del_obj.delete_meme(id_meme=obj.meme_id, token=token)

    obj.delete_params(method='post', param='text', token=token)  # без параметра "text"
    obj.assert_status_code(400)

    obj.create_meme(text=1, info=info, token=token, url=url, tags=tags)  # тип данных "text" int
    obj.assert_status_code(400)

    obj.create_meme(text=[], info=info, token=token, url=url, tags=tags)  # тип данных "text" list
    obj.assert_status_code(400)

    obj.create_meme(text={}, info=info, token=token, url=url, tags=tags)  # тип данных "text" dict
    obj.assert_status_code(400)

    obj.create_meme(text=None, info=info, token=token, url=url, tags=tags)  # значение параметра "text" None
    obj.assert_status_code(400)

    obj.delete_params(method='post', param='url', token=token)  # без параметра "url"
    obj.assert_status_code(400)

    obj.create_meme(text=text, info=info, token=token, url='', tags=tags)  # пустое значение "url"
    obj.assert_status_code(200)
    del_obj.delete_meme(id_meme=obj.meme_id, token=token)

    obj.create_meme(text=text, info=info, token=token, url=1, tags=tags)  # тип данных "url" int
    obj.assert_status_code(400)

    obj.create_meme(text=text, info=info, token=token, url=[], tags=tags)  # тип данных "url" list
    obj.assert_status_code(400)

    obj.create_meme(text=text, info=info, token=token, url={}, tags=tags)  # тип данных "url" dict
    obj.assert_status_code(400)

    obj.create_meme(text=text, info=info, token=token, url=None, tags=tags)  # значение параметра "url" None
    obj.assert_status_code(400)

    obj.delete_params(method='post', param='tags', token=token)  # без параметра "tags"
    obj.assert_status_code(400)

    obj.create_meme(text=text, info=info, token=token, url=url, tags=[])  # пустое значение "tags"
    obj.assert_status_code(200)
    del_obj.delete_meme(id_meme=obj.meme_id, token=token)

    obj.create_meme(text=text, info=info, token=token, url=url, tags='tags')  # тип данных "tags" str
    obj.assert_status_code(400)

    obj.create_meme(text=text, info=info, token=token, url=url, tags=1)  # тип данных "tags" int
    obj.assert_status_code(400)

    obj.create_meme(text=text, info=info, token=token, url=url, tags={})  # тип данных "tags" dict
    obj.assert_status_code(400)

    obj.create_meme(text=text, info=info, token=token, url=url, tags=None)  # значение параметра "tags" None
    obj.assert_status_code(400)

    obj.delete_params(method='post', param='info', token=token)  # без параметра "info"
    obj.assert_status_code(400)

    obj.create_meme(text=text, info={}, token=token, url=url, tags=tags)  # пустое значение "info"
    obj.assert_status_code(200)
    del_obj.delete_meme(id_meme=obj.meme_id, token=token)

    obj.create_meme(text=text, info='info', token=token, url=url, tags=tags)  # тип данных "info" str
    obj.assert_status_code(400)

    obj.create_meme(text=text, info=1, token=token, url=url, tags=tags)  # тип данных "info" int
    obj.assert_status_code(400)

    obj.create_meme(text=text, info=[info], token=token, url=url, tags=tags)  # тип данных "info" list
    obj.assert_status_code(400)

    obj.create_meme(text=text, info=None, token=token, url=url, tags=tags)  # значение параметра "info" None
    obj.assert_status_code(400)
