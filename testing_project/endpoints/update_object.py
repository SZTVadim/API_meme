from testing_project.endpoints.endpoint import Endpoint
import allure


class UpdateMeme(Endpoint):
    @allure.step('Полное обновление мема')
    def updating_meme(self, id_meme=None, text=None, tags=None, info=None, token=None, url=None):
        body = {'id': id_meme, "text": text, "url": url, "tags": [tags], "info": {'discription': info}}
        self.response = self.send_request(method='put', url=f"{self.url_req}/meme/{id_meme}", body=body, token=token)
        if self.response.status_code == 200:
            self.response_json = self.response.json()
            self.meme_id = self.response_json["id"]
        return self.response
