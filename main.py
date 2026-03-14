###################################
#Passmanner By Jeremy Bess
#Final Project for CS162P
#3/13/2026
#DISCLAIMER: This password manager is a student project and is NOT SECURE!!! Don't use this for anything you care about!
#If you get your accounts owned, don't blame me. Use Bitwarden; it's great!
###################################
import passmanner
import os
import csv
import sys

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

def print_help():
    """Prints the help menu"""
    print("[a] - add - Add account details to passmanner vault.\n"
          "[l] - list - List account details in passmanner vault.\n"
          "[s] - search - Search for account details in passmanner vault by account type or username.\n"
          "[d] - delete - Delete account details from passmanner vault.\n"
          "[q] - quit - Quit passmanner.\n"
          "[h] - help - Show this help menu.\n")

def main():
    print("-- passmanner --\n")
    #if vault file doesn't exist, ask to create it
    if 'pmvault.csv' not in os.listdir('.'):
        create_vault()
    #ask if user wants to search for, see, add or delete profile info, accept input
    #conditional tree to selected option, loops if not terminated
    while True:
        input_choice = input("Would you like to [a]dd, [l]ist, [s]earch for, or [d]elete an account?\n"
                             "You can enter 'h' for help, or 'q' to quit.\n"
                             "[a/l/s/d/q/h]: ").strip().lower()
        if input_choice == 'h':
            print_help()

if __name__ == '__main__':
    main()