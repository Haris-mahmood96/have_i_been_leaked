from social_media_osint_api.services.emailosint.email_request import EmailRequest


class Google(EmailRequest):
    def __init__(self):
        EmailRequest.__init__(self)

    def search(self, email=""):
        print('Searching "%s" in Google...' % email)
        base_url = 'https://www.google.com/search?q=intext:%22%40{target}%22&num=50'.format(
            target=email)
        mails = []
        page = 0
        while page < 7:
            url = base_url + "&start=" + str(page)
            try:
                resp = self.send_request(url)
                if "detected unusual traffic" in resp.text:
                    break
                emails = self.get_email(resp.content, email)
                mails.extend(email for email in emails if email not in mails)
                page += 1
            except Exception as e:
                print("An error occurred:", e)
                break
        return mails
