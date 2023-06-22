from social_media_osint_api.services.emailosint.email_request import EmailRequest


class PGP(EmailRequest):
    def __init__(self, target):
        EmailRequest.__init__(self)
        self.target = target

    def search(self, email=""):
        print('Searching "%s" in PGP...'.format(self.target))
        url = "http://pgp.mit.edu/pks/lookup?search={target}&op=index".format(
            target=self.target)
        try:
            resp = self.send(
                method='GET',
                url=url,
                headers={
                    'Host': 'pgp.mit.edu'
                }
            )
            return self.get_email(resp.content, self.target)
        except Exception as e:
            pass
