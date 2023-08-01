import json
from social_media_osint_api.services.emailosint.email_request import EmailRequest


class BreachedDirectory(EmailRequest):
    # 10 request / month
    API_KEYS = ['9230615fd0msha7197987c90bd0fp1ee1bejsnb133dd54f02e',
                '28c39a197bmsh22e86f1139ed412p17d1d6jsn9a72df9c0bed',
                'f9333cd439mshde02046d26674a3p137999jsnda4be13b615b']
    API_KEY = '9230615fd0msha7197987c90bd0fp1ee1bejsnb133dd54f02e'
    API_KEY2 = '28c39a197bmsh22e86f1139ed412p17d1d6jsn9a72df9c0bed'
    API_KEY3 = 'f9333cd439mshde02046d26674a3p137999jsnda4be13b615b'

    def __init__(self):
        EmailRequest.__init__(self)

    def search(self, email=""):
        print('Searching "{}" in breachdirectory...'.format(email))

        try:
            for key in self.API_KEYS:
                resp = self.__search(email=email, api_key=key)
                if resp.status_code != 429:
                    break

            data = resp.text
            parsed = json.loads(data)
            return parsed
        except Exception as e:
            print(e)
            pass

    def __search(self, email: str, api_key:str ):

        url = 'https://breachdirectory.p.rapidapi.com/'
        params = {"func": "auto", "term": email}

        headers = {
            "X-RapidAPI-Key": api_key,
            "X-RapidAPI-Host": "breachdirectory.p.rapidapi.com"
        }
        resp = self.send_request(
            method='GET',
            url=url,
            params=params,
            headers=headers
        )
        return resp