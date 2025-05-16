import requests
import allure


class Endpoint:
    url_req = "http://167.172.172.115:52355"
    side_body = {"text": "text", "url": "example_url", "tags": ["tags"], "info": {"description": "info"}}
    token = None
    name = None
    response = None
    meme_id = None
    response_json = None
    response_without_auth = None
    body = None

    @allure.step('удаление из "body" определенного парамера')
    def missing_parameter(self, method, param, token, meme_id=None):  # для запросос, где необходимо удалить параметр
        if token:
            body = self.side_body.copy()
            del body[param]
            if method.lower() in ["put"]:
                body['id'] = meme_id
            self.response = self.send_request(method=method, url=self.get_url(method, meme_id),
                                              token=token,
                                              body=body)
        else:
            body = {"name": "Test"}
            del body[param]
            self.response = self.send_request(method=method, url=f"{self.url_req}/authorize",
                                              token=None,
                                              body=body)

    @allure.step('заменить в "body" определенный парамер на заданное значение ')
    @allure.step('Полное обновление мема')
    def replace_body_parameter(self, method, param, value, token,
                               id_meme=None):  # для запросов, где необходимо заменить тип данных у параметра
        url = self.get_url(method, id_meme)
        self.side_body[param] = value
        if method.lower() in ["put"]:
            self.side_body['id'] = id_meme
        self.response = self.send_request(method=method, url=url,
                                          token=token, body=self.side_body)
        return self.response

    def prepare_token(self, token=None):  # Создаю словарь для передачи токена в хедерах запроса
        token_for_header = token if token else self.token
        return {"Authorization": token_for_header}

    def send_request(self, method, url, body, token=None, name=None):  # метод для отправки универсального запроса
        if name:
            return requests.request(method=method, url=url, json=body)
        else:
            header = self.prepare_token(token)
            return requests.request(method=method, url=url, headers=header, json=body)

    def get_url(self, method, meme_id=None):  # метод для  получения универсального значения "url"
        url = f"{self.url_req}/meme/{meme_id}" if method.lower() in ["put"] else f'{self.url_req}/meme'
        return url

    @allure.step('проверка статус кода ответа')
    def assert_status_code(self, status_code):
        assert self.response.status_code == status_code, ("The status code does not match the expected one"
                                                          f" your status code: {self.response.status_code}")

    @allure.step('проверка валидности параметра и его значения')
    def assert_any_param(self, param, value):
        match param:
            case 'info':
                assert self.response_json[param]['discription'] == value, (
                    f"The '{param}' of the meme does not match the expected one"
                    f" your value: {value}: {self.response_json[param]}")
            case 'tags':
                assert self.response_json[param][0] == value, (
                    f"The '{param}' of the meme does not match the expected one"
                    f" your value: {value}: {self.response_json[param]}")
            case _:
                assert self.response_json[param] == value, (f"The '{param}' of the meme does not match the expected one"
                                                            f" your value: {value}: {self.response_json[param]}")
