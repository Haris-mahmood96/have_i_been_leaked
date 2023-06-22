from social_media_osint_api.services.emailosint.email_request import EmailRequest


class Dogpile(EmailRequest):
    def __init__(self, target):
        EmailRequest.__init__(self)
        self.target = target

    def search(self, email=""):
        print('Searching "%s" in DogPile...'.format(self.target))
        url = "http://www.dogpile.com/search/web?qsi=0&q=%40{target}".format(
            target=self.target)
        try:
            resp = self.send_request(
                method='GET',
                url=url,
                headers={
                    'Host': 'www.dogpile.com'
                }
            )
            return self.get_email(resp.content, self.target)
        except Exception as e:
            pass
