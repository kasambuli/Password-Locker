import unittest
from password import Credentials

class TestCredentials(unittest.TestCase):

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_credential = Credentials("Kasambuli","Cynthia","cynthiakasambuli@gmail.com")


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_credential.user_name,"Kasambuli")
        self.assertEqual(self.new_credential.first_name,"Cynthia")
        self.assertEqual(self.new_credential.email,"cynthiakasambuli@gmail.com")

    def test_save_credential(self):
        '''
        test_save_contact test case to test if the new log in credentials have been saved to credentials list
        '''
        self.new_credential.save_credential() # saving the new contact
        self.assertEqual(len(Credentials.credentials),1)

    def test_display_credentials(self):
        '''
        method that returns a list of all credentials saved
        '''

        self.assertEqual(Credentials.display_credentials(),Credentials.credentials)

if __name__ == '__main__':
    unittest.main()
