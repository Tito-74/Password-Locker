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


if __name__ == '__main__':

    main()
