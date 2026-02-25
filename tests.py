from Utilities.decorators import login_required, role_required
from Models import users, patient, appointment


@login_required
def protected_action(user=None):
    user = user or users.get_current_user()
    print("Protected action executed for", user["username"] if user else "unknown")


@role_required("doctor")
def doctor_action(user=None):
    user = user or users.get_current_user()
    print("Doctor action executed for", user["username"])


@role_required("receptionist")
def receptionist_action(user=None):
    user = user or users.get_current_user()
    print("Receptionist action executed for", user["username"])


def run_tests():
    print("Initially calling protected_action (no user):")
    protected_action()
    print("\nLogging in as receptionist...")
    users.login_user("rec1", "recpass")
    protected_action()
    receptionist_action()
    doctor_action()
    print("\nLogging out and logging in as doctor...")
    users.logout_user()
    users.login_user("doc1", "docpass")
    protected_action()
    doctor_action()
    receptionist_action()
    print("\nDoctor's appointments:", appointment.list_appointments_for_doctor("doc1"))
    print("\nPatients list:", patient.list_patients())


if __name__ == "__main__":
    run_tests()
