from Models.users import UserManager
from Models.patient import list_patients
from Models.appointment import list_appointments_for_doctor
from Utilities.decorators import login, role


@login
@role("doctor")
def doctor_menu(manager: UserManager, user=None):
    while True:
        print("\n--- DOCTOR MENU ---")
        print("1. View my appointments- Not complete")
        print("2. Mark appointment completed - Not complete")
        print("3. View all complete appointments - Not complete")
        print("4. Back / Logout")
        choice = input("Select (1-3): ").strip()
        if choice == "1":
            username = user.username if hasattr(user, 'username') else user.get('username')
            appts = list_appointments_for_doctor(username)
            print("Appointments for", username, appts)
        elif choice == "2":
            print("Example: No logic implemented")
        elif choice == "3":
            print("Example: No logic implemented")
        elif choice == "4":
            print(manager.logout_user())
            break
        else:
            print("Invalid option")


@login
@role("receptionist")
def receptionist_menu(manager: UserManager, user=None):
    while True:
        print("\n--- RECEPTIONIST MENU ---")
        print("1.Register patient. - Not complete")
        print("2.List patients - Not complete ")
        print("3.Create appointment-Not complete")
        print("4.View appointments(1.For each patient, 2. For each doctor)-Not complete")
        print("5. Back / Logout")
        choice = input("Select (1-3): ").strip()
        if choice == "1":
            print("Example: No logic implemented.")
        elif choice == "2":
            pats = list_patients()
            print("Patients:", pats)
        elif choice == "3":
            print("Example: create appointment (No logic implemented)")
        elif choice == "4":
            print("Example: View appointments(No logic implemented)")
        elif choice == "5":
            print(manager.logout_user())
            break
        else:
            print("Invalid option")


def main():
    manager = UserManager()

    verification_codes = {"doctor": "DOC123", "receptionist": "REC456"}

    while True:
        print("\n=== SMART CLINIC MANAGEMENT SYSTEM ===")
        print("1. Register User")
        print("2. Login")
        print("3. Logout")
        print("4. Exit")

        choice = input("Select an option (1-4): ").strip()

        if choice == "1":
            print("\n--- REGISTER USER ---")
            username = input("Enter username: ").strip()
            password = input("Enter password: ").strip()
            role = input("Enter role (doctor/receptionist): ").strip().lower()

            if role not in ["doctor", "receptionist"]:
                print("Invalid role. Must be 'doctor' or 'receptionist'.")
                continue

            code_input = input(f"Enter {role} verification code: ").strip()
            if code_input != verification_codes[role]:
                print("Invalid verification code. Cannot register.")
                continue

            result = manager.register_user(username, password, role)
            print(result)

        elif choice == "2":
            print("\n--- LOGIN ---")
            username = input("Enter username: ").strip()
            password = input("Enter password: ").strip()
            result = manager.login_user(username, password)
            print(result)

            if manager.current_user:
                role_name = manager.current_user.role.lower()
                if role_name == "doctor":
                    doctor_menu(manager, user=manager.current_user)
                elif role_name == "receptionist":
                    receptionist_menu(manager, user=manager.current_user)
                else:
                    print("Unknown role; contact admin.")

        elif choice == "3":
            print("\n--- LOGOUT ---")
            print(manager.logout_user())

        elif choice == "4":
            print("Exiting system. Goodbye!")
            break

        else:
            print("Invalid option. Please select 1-4.")


if __name__ == "__main__":
    main()
