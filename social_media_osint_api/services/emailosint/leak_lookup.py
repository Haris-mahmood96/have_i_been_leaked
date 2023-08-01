import json
from social_media_osint_api.services.emailosint.email_request import EmailRequest


class LeakLookUp(EmailRequest):
    # 10 API requests per day
    API_KEY = '20e6f94e77456c2fc20b9ad4c8d10d78'

    def __init__(self):
        EmailRequest.__init__(self)

    def search(self, email=""):
        print('Searching "{}" in leak-lookup...'.format(email))
        url = 'https://leak-lookup.com/api/search'
        params = {'key': self.API_KEY, 'type': 'email_address', 'query': email}
        try:
            resp = self.send_request(
                method='POST',
                url=url,
                data=params
            )
            data = resp.text
            parsed = json.loads(data)
            return parsed
        except Exception as e:
            pass
