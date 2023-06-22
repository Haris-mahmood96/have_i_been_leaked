import json
from social_media_osint_api.services.emailosint.email_request import EmailRequest


class BreachedDirectory(EmailRequest):
    API_KEY = '9230615fd0msha7197987c90bd0fp1ee1bejsnb133dd54f02e'

    def __init__(self):
        EmailRequest.__init__(self)

    def search(self, email=""):
        print('Searching "%s" in breachdirectory...'.format(email))
        url = 'https://breachdirectory.p.rapidapi.com/'
        params = {"func": "auto", "term": email}

        headers = {
            "X-RapidAPI-Key": self.API_KEY,
            "X-RapidAPI-Host": "breachdirectory.p.rapidapi.com"
        }
        try:
            resp = self.send_request(
                method='GET',
                url=url,
                params=params,
                headers=headers
            )
            data = resp.text
            parsed = json.loads(data)
            return parsed
        except Exception as e:
            pass
