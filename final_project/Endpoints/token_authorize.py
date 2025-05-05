from final_project.helpers.helpers import check_in_dotenv, delete_from_dotenv, add_in_dotenv
from final_project.Endpoints.endpoint import Endpoint
import allure


class TokenAuthorize(Endpoint):
    @allure.step('Создание токена вторизации')
    def new_token(self, name):
        self.response = self.send_request(method='post', url=f"{self.url_req}/authorize", body={"name": name},
                                          token=None)
        if self.response.status_code == 200:
            self.response_json = self.response.json()
            self.token = self.response.json()["token"]
            self.name = name
            add_in_dotenv(self.token)

            return self.token

    @allure.step('Проверка не протух ли токен')
    def validate_token(self, token):
        self.response = self.send_request(method='get', url=f"{self.url_req}/authorize/{token}", token=None, body=None)
        respons_status = self.response.status_code
        return respons_status

    @allure.step('Проверяем есть ли старый токен для работы')
    def token_preparation(self, name_token,
                          key_token):  # Проверяем можно ли использовать старый токен, или создаем новый
        token = check_in_dotenv(key_token)
        need_new_token = None
        if token:
            valid_token = self.validate_token(token)
            match valid_token:
                case 200:
                    self.token = token
                    need_new_token = False
                case _:
                    delete_from_dotenv(key_token)
                    need_new_token = True
        else:
            need_new_token = True

        if need_new_token:
            self.new_token(name_token)
        return self.token
