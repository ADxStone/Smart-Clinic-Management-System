import json

DATA_FILE = "Storage/patients.json"

def load_patients():
    with open(DATA_FILE, "r") as file:
        return json.load(file)

def save_patients(patients):
    with open(DATA_FILE, "w") as file:
        json.damp(patients, file, indent=4)