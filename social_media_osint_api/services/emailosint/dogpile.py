from social_media_osint_api.services.emailosint.email_request import EmailRequest


class Dogpile(EmailRequest):
    def __init__(self):
        EmailRequest.__init__(self)

    def search(self, email=""):
        print('Searching "{}" in DogPile...'.format(email))
        url = "http://www.dogpile.com/search/web?qsi=0&q=%40{target}".format(
            target=email)
        try:
            resp = self.send_request(
                method='GET',
                url=url,
                headers={
                    'Host': 'www.dogpile.com'
                }
            )
            return self.get_email(resp.content, email)
        except Exception as e:
            print(e)
            pass
