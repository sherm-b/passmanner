import csv
import os
import sys

class Account(object):
    def __init__(self, account_type, username, password):
        self._account_type = account_type
        self._username = username
        self._password = password

    @property
    def account_type(self):
        return self._account_type

    @account_type.setter
    def account_type(self, account_type):
        self._account_type = account_type

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
        self._password = password

def create_vault():
    """Creates a 'vault' csv to store account details"""
    #could add option to have user specify path to vault file if it's not in main dir
    create_vault_input = input('No vault file found. Would you like to create one? [y/n] ')
    input_invalid = True
    while input_invalid:
        if create_vault_input.strip().lower() == 'y':
            #create and initialize vault csv with header
            with open('pmvault.csv', 'w', newline='') as vault_file:
                vault_writer = csv.writer(vault_file)
                vault_writer.writerow(['#', 'account_type', 'username', 'password'])
                print(f"Vault created at {os.getcwd()}\\pmvault.csv\n")
                input_invalid = False
        elif create_vault_input.strip().lower() == 'n':
            sys.exit("passmanner needs a vault file to function. Exiting...")
        else:
            create_vault_input = input("Please enter a valid input. [y/n] ")

def add_to_vault(account):
    """Adds account details to vault"""
    with open('pmvault.csv', 'r+', newline='') as vault_file:
        vault_writer = csv.writer(vault_file)
        last_row = vault_file.readlines()[-1]
         #Checks if there is an item before the new one, increments the list value by one, and adds account details.
        if last_row[0] == '#':
            vault_writer.writerow(['1', f'{account.account_type}', f'{account.username}', f'{account.password}'])
        else:
            vault_writer.writerow([f"{str(int(last_row[0]) + 1)}", f'{account.account_type}', f'{account.username}', f'{account.password}'])

def add_account():
    """Creates an account object and passes it to the add_to_vault function"""
    #these loops are messy, going to mess around with this and try to clean it up
    trying_to_add = True
    while trying_to_add:
        account_type = input("Please enter the service this account is for: ")
        username = input("Please enter your username: ")
        password = input("Please enter your password: ")
        acct = Account(account_type, username, password)
        print("\n- Account Details -\n"
              f"Account Type: {acct.account_type}\n"
              f"Username: {acct.username}\n"
              f"Password: {acct.password}\n")
        check_details = input("Double check your details. Does this look correct? [y/n] ").strip().lower()
        while check_details:
            if check_details == "y":
                add_to_vault(acct)
                print(f"Account details for {acct.account_type} added successfully.\n")
                trying_to_add = False
                check_details = False
            elif check_details != "n":
                check_details = input("Please enter a valid input. [y/n] ")
            else:
                check_details = False

def list_vault():
    """Prints out the vault details"""
    with open('pmvault.csv', 'r', newline='') as vault_file:
        vault_reader = csv.reader(vault_file)
        #find length of longest items in each column to build formatting around
        longest_items = []
        for row in vault_reader:
            for item in row:
                if len(longest_items) < 4:
                    longest_items.append(len(item))
                if longest_items[row.index(item)] < len(item):
                    longest_items[row.index(item)] = len(item)
    #reopen file to reset reader cursor
    with open("pmvault.csv", 'r', newline='') as vault_file:
        vault_reader = csv.reader(vault_file)
        for row in vault_reader:
            print(f" {row[0]: ^{longest_items[0]}} | {row[1]: ^{longest_items[1]}} | {row[2]: ^{longest_items[2]}} | {row[3]: ^{longest_items[3]}}")

def search_vault():
    """Searches for specific account details in vault"""
    search_term = input("Enter Account Type or Username: ")
    found_one_yet = False
    #preserve search term in form entered for use in success message
    search_term_strip_lower = search_term.strip().lower()
    with open('pmvault.csv', 'r', newline='') as vault_file:
        vault_reader = csv.reader(vault_file)
        for row in vault_reader:
            for item in row:
                #checks if search term is in row, excluding passwords.
                if search_term_strip_lower == item.lower().strip() and search_term_strip_lower != row[3]:
                    #checks if success message has already been printed, skips otherwise
                    if found_one_yet == False:
                        found_one_yet = True
                        print(f"\nAccount details for {search_term} found successfully.\n"
                              f"Account Type: {row[1]}\n"
                              f"Username: {row[2]}\n"
                              f"Password: {row[3]}\n")
                    else:
                        print(f"Account Type: {row[1]}\n"
                              f"Username: {row[2]}\n"
                              f"Password: {row[3]}")
    if found_one_yet == False:
        print(f"No account details found for {search_term}.")

def delete_from_vault():
    """Deletes account details from vault"""
    start_delete = False
    list_vault()
    #get the list item number that the user wishes to delete
    delete_account = input("Which account details do you want to delete?\n"
                           "Input account number (first column), or enter nothing to abort: ").strip().lower()
    with open('pmvault.csv', 'r+', newline='') as vault_file:
        vault_reader = csv.reader(vault_file)
        for row in vault_reader:
            #checks deletion candidate is found, stops looping when it is
            if not start_delete:
                if row[0] == delete_account:
                    if delete_check(row):
                        vault_file.seek(0)
                        lines = vault_file.readlines()
                        start_delete = True
    if start_delete:
        with open("pmvault.csv", 'w', newline='') as vault_file:
            vault_writer = csv.writer(vault_file, delimiter=',')
            #write all lines in file except for the selected deletion line
            for line in lines:
                line = line.strip()
                #makes sure header never gets deleted
                if line[0] == '#':
                    vault_writer.writerow(line.split(','))
                #if line comes after deleted line, decrement number by one
                elif line[0] != delete_account and int(line[0]) > int(delete_account):
                    line = line.replace(line[0], str(int(line[0]) - 1), 1)
                    vault_writer.writerow(line.split(','))
                elif line[0] != delete_account:
                    vault_writer.writerow(line.split(','))
        print(f"Details deleted successfully.")
    else:
        #if deletion candidate isn't found, print this
        print(f"No account details found for {delete_account}. Deletion aborted.")

def delete_check(acct):
    """Double checks if user wants to delete the account details"""
    check_input = input("Are you sure you want to delete these details?\n"
                      f"Please type [{acct[3]}] to confirm: ")
    if check_input == acct[3]:
        print(f"Deleting account details for {acct[1]}.\n")
        return True
    else:
        print("Deletion aborted.\n")
        return False