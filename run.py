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





if __name__ == '__main__':

    main()
