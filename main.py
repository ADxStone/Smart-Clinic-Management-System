from Models.users import UserManager  # matches your folder structure

def main():
    manager = UserManager()

    # Verification codes for self-registration
    verification_codes = {
        "doctor": "DOC123",
        "receptionist": "REC456"
    }

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
                print(" Invalid role. Must be 'doctor' or 'receptionist'.")
                continue

            # Ask for verification code for the role
            code_input = input(f"Enter {role} verification code: ").strip()
            if code_input != verification_codes[role]:
                print(" Invalid verification code. Cannot register.")
                continue

            # Register user
            result = manager.register_user(username, password, role)
            print(result)

        elif choice == "2":
            print("\n--- LOGIN ---")
            username = input("Enter username: ").strip()
            password = input("Enter password: ").strip()
            result = manager.login_user(username, password)
            print(result)

            if manager.current_user:
                print(f"Logged in as {manager.current_user.role}: {manager.current_user.username}")

        elif choice == "3":
            print("\n--- LOGOUT ---")
            print(manager.logout_user())

        elif choice == "4":
            print("Exiting system. Goodbye!")
            break

        else:
            print(" Invalid option. Please select 1-4.")


if __name__ == "__main__":
    main()