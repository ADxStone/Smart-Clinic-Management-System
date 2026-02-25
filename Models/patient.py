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

if __name__ == "__main__":
    Patient.register_patient()
    Patient.view_patients()

 
