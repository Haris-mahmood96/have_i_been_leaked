import re


class EmailParser:
    def __init__(self, content, target):
        self.target = target
        self.content = str(content)

    def email(self):
        # email_regex variable which constructs the regular expression pattern for matching email addresses.
        # The re.escape() function is used to escape special characters in the target domain to ensure they are
        # treated as literals in the pattern.
        email_regex = r'[a-zA-Z0-9.\-_+#~!$&\',;=:]+@' + re.escape(self.target)

        # The tmp_emails variable stores the results of applying re.findall() with the email_regex pattern on the
        # cleaned content obtained from the clean property.
        tmp_emails = re.findall(email_regex, self.clean)

        # Instead of manually creating a new email_list, the tmp_emails list is converted to a set to remove duplicates
        # and then converted back to a list using list(set(tmp_emails)).
        email_list = list(set(tmp_emails))

        # The filtered_emails list comprehension is used to filter out email addresses where the part before the '@'
        # symbol starts with a single or double quote using the startswith() method.
        filtered_emails = [email for email in email_list if not email.split('@')[0].startswith(("'", '"'))]
        return filtered_emails

    # The clean method is transformed into a property using the @property decorator for improved code readability.
    # The regular expressions remove various HTML tags (such as <em>, <b>, <strong>, <wbr>) from the content using
    # re.sub(). Characters such as >, :, =, <, /, \, ;, &, %3A, %3D, and %3C are replaced with a space using re.sub()
    # to clean up the content.
    @property
    def clean(self):
        content = re.sub(r'<(?:em|b|strong|wbr)>', '', self.content)
        content = re.sub(r'</(?:em|b|strong|wbr)>', '', content)
        content = re.sub(r'<[a-zA-Z]+>', '', content)
        content = re.sub(r'</[a-zA-Z]+>', '', content)
        content = re.sub(r'[>:=/\\;&%3A%3D%3C]', ' ', content)
        return content
