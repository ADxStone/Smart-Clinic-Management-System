import json
import os

APPOINTMENTS_FILE = "appointments.json"
PATIENTS_FILE = "patients.json"

class Appointment:
    
    @staticmethod
    def load_data(file):
        if not os.path.exists(file):
            return[]
        with open(file, "r") as f:
            return json.load(f)
        
    @staticmethod
    def save_data(file, data):
        with open(file, "w") as f:
            json.dump(data, f, indent=4)
            
            
    @staticmethod
    def create():
        appointments = Appointment.load_data(APPOINTMENTS_FILE)
        patients = Appointment.load_data(PATIENTS_FILE)
        
        
        
        patient_id = int(input("patoent ID: "))
        doctor = input("Doctor username: ")
        date = input("Dte (YYYY-MM-DD): ")
        
        
        found = False
        for p in patients:
            if p["id"] == patient-id:
                found = True
                break
            
            
            if not found:
                print("patient not found.")
                new_id = len(appointments) + 1
                
                appointment = {
                    "id": new_id,
                    "patient_id": patient_id,
                    "doctor": doctor,
                    "date": date,
                    "completed":  False
                
                }
                
                appointments.append(appointment)
                Appointment.save_data(APPOINTMENTS_FILE, appointments)
                print("Appointment created. ")
                
                
    @staticmethod
    def view_all():
        
        appointments = Appointment.load.data(APPOINTMENTS_FILE)
        
        if not appointments:
            print("No appointments.")
            return
        
        for a in appointments:
            print(a)
            
    @staticmethod
    def view_all():
        appointments = Appointment.load_data(APPOINTMENTS_FILE)
        
        if not appointments:
            print("No appointments.")
            return
        
        for a in appointments:
            print(a)
        
        
    @staticmethod
    def view_doctor(current_user):
        appointments = Appointment.load_data(APPOINTMENTS_FILE)
        
        
        appointment_id = int(input("Appointment ID:  "))
        
        
        for a in appointments:
            if a ["id"] == appointment_id:
                if a["doctor"] != current_user["username"]:
                    print("You cannot complete this appointment.")
                    return
                
                a["completed"]  = True
                Appointment.save_data(APPOINTMENTS_File, appointments)
                print("Marked as completed.")
                return 
            
            print("Appointment not found.")
                
                
                
                
    @staticmethod
    def delete():
        appointments = Appointment.load_data(APPOINTMENTS_FILE)
        
        appointment_id = int(input("APPOINTMENTS ID: "))
        
        for a in appointments:
            if a["id"] == appointment_id:
               appointments.remove(a)
               Appointment.save_data(APPOINTMENTS_FILE, appointments)
               print("Appointment deleted.")
               return
           
        print("Appointment not found.")
            