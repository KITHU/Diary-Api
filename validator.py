"""to check if user has correctl
input before storing to database"""

import re

class Validate():
    """class to ensure users input are valid"""

    def valid_email(self, email):
        """valid email and return true or false """

        self.email = email
        match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email)# pylint: disable=anomalous-backslash-in-string
        if match is None:
            return False
        return True

    def valid_username(self, kastring):
        """valid strings usernames and return true or false """

        self.kastring = kastring
        match = re.match('^[_a-zA-Z]+[a-z]{0,9}', kastring)
        if match is None:
            return False
        return True

    def valid_title(self, title):
        """valid title check """

        #self.title = title
        match = re.match('^[_a-zA-Z]', title)
        if match is None:
            return False
        if len(title) < 2:
            return False
        return True



