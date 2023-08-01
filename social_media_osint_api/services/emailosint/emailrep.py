import json
from social_media_osint_api.services.emailosint.email_request import EmailRequest
from emailrep import EmailRep


class EmailRepIo(EmailRequest):
    API_KEY = '300feacc6n7cd1b5n3yf1fhhprkxipazx1rsm97fg1t96z07'

    def __init__(self):
        EmailRequest.__init__(self)

    def search(self, email=""):
        print('Searching "{}" in Emailrep...'.format(email))
        try:
            emailrep = EmailRep(self.API_KEY)
            # query an email address
            return emailrep.query(email)
        except Exception as e:
            print(e)
            pass
