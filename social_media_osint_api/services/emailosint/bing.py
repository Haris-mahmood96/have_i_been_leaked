from social_media_osint_api.services.emailosint.email_request import EmailRequest


class Bing(EmailRequest):
    def __init__(self):
        EmailRequest.__init__(self)

    def search(self, email=""):
        print('Searching "%s" in Bing...' % (email))
        url = "http://bing.com/search?q=%40{target}".format(
            target=email)
        try:
            resp = self.send_request(
                method='GET',
                url=url,
                headers={
                    'Cookie': 'SRCHHPGUSR=ADLT=DEMOTE&NRSLT=100'
                }
            )
            return self.get_email(resp.content, email)
        except Exception as e:
            pass
