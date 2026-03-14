###################################
#Passmanner By Jeremy Bess
#Final Project for CS162P
#3/13/2026
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
                print(f"Vault created at {os.getcwd()}\\pmvault.csv")
                input_invalid = False
        elif create_vault_input.strip().lower() == 'n':
            sys.exit("passmanner needs a vault file to function. Exiting...")
        else:
            create_vault_input = input("Please enter a valid input. [y/n] ")


def main():
    print("-- passmanner --\n")
    #if vault file doesn't exist, ask to create it
    if 'pmvault.csv' not in os.listdir('.'):
        create_vault()
    #ask if user wants to search for, see, add or delete profile info, accept input
    #conditional tree to selected option, loops if not terminated

if __name__ == '__main__':
    main()