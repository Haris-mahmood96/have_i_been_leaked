from social_media_osint_api.services.emailosint.email_request import EmailRequest
from social_media_osint_api.services.request import Request


class Ask(EmailRequest):
    def __init__(self, target):
        EmailRequest.__init__(self)
        self.target = target

    def search(self, email=""):
        print('Searching %s in Ask...'.format(self.target))
        url = "http://www.ask.com/web?q=%40{target}&pu=100&page=0".format(
            target=self.target)
        try:
            resp = self.send_request(
                method='GET',
                url=url
            )
            return self.get_email(resp.content, self.target)
        except Exception as e:
            print(e)
