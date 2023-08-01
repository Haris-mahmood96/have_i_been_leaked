import abc

from social_media_osint_api.services.emailosint.email_parser import EmailParser
from social_media_osint_api.services.emailosint.request import Request


class EmailRequest(Request):
    def __init__(self):
        Request.__init__(self)

    @abc.abstractmethod
    def search(self, email=""):
        pass

    @staticmethod
    def get_email(content, target):
        return EmailParser(content, target).email()
