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


if __name__ == '__main__':
    unittest.main()
