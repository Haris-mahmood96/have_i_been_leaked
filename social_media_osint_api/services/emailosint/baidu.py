from social_media_osint_api.services.emailosint.email_request import EmailRequest
from social_media_osint_api.services.request import Request


class Baidu(EmailRequest):
    def __init__(self, target):
        EmailRequest.__init__(self)
        self.target = target

    def search(self, email=""):
        print('Searching "%s" in Baidu...'.format(self.target))
        url = "http://www.baidu.com/s?wd=%40{target}&pn=0".format(
            target=self.target)
        try:
            resp = self.send_request(
                method='GET',
                url=url,
                headers={
                    'Host': 'www.baidu.com'
                }
            )
            return self.get_email(resp.content, self.target)
        except Exception as e:
            pass
