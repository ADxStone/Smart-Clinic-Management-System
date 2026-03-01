from Models.users import UserManager
from Models.appointment import Appointment
from Utilities.decorators import login, role
from Models.patient import Patient

@login
@role("doctor")
def doctor_menu(manager: UserManager, user=None):
    while True:
        print("\n--- DOCTOR MENU ---")
        print("1. View my appointments")
        print("2. Mark appointment completed")
        print("3. View all complete appointments")
        print("4. Back / Logout")
        choice = input("Select (1-4): ").strip()
        if choice == "1":
            Appointment.view_doctor(
                {"username": user.username}
            )
        elif choice == "2":
            Appointment.complete(
                {"username": user.username}
            )
            
        elif choice == "3":
            print("completed appointments:")
            Appointment.view_all()
            
        elif choice == "4":
            print(manager.logout_user())
            break
        else:
            print("Invalid option")


@login
@role("receptionist")
def receptionist_menu(manager: UserManager, user=None):
    while True:
        print("1. Register patient")
        print("2. List patients")
        print("3. Update patient")
        print("4. Delete patient")
        print("5. Create appointment")
        print("6. View appointments")
        print("7. Back / Logout")
        choice = input("Select (1-7): ").strip()
        print("")
        if choice == "1":
            Patient.register_patient()

        elif choice == "2":
            Patient.view_patients()

        elif choice == "3":
            Patient.update_patients()

        elif choice == "4":
            Patient.delete_patients()

        elif choice == "5":
            Appointment.create({"username": user.username})

        elif choice == "6":
            Appointment.view_all()

        elif choice == "7":
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
        print("3. Exit")

        choice = input("Select an option (1-3): ").strip()

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
            print("")
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
            print("Exiting system. Goodbye!")
            break

        else:
            print("Invalid option. Please select 1-4.")
            

if __name__ == "__main__":
    main()