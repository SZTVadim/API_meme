from testing_project.endpoints.endpoint import Endpoint
import allure


class GetMeme(Endpoint):
    @allure.step('Получить один мем')
    def get_one_meme(self, id_meme, token):
        self.response = self.send_request(method='get', url=f"{self.url_req}/meme/{id_meme}", body=None, token=token)
        if self.response.status_code == 200:
            self.response_json = self.response.json()
        return self.response

    @allure.step('Получить все мемы')
    def get_all_meme(self, token):
        self.response = self.send_request(method='get', url=f"{self.url_req}/meme", token=token, body=None)
        if self.response.status_code == 200:
            self.response_json = self.response.json()
        return self.response

    @allure.step('Проверка, что в ответе больше одного элемента')
    def assert_get_all(self):
        assert len(self.response_json['data']) > 0
