#!/usr/bin/env python3.6
from usercredentials import Credentials

def create_credential(uname,fname,email):
    '''
    Function to create a new user credential
    '''
    new_credential = Credentials(uname,fname,email)
    return new_credential

def save_credential(credentials):
    '''
    Function to save new user credentials
    '''
    credentials.save_credential()

def display_credentials():
    '''
    Function that returns all the saved user credentials
    '''
    return Credentials.display_credentials()

def main():

    print("Hey there, Welcome to password locker.What is your name?")

    name = input()
    print(f"Nice to meet you {name}.What are you here for?")
    print('\n')

    while True:
        print("use these shortcodes provided to get to where you want : cc - create a new user account, gp - generate a password, dc - display user credentials, exit - exit usercredentials")
        short_code = input().lower()

        if short_code == 'cc':
            print("New User")
            print('.....')

            print ("User name ....")
            user_name = input()

            print("Last name ...")
            first_name = input()

            print("Email address ...")
            email = input()
