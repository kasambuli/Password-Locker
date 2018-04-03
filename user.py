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
