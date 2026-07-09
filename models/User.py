class User:
    name = "John"
    email = "John@gmail.com"

    def __init__(self):
        pass

    def getUserName(self):
        return self.name
    
    def getUser(self):
        return self.name +":"+ self.email
    