class Credentials:
    """
    Class that generates new instances of user.
    """

    credentials= []
    def save_credential(self):
        '''
        save_credential method saves user details into credentials
        '''

        Credentials.credentials.append(self)

    @classmethod
    def display_credentials(cls):
        '''
        method that returns the user details
        '''
        return cls.credentials



    def __init__(self, user_name, first_name, email):

        self.user_name = user_name
        self.first_name = first_name
        self.email = email
