import json

DATA_FILE = "Storage/patients.json"

def load_patients():
    with open(DATA_FILE, "r") as file:
        return json.load(file)

def save_patients(patients):
    with open(DATA_FILE, "w") as file:
        json.dump(patients, file, indent=4)


class Patient:

    @staticmethod
    def register_patient():
        data = load_patients()

        name = input("Enter patient name: ")
        age = input("Enter age: ")
        condition = input("Enter condition: ")

        patient_id = "p" + str(len(data) + 1)

        new_patient = {
            "id": patient_id,
            "name": name,
            "age": age,
            "condition": condition
        }

        data.append(new_patient)
        save_patients(data)

        print("Patient registered successfully!")


    @staticmethod
    def view_patients():
        data = load_patients()

        for patient in data:
            print("-----------------------")
            print("ID", patient["id"])
            print("Name", patient["name"])
            print("Age", patient["age"])
            print("Condition", patient["condition"])

    @staticmethod
    def update_patients():
        data = load_patients()
        patient_id = input("Enter patient ID to update: ")

        for patient in data:
            if patient["id"] == patient_id:

                print("Leave black to keep current value.")

                new_name = input(f"New name ({patient['name']}): ")
                new_age = input(f"New age ({patient['age']}): ")
                new_condition = input(f"New condition ({patient['condition']}): ")

                if new_name != "":
                    patient["name"] = new_name

                if new_age != "":
                    patient["age"] = new_age

                if new_condition != "":
                    patient["condition"]

                save_patient(data)
                print("Patient updated successfuly")
                return

        print("Patient not found.")


    @staticmethod
    def search_patients():
        data = load_patients()
        search_id = input("Enter patient ID: ") 

        for patient in data:
            if patient["id"] == search_id:
                print("Patient found: ")
                print(patient)
                return

        print("Patient not found.")

    @staticmethod
    def delete_patients():
        data = load_patients()
        patient_id = input("Enter patient ID to delete: ")

        for patient in data:
            if patient["id"] == patient_id:
                data.remove(patient)
                save_patients(data)
                print("Patient deleted.")
                return

        print("Patient not found.")

if __name__ == "__main__":
    Patient.register_patient()
    Patient.view_patients()
    Patient.search_patients()
    Patient.delete_patients()

 


#This Part of Code is From main.py
from Models.patient import Patient

def receptionist_menu():
    while True:
        print("\n--- Receptionist Menu ---")
        print("1. Register Patient")
        print("2. View Patients")
        print("3. Search Patient")
        print("4. Update Patient")
        print("5. Delete Patient")
        print("6. Back")

        choice = input("Choose option: ")

        if choice == "1":
            Patient.register_patient()
        elif choice == "2":
            Patient.view_patients()
        elif choice == "3":
            Patient.search_patients()
        elif choice == "4":
            Patient.update_patients()
        elif choice == "5":
            Patient.delete_patients()
        elif choice == "6":
            break
        else:
            print("Invalid choice.")

        
if __name__ == "__main__":
    receptionist_menu()
