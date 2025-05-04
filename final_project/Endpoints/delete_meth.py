from final_project.Endpoints.endpoint import Endpoint


class DeleteMeme(Endpoint):
    def delete_meme(self, id_meme, token):
        self.response = self.send_request(method='delete', url=f"{self.url_req}/meme/{id_meme}", token=token, body=None)
        return self.response
