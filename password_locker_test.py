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
        

    def test_save_credential(self):
        '''
        test_save_credential test case to test if the credential object is saved into
         the credential list
        '''
        self.new_credential.save_credential() 
        self.assertEqual(len(Credentials.credential_list),1)

    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            Credentials.credential_list = []
    
    def test_save_multiple_credential(self):
            '''
            test_save_multiple_credential to check if we can save multiple credential
            objects to our credential_list
            '''
            self.new_credential.save_credential()
            test_credential = Credentials("Test","0000","userAccount") # new credential
            test_credential.save_credential()
            self.assertEqual(len(Credentials.credential_list),2)

    def test_delete_credential(self):
            '''
            test_delete_credential to test if we can remove a credential from our credential list
            '''
            self.new_credential.save_credential()
            test_credential = Credentials("Test","0000","userAccount")
            test_credential.save_credential()

            self.new_credential.delete_credential()
            self.assertEqual(len(Credentials.credential_list),1)

    def test_find_credential_by_account(self):
        '''
        test to check if we can find a credential by phone number and display information
        '''

        self.new_credential.save_credential()
        test_credential = Credentials("Test","0000","userAccount") # new contact
        test_credential.save_credential()

        found_credential = Credentials.find_by_account("userAccount")

        self.assertEqual(found_credential.username,test_credential.username)
    
    def test_credential_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the credential.
        '''

        self.new_credential.save_credential()
        test_credential = Credentials("Test","0000","userAccount") # new credential
        test_credential.save_credential()

        credential_exists = Credentials.credential_exist("userAccount")

        self.assertTrue(credential_exists)

    def test_display_credential(self):
        '''
        method that returns a list of all credential saved
        '''

        self.assertEqual(Credentials.display_credential(),Credentials.credential_list)

    def test_copy_userPassword(self):
        '''
        Test to confirm that we are copying the userpassword address from a found credential
        '''

        self.new_credential.save_credential()
        Credentials.copy_userPassword("accountK")

        self.assertEqual(self.new_credential.userPassword, pyperclip.paste())
    
   






if __name__ == '__main__':
    unittest.main()