import requests
import urllib3


class Request(object):
    agent = ''

    def send_request(self, method: str, url: str, params=None, data=None, headers=None):
        if headers is None: headers = {}
        headers['User-Agent'] = Request.agent
        try:
            session = requests.Session()

            urllib3.disable_warnings(
                urllib3.exceptions.InsecureRequestWarning
            )
            req = requests.request(method=method, url=url, params=params, data=data, headers=headers,
                                   allow_redirects=True,
                                   verify=False)

            return req
        except requests.RequestException as e:
            exit(print('Failed to establish a new connection'))


