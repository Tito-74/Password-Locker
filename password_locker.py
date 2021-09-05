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
    

class Credentials(User):
    credential_list = []
    def __init__(self,username,userPassword,accountName):
        super().__init__(username,userPassword)
        self.accountName = accountName

   

