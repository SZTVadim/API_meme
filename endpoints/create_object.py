from endpoints.endpoint import Endpoint
import allure


class CreateMeme(Endpoint):
    def setup_meme(self, text=None, tags=None, info=None, token=None, url=None):
        body = {"text": text, "url": url, "tags": tags, "info": info}
        self.response = self.send_request(method='post', body=body, token=token, url=f'{self.url_req}/meme')
        if self.response.status_code == 200:
            self.response_json = self.response.json()
            self.meme_id = self.response_json["id"]
        return self.meme_id

    @allure.step('Создание мема')
    def new_meme(self, text=None, tags=None, info=None, token=None, url=None):
        body = {"text": text, "url": url, "tags": [tags], "info": {'discription': info}}
        self.response = self.send_request(method='post', body=body, token=token, url=f'{self.url_req}/meme')
        if self.response.status_code == 200:
            self.response_json = self.response.json()
            self.meme_id = self.response_json["id"]
        return self.meme_id
