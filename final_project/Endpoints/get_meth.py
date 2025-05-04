from final_project.Endpoints.endpoint import Endpoint


class GetMeme(Endpoint):
    def get_one_meme(self, id_meme, token):
        self.response = self.send_request(method='get', url=f"{self.url_req}/meme/{id_meme}", body=None, token=token)
        if self.response.status_code == 200:
            self.response_json = self.response.json()
        return self.response

    def get_all_meme(self, token):
        self.response = self.send_request(method='get', url=f"{self.url_req}/meme", token=token, body=None)
        if self.response.status_code == 200:
            self.response_json = self.response.json()
        return self.response

    def assert_get_all(self):
        assert len(self.response_json['data']) > 0
