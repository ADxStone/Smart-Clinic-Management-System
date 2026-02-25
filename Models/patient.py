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
                data["patients"].remove(patient)
                save_data(data)
                print("Patient deleted.")
                return

        print("Patient not found.")

if __name__ == "__main__":
    Patient.register_patient()
    Patient.view_patients()
    Patient.search_patients()
    Patient.delete_patients()

 
