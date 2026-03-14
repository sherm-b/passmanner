import csv
import os
import sys

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

def create_vault():
    """Creates a 'vault' csv to store account details"""
    create_vault_input = input('No vault file found. Would you like to create one? [y/n] ')
    input_invalid = True
    while input_invalid:
        if create_vault_input.strip().lower() == 'y':
            #create and initialize vault csv with header
            with open('pmvault.csv', 'w', newline='') as vault_file:
                vault_writer = csv.writer(vault_file)
                vault_writer.writerow(['#', 'account_name', 'username', 'password'])
                print(f"Vault created at {os.getcwd()}\\pmvault.csv\n")
                input_invalid = False
        elif create_vault_input.strip().lower() == 'n':
            sys.exit("passmanner needs a vault file to function. Exiting...")
        else:
            create_vault_input = input("Please enter a valid input. [y/n] ")