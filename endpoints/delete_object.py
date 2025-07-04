from endpoints.endpoint import Endpoint
import allure


class DeleteMeme(Endpoint):
    @allure.step('удаление мема')
    def deleting_meme(self, id_meme, token):
        self.response = self.send_request(method='delete', url=f"{self.url_req}/meme/{id_meme}", token=token, body=None)
        return self.response

    def deleting_without_step(self, id_meme, token):
        self.response = self.send_request(method='delete', url=f"{self.url_req}/meme/{id_meme}", token=token, body=None)
        return self.response
