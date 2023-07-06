from models import User_details

class UserService:
    def signup(self,username : str, password : str):
        users=User_details.create(username=username,password=password)
        print(f"{users.username} Signed Up!!")
        
        
