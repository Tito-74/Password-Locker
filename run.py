#!/usr/bin/env python3
import random 
import string
from password_locker import User
from password_locker import Credentials

#user Functions
def add_user(username,userPassword):
    '''
    function to add new user 
    '''
    new_user= User(username,userPassword)
    return new_user
def save_new_user(user):
    '''
    Function to save credential
    '''
    user.save_user()
def find_user(username,userPassword):
    '''
    Function that finds a credential by number and returns the credential
    '''
    return User.find_user(username,userPassword)
def check_existing_user(username,userPassword):
    '''
    Function that check if a user exists with that number and return a Boolean
    '''
    return User.user_exist(username,userPassword)

# Credential Functions
def add_credential(username,userPassword,accountName):
    '''
    function to add new credential 
    '''
    new_credential= Credentials(username,userPassword,accountName)
    return new_credential

def save_credential(credential):
    '''
    Function to save credential
    '''
    credential.save_credential()

def del_credential(credential):
    '''
    Function to delete a credential
    '''
    credential.delete_credential()

def find_credential(account):
    '''
    Function that finds a credential by number and returns the credential
    '''
    return Credentials.find_by_account(account)

def check_existing_credential(account):
    '''
    Function that check if a credential exists with that number and return a Boolean
    '''
    return Credentials.credential_exist(account)

def display_credential():
    '''
    Function that returns all the saved credential
    '''
    return Credentials.display_credential()
def password_choice(quiz):
    """
    Function that defines mode of password creation.
    """
    user_choice = None
    while user_choice not in ("yes", "no"):
        user_choice = input(quiz).lower()
    return user_choice


def main():
    print("Hello Welcome to your Password Locker")
    print("Create a username")
    print('~' * 17)
    username = input()
    print('\n')
    print("Create password for you Password Locker account.")
    print('~' * 40)
    userPassword = input()
    print('\n')
    save_new_user(add_user(username,userPassword))
    print('_'*65)
    print("\n")
    print(f"Hello {username}, Thank you for creating an account with us.")
    print('\n')
    print("Proceed to Login")
    print('\n')
    print("Enter your username:")
    print('~' * 20)
    account_username = input()
    print('\n')
    print("Enter your password:")
    print('~' * 20)
    account_password = input()
    print('\n')
    if check_existing_user(account_username, account_password):
        """
        Function to check if the user provided in login exists in the users list.
        """
        get_user = find_user(account_username, account_password)


        while True:
            print("Use these short codes :  C- create a new Credential, D - display credentials, F -find a credentials, R -To delete an existing account credentials., Q -exit the contact list ")
            print("What would you like to do?")
            short_code = input().upper()
            if short_code == 'C':
                    print("New Credential Account")
                    print("~"*22)
                    print("Enter Account Type")
                    print("~"*18)
                    accountName = input()
                    print("\n")
                    print("Enter it's Username")
                    print("~"*19)
                    username = input()
                    print("\n")
                    # Password generation
                    password_creation = password_choice(
                        "Would you like to have your password generated?(yes/no)"
                    )
                    if password_creation == "yes":
                        """
                        Autogenerate password code.
                        """
                        value = 16
                        lower = string.ascii_lowercase
                        upper = string.ascii_uppercase
                        num = string.digits
                        all = lower + upper + num
                        temp = random.sample(all, value)
                        userPassword = "".join(temp)
                    else:
                        """
                        Password created by user.
                        """
                        print("\n")
                        print("Please Create a password for your account.")
                        print("~"*41)
                        userPassword = input()
                    # Saving the new credentials
                    save_credential(add_credential(accountName, username,userPassword))
                    print('\n')
                    print("ACCOUNT CREDENTIALS SUCCESSFULLY SAVED.")
                    print("~"*38)
                    print(f"TYPE--->{accountName} account.")
                    print(f"USERNAME--->{username}")
                    print(f"PASSWORD--->{userPassword}")
                    print('\n')
            elif short_code == 'D':
                if display_credential():
                    print("Here is a list of all your accounts")
                    print('~'*35)
                    for credential in display_credential():
                        print(f"Account Name--->{credential.accountName} account.")
                        print(f"USERNAME--->{credential.username}")
                        print(f"PASSWORD--->{credential.userPassword}")
                        print('-'*33)
                else:
                    print('\n')
                    print(
                        "We can't seem to find any accounts saved in your account. \nMake sure have have successfuly created first.")
                    print('\n')

            elif short_code == 'F':
                    print("Enter the account name you would like to find.")
                    print('~'*40)
                    find_accounts = input()
                    print('\n')
                    if check_existing_credential(find_accounts):
                        search_account = find_credential(find_accounts)
                        print("RESULTS")
                        print("~"*6)
                        print(f"Account Name ~~~>{search_account.accountName}")
                        print(f"Username ~~~>{search_account.username}")
                        print(f"Password ~~~>{search_account.userPassword}")
                    else:
                        print(
                            "We can find the account you are looking for! \nCheck the account you provided and try again.")
                    print('\n')
            elif short_code == 'R':
                    print("Enter name of account to delete")
                    print("~"*31)
                    find_accounts = input()
                    print("\n")
                    if check_existing_credential(find_accounts):
                        search_account = find_credential(find_accounts)
                        del_credential(search_account)
                        print(
                            f"{search_account.accountName}Account deleted successfully")
                    else:
                        print('\n')
                        print(
                            "We can find the account you are looking for! \nCheck the accounts you have and try again.")
            elif short_code == "Q":
                print("Thanks for choosing Password Locker. Bye.")
                break
            else:
                print(
                    "I  didn't get that. Please make sure you use the abbreviations to perform an operation.")
    else:
        print("That account does not exist. Please create one")
        print('\n')
         

if __name__ == '__main__':

    main()
