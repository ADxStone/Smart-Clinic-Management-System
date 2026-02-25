users = []
current_user = None


def get_user_by_username(username):
    return None


def login_user(username, password):
    return False


def logout_user():
    global current_user
    current_user = None


def get_current_user():
    return current_user
