import json
from social_media_osint_api.services.emailosint.email_request import EmailRequest


class EmailRep(EmailRequest):
    def __init__(self):
        EmailRequest.__init__(self)

    def search(self, email=""):
        print('Searching "%s" in Emailrep...'.format(email))
        url = 'https://emailrep.io/{}'.format(email)
        try:
            resp = self.send_request(
                method='GET',
                url=url,
                headers={
                    'Host': 'search.emailrep.io'
                }
            )
            data = resp.text
            parsed = json.loads(data)
            return parsed
        except Exception as e:
            pass
