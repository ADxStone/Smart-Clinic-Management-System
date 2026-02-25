users = [
    {"username": "doc1", "password": "docpass", "role": "doctor"},
    {"username": "rec1", "password": "recpass", "role": "receptionist"},
]

current_user = None


def get_user_by_username(username):
    for u in users:
        if u["username"] == username:
            return u
    return None


def login_user(username, password):
    global current_user
    u = get_user_by_username(username)
    if u and u["password"] == password:
        current_user = u
        return True
    return False


def logout_user():
    global current_user
    current_user = None


def get_current_user():
    return current_user
