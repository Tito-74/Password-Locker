import pyperclip
class User:
    user_list = []
    def __init__(self, username, userPassword):
        self.username = username
        self.userPassword = userPassword

   

class Credentials(User):
    credential_list = []
    def __init__(self,username,userPassword,accountName):
        super().__init__(username,userPassword)
        self.accountName = accountName

   

