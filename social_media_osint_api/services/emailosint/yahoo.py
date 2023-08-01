from social_media_osint_api.services.emailosint.email_request import EmailRequest


class Yahoo(EmailRequest):
    def __init__(self):
        EmailRequest.__init__(self)

    def search(self, email=""):
        print('Searching "{}" in Yahoo...'.format(email))
        url = "http://search.yahoo.com/search?p=%40{target}&b=0&pz=10".format(
            target=email)
        try:
            resp = self.send_request(
                method='GET',
                url=url,
                headers={
                    'Host': 'search.yahoo.com'
                }
            )
            return self.get_email(resp.content, email)
        except Exception as e:
            pass
