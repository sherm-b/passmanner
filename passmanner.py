class Account(object):
    def __init__(self, account_name, username, password):
        self._account_name = account_name
        self._username = username
        self._password = password

    @property
    def account_name(self):
        return self._account_name

    @account_name.setter
    def account_name(self, account_name):
        self._account_name = account_name

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        self._username = username

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        if password != self._password:
            validate_change = input(f"Are you sure you want to change your password to [{password}]? (y/n)")
            if validate_change == "y":
                self._password = password
                print("Your password has been changed")
            else:
                return

    def __str__(self):
        return f"{self._account_name} | {self._username} | {self._password}"