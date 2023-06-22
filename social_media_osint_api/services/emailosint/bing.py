from social_media_osint_api.services.emailosint.email_request import EmailRequest


class Bing(EmailRequest):
    def __init__(self, target):
        EmailRequest.__init__(self)
        self.target = target

    def search(self, email=""):
        print('Searching "%s" in Bing...' % (self.target))
        url = "http://bing.com/search?q=%40{target}".format(
            target=self.target)
        try:
            resp = self.send_request(
                method='GET',
                url=url,
                headers={
                    'Cookie': 'SRCHHPGUSR=ADLT=DEMOTE&NRSLT=100'
                }
            )
            return self.get_email(resp.content, self.target)
        except Exception as e:
            pass
