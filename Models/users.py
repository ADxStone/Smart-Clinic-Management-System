import json
import os
import hashlib


def load_users():
    if not os.path.exists("Storage/users.json"):
        return []
    with open("Storage/users.json", "r") as file:
        data = json.load(file)
        return data.get("users", [])


def save_users(data):
    with open("Storage/users.json", "w") as file:
        json.dump(data, file, indent=4)


class User:
    def __init__(self, username: str, password: str, role: str):
        self.username = username
        self.password = password
        self.role = role

    def to_dict(self):
        return {"username": self.username, "password": self.password, "role": self.role}


class UserManager:
    def __init__(self):
        self.users = load_users()
        self.current_user = None
        self.failed_Login_attempts = 0
        self.max_Login_attempts = 5

    def hash_password(self, password: str):
        return hashlib.sha256(password.encode()).hexdigest()

    def register_user(self, username: str, password: str, role: str):
        for user in self.users:
            if user.get("username") == username:
                return "Username already exists. Please enter a different username."

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

    def login_user(self, username: str, password: str):
        hashed_password = self.hash_password(password)
        for user in self.users:
            stored = user.get("password")
            if user.get("username") == username and (stored == hashed_password or stored == password):
                self.current_user = User(user["username"], stored, user.get("role"))
                self.failed_Login_attempts = 0
                return f"Welcome! {user.get('role')} {username}, Login successful."

        self.failed_Login_attempts += 1
        remaining_attempts = self.max_Login_attempts - self.failed_Login_attempts

        if remaining_attempts > 0:
            return f"Invalid username or password. Attempt remaining: {remaining_attempts} ."
        else:
            return "Too many failed login attempts. Access Blocked.Try again later."

    def logout_user(self):
        if self.current_user:
            self.current_user = None
            self.failed_Login_attempts = 0
            return "Logout Successful."
        else:
            return "No user is currently logged in."

    def get_current_user(self):
        return self.current_user
