###################################
#Passmanner By Jeremy Bess
#Final Project for CS162P
#3/13/2026
#DISCLAIMER: This password manager is a student project and is NOT SECURE!!! Don't use this for anything you care about!
#If you get your accounts owned, don't blame me. Use Bitwarden; it's great!
###################################
import passmanner, os, sys

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
        passmanner.create_vault()
    #ask if user wants to search for, see, add or delete profile info, accept input
    #conditional tree to selected option, loops if not terminated with q option
    print("Would you like to [a]dd, [l]ist, [s]earch for, or [d]elete an account?\n"
          "You can enter '?' for help, or 'q' to quit.")
    while True:
        input_choice = input("\n[a/l/s/d/h/?]: ").strip().lower()
        if input_choice == '?':
            print_help()
        if input_choice == 'q':
            sys.exit("Thank you for using passmanner. Exiting...")
        if input_choice == 'a':
            passmanner.add_account()
        if input_choice == 'l':
            passmanner.list_vault()
        if input_choice == 's':
            passmanner.search_vault()


if __name__ == '__main__':
    main()