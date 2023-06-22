import abc

from social_media_osint_api.services.emailosint.email_parser import EmailParser
from social_media_osint_api.services.request import Request


class EmailRequest(Request):
    def __init__(self, target):
        Request.__init__(self)
        self.target = target

    @abc.abstractmethod
    def search(self, email=""):
        pass

    @staticmethod
    def get_email(content, target):
        return EmailParser(content, target).email()