from social_media_osint_api.services.emailosint.email_request import EmailRequest
from social_media_osint_api.services.request import Request


class Baidu(EmailRequest):
    def __init__(self):
        EmailRequest.__init__(self)

    def search(self, email=""):
        print('Searching "%s" in Baidu...'.format(email))
        url = "http://www.baidu.com/s?wd=%40{target}&pn=0".format(
            target=email)
        try:
            resp = self.send_request(
                method='GET',
                url=url,
                headers={
                    'Host': 'www.baidu.com'
                }
            )
            return self.get_email(resp.content, email)
        except Exception as e:
            pass
