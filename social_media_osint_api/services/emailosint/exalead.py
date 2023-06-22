from social_media_osint_api.services.emailosint.email_request import EmailRequest


class Exalead(EmailRequest):
    def __init__(self, target):
        EmailRequest.__init__(self)
        self.target = target

    def search(self, email=""):
        print('Searching "%s" in Exalead...'.format(self.target))
        url = "http://www.exalead.com/search/web/results/?q=%40{target}&elements_per_page=50&start_index=0".format(
            target=self.target)
        try:
            resp = self.send_request(
                method='GET',
                url=url,
                headers={
                    'Host': 'www.exalead.com',
                    'Referer': 'http://exalead.com/search/web/results/?q=%40{target}'.format(
                        target=self.target)
                }
            )
            return self.get_email(resp.content, self.target)
        except Exception as e:
            pass
