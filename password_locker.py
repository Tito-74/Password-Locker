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
    
class Credentials(User):
    credential_list = []
    def __init__(self,username,userPassword,accountName):
        super().__init__(username,userPassword)
        self.accountName = accountName

   

