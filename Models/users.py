#This function is responsible for loading/ reading the existing users from the users.json file and returning then as a list of dictionaries.
import json
import os
import hashlib

def load_users():
    if not os.path.exists("Storage/users.json"):
        return []
    with open("Storage/users.json", "r") as file: #opens the file in read mode
        data = json.load(file)
        return data.get("users", [])
    
#This function is responsible for saving the users data to the user.json file    
def save_users(data):
    with open("Storage/users.json", "w") as file: #opens file in write mode and writes the data to the file in a formatted way using json.dump() method.
        json.dump(data, file, indent=4)
        
        
    
    #__________
    #USER CLASS 
    #__________
#Object oriented programming approach to represent a user in the system   

class User:
    def __init__(self, username :str, password:str, role:str):
        self.username = username
        self.password = password
        self.role = role
    
#This method is used to convert the user object into a dictionary format which is easily stored in the JSON file    
    def to_dict(self):
        return {
            "username": self.username,
            "password": self.password,
            "role": self.role
        }
        
"""UserManager handles system authentication and manages accounts for  doctors, and receptionists """      

class UserManager:
    def __init__(self):
        self.users = load_users()   #Loads the existing users from the json file whten the UserManager is initialized.
        self.current_user = None    # session memory /session management . it stores the logged in user (object) information during the session. it sets to none when no user is logged in.
        self.failed_Login_attempts = 0
        self.max_Login_attempts = 5
        
    #password hashing . it uses the hashlib library    
        
    def hash_password(self, password:str):
        return hashlib.sha256(password.encode()).hexdigest()
    
    #User registration    
    def register_user(self, username:str, password:str, role:str):
        for user in self.users:
            if user["username"] == username:
                return "Username already exists.Please enter a different username."
            
            if role not in ["doctor", "receptionist"]:
                return "Invalid role. Role must be either 'doctor' or 'receptionist'."
            
            if len(password) < 6:
                return "Password must be at least 6 characters long."
            
            if not any(char.isdigit() for char in password):
                return "Password must contain at least one digit."
            
            if not any(char.isalpha() for char in password):
                return "Password must contain at least one letter."
            
         
        hashed_password = self.hash_password(password)
                
        new_user = User(username, hashed_password, role)
        self.users.append(new_user.to_dict())
        save_users({"users": self.users})
        
        
        return "User registered successfully."
    
    #Login authentication
    def login_user(self, username:str, password:str):
        hashed_password = self.hash_password(password)
        for user in self.users:
            if user["username"]== username and hashed_password == user["password"]:
                self.current_user = User(user["username"], user["password"], user["role"])
                self.failed_Login_attempts = 0  # Reset failed attempts on successful login
                return f"Welcome! {user['role']} {username}, Login successful."
        
        
        #Failed Login 
        self.failed_Login_attempts += 1
        remaining_attempts = self.max_Login_attempts - self.failed_Login_attempts
        
        if remaining_attempts > 0:
            return f"Invalid username or password. Attempt remaining: {remaining_attempts} ."
        else:
            return "Too many failed login attempts. Access Blocked.Try again later."
        
        
#Logout functionality
    def logout_user(self):
        if self.current_user:
            self.current_user = None
            self.failed_Login_attempts = 0 #reset attempts on logout
            return "Logout Successful."
        else:
            return "No user is currently logged in."

