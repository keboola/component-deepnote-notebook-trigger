from keboola.http_client import HttpClient
from requests.exceptions import HTTPError

BASE_URL = "https://api.deepnote.com/v1/"


class DeepnoteClientException(Exception):
    pass


class DeepnoteClient(HttpClient):
    def __init__(self, token: str):
        header = {"Authorization": f"Bearer {token}"}
        super().__init__(BASE_URL, default_http_header=header)

    def start_notebook(self, project_id: str, notebook_id: str):
        try:
            return self.post(endpoint_path=f"projects/{project_id}/notebooks/{notebook_id}/execute")
        except HTTPError as http_err:
            raise DeepnoteClientException(http_err) from http_err
