from testing_project.endpoints.endpoint import Endpoint
import allure


class CreateMeme(Endpoint):
    @allure.step('Создание мема')
    def new_meme(self, text=None, tags=None, info=None, token=None, url=None):
        body = {"text": text, "url": url, "tags": [tags], "info": {'discription': info}}
        self.response = self.send_request(method='post', body=body, token=token, url=f'{self.url_req}/meme')
        if self.response.status_code == 200:
            self.response_json = self.response.json()
            self.meme_id = self.response_json["id"]
            print(self.meme_id)
        return self.meme_id
