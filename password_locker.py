import pyperclip
class User:
    user_list = []
    def __init__(self, username, userPassword):
        self.username = username
        self.userPassword = userPassword

    def save_user(self):
        '''
        Function to save user
        '''
        User.user_list.append(self)
    @classmethod
    def user_exist(cls,username,userPassword):
        # '''
        # Method that checks if a credential exists from the credential list.
        # Args:
        #     number: Phone number to search if it exists
        # Returns :
        #     Boolean: True or false depending if the credential exists
        # '''
        for user in cls.user_list:
            if user.username == username and user.userPassword == userPassword:
                    return True

        return False
    @classmethod
    def find_user(cls,username,userPassword):
        '''
        Method that takes in a number and returns a credential  that matches that number.

        Args:
            number: Phone number to search for
        Returns :
            credential of person that matches the number.
        '''

        for user in cls.user_list:
            if user.username == username and user.userPassword == userPassword:
                return user

class Credentials(User):
    credential_list = []
    def __init__(self,username,userPassword,accountName):
        super().__init__(username,userPassword)
        self.accountName = accountName

    def save_credential(self):

        '''
        save_credentials method saves credentials objects into credential_list
        '''
    
        Credentials.credential_list.append(self)

    def delete_credential(self):

        '''
        delete_credential method deletes a saved credential from the credential_list
        '''

        Credentials.credential_list.remove(self)
    
    
    @classmethod
    def find_by_account(cls,account):
        '''
        Method that takes in a number and returns a credential  that matches that number.

        Args:
            number: Phone number to search for
        Returns :
            credential of person that matches the number.
        '''

        for credential in cls.credential_list:
            if credential.accountName == account:
                return credential

    @classmethod
    def credential_exist(cls,account):
        '''
        Method that checks if a credential exists from the credential list.
        Args:
            number: Phone number to search if it exists
        Returns :
            Boolean: True or false depending if the credential exists
        '''
        for credential in cls.credential_list:
            if credential.accountName == account:
                    return True

        return False

    @classmethod
    def display_credential(cls):
        '''
        method that returns the credentials list
        '''
        
        return cls.credential_list

    @classmethod
    def copy_userPassword(cls, account):
        credential_found = Credentials.find_by_account(account)
        pyperclip.copy(credential_found.userPassword)


# user1 = Credentials('tito','1234','twitter')
# user2 = Credentials('kipkirui','4321','facebook')
# print(credential_found)

