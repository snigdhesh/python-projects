from models.User import User
from services import utils

def main():
    user = User()
    username= user.getUserName()
    userObj = user.getUser()
    print(f"username is {username}")
    print(f"user is {userObj}")

if __name__ == '__main__':
    main()