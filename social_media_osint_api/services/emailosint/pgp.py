from social_media_osint_api.services.emailosint.email_request import EmailRequest


class PGP(EmailRequest):
    def __init__(self):
        EmailRequest.__init__(self)

    def search(self, email=""):
        print('Searching "%s" in PGP...'.format(email))
        url = "http://pgp.mit.edu/pks/lookup?search={target}&op=index".format(
            target=email)
        try:
            resp = self.send(
                method='GET',
                url=url,
                headers={
                    'Host': 'pgp.mit.edu'
                }
            )
            return self.get_email(resp.content, email)
        except Exception as e:
            pass
