from Utilities.decorators import login_required, role_required


class UserObj:
    def __init__(self, username, role):
        self.username = username
        self.role = role


@login_required
def f_requires_login(user=None):
    print("ok-login:", user)


@role_required("doctor")
def f_doctor(user=None):
    print("ok-doctor:", user)


@role_required(["doctor", "receptionist"])
def f_doctor_or_rec(user=None):
    print("ok-doctor-or-rec:", user)


def run():
    print("1) No user -> login_required should deny")
    f_requires_login()

    print("\n2) Dict user with username+role passed as kwarg")
    d = {"username": "d1", "role": "doctor"}
    f_requires_login(user=d)
    f_doctor(user=d)
    f_doctor_or_rec(user=d)

    print("\n3) Dict user passed as first positional arg")
    f_requires_login(d)
    f_doctor(d)

    print("\n4) Object-like user with .username and .role")
    u = UserObj("o1", "receptionist")
    f_requires_login(u)
    f_doctor_or_rec(u)

    print("\n5) Role mismatch: receptionist to doctor-only")
    f_doctor(user={"username": "r1", "role": "receptionist"})


if __name__ == "__main__":
    run()
