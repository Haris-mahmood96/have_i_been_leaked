from social_media_osint_api.services.emailosint.email_request import EmailRequest


class Yahoo(EmailRequest):
    def __init__(self, target):
        EmailRequest.__init__(self)
        self.target = target

    def search(self, email=""):
        print('Searching "%s" in Yahoo...'.format(self.target))
        url = "http://search.yahoo.com/search?p=%40{target}&b=0&pz=10".format(
            target=self.target)
        try:
            resp = self.send_request(
                method='GET',
                url=url,
                headers={
                    'Host': 'search.yahoo.com'
                }
            )
            return self.get_email(resp.content, self.target)
        except Exception as e:
            pass
