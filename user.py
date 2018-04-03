#!/usr/bin/env python3.6
import random
from usercredentials import Credentials

def create_credential(u_name,f_name,email):
    '''
    Function to create a new user credential
    '''
    new_credential = Credentials(u_name,f_name,email)
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
            u_name = input()

            print("First name ...")
            f_name = input()

            print("Email address ...")
            email = input()

            save_credential(create_credential(u_name,f_name,email)) # create and save new credential
            print ('\n')
            print(f"New User {u_name} ,{f_name} ,{email} created")
            print ('\n')


        elif short_code == 'dc':

            if display_credentials():
                print("Here is a list of all your details")
                print('\n')


            for credential in display_credentials():
                print(f"{credential.user_name} ,{credential.first_name} ,{email}")

                print('\n')
        elif short_code == 'gp':
            print("input username")
            username = input()
            if username == u_name:
                characters = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ?()@#$%^&*!"
                length = len(characters)
                print("Give your preferred password length")
                passwordlength = int(input())
                password = "".join(random.sample(characters,passwordlength ))
                print ('\n')

                print(password)
            else:
                print("wrong username")

        elif short_code == "exit":
            print("Good Bye .......")
            break
        else:
            print("I really didn't get that. Please use the short codes")


if __name__ == '__main__':

    main()
