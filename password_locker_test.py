import unittest
import pyperclip
from password_locker import User
from password_locker import Credentials

class TestCredentials(unittest.TestCase):
    '''
    Test class that defines test cases for the credential class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
        # Items up here .......
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_credential = Credentials("Tito","22222","accountK") # create credential object
    
    def test_init(self):

        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_credential.username,"Tito")
        self.assertEqual(self.new_credential.userPassword,"22222")
        self.assertEqual(self.new_credential.accountName,"accountK")
        

   





if __name__ == '__main__':
    unittest.main()