from social_media_osint_api.services.emailosint.email_request import EmailRequest
from social_media_osint_api.services.request import Request


class Ask(EmailRequest):
    def __init__(self):
        EmailRequest.__init__(self)


    def search(self, email=""):
        print('Searching %s in Ask...'.format(email))
        url = "http://www.ask.com/web?q=%40{target}&pu=100&page=0".format(
            target=email)
        try:
            resp = self.send_request(
                method='GET',
                url=url
            )
            return self.get_email(resp.content, email)
        except Exception as e:
            print(e)
