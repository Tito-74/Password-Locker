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
def password_generator():
    value = 10
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    num = string.digits
    all = lower + upper + num
    temp = random.sample(all, value)
    genPassword = "".join(temp)

    return genPassword
# print('Do You want Generated Password?')
#         print('Please choose Yes or No')
#         inputPwd = input().lowerCase()
#         if inputPwd = 'no':
#             print('Create Password')
#             createdpasswrd = input()
#         else:
#             print("Your Password is" password_generator())


def main():
    print("Hello Welcome to your Password Locker")
    print("Create a username")
    print('~' * 17)
    username = input()
    print('\n')
    print("Create password for you Password Locker account.")
    print('~' * 47)
    userPassword = input()
    print('\n')
    save_new_user(add_user(username,userPassword))
    print('_'*70)
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
        # """
        # Function to check if the user provided in login exists in the users list.
        # """
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
                    password = "".join(temp)
                else:
                    """
                    Password created by user.
                    """
                    print("\n")
                    print("Please Create a password for your account.")
                    print("~"*41)
                    userPassword = input()
                


if __name__ == '__main__':

    main()
