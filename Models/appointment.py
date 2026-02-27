<<<<<<< HEAD
import json
import os
from datetime import datetime

APPOINTMENTS_FILE = "Storage/appointments.json"
PATIENTS_FILE = "Storage/patients.json"

#---------------- HELPER METHODS ------------------
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

#-------------------CREATE--------------------
            
    @staticmethod
    def create(current_user):
        appointments = Appointment.load_data(APPOINTMENTS_FILE)
        patients = Appointment.load_data(PATIENTS_FILE)
        
        
        try:
            patient_id = int(input("patient ID: "))
        except ValueError:
            print("Invalid patient ID.")
            return
        
        date = input("Date (YYYY-MM-DD): ")
        
        time_input = input("Time (HH:MM AM/PM): ")
        
        try:
            valid_time = datetime.strtime(time_input, "%I:%M:%P")
            time = valid_time.strftime("%I:%M:%P")
        except ValueError:
            print("Invalid time format. Example: 02:30pm")
            return
        
        #CHECK IF PATINETS EXISTS
    
        if not any(p["id"] == patient_id for p in patients):
            print("Patient not found.")
            return
        
     #GENERATE UNIQUE ID SAFELY
        if appointments:
             new_id = max(a["id"] for a in appointments) + 1
        else:
           new_id = 1

        appointment = {
            "id": new_id,
            "patient_id": patient_id,
            "doctor": current_user["username"],  # auto-assign logged-in doctor
            "date": date,
            "completed": False
        }

        appointments.append(appointment)
        Appointment.save_data(APPOINTMENTS_FILE, appointments)

        print("Appointment created successfully.")
            
         
                
#-----------------VIEW_ALL-------------------
            
    @staticmethod
    def view_all():
        appointments = Appointment.load_data(APPOINTMENTS_FILE)
        
        if not appointments:
            print("No appointments.")
            return
        
        for a in appointments:
             print(f"ID: {a['id']} | Patient ID: {a['patient_id']} | "
                  f"Doctor: {a['doctor']} | Date: {a['date']} | "
                  f"Completed: {a['completed']}")
             

#----------------------DOCTOR APPOINTMENTS-----------------            
    @staticmethod
    def view_doctor(current_user):
        appointments =Appointment.load_data(APPOINTMENTS_FILE)
        
        
        doctor_appointments = [
            a for a in appointments
            if a["doctor"]  == current_user["username"]
        ]
        
        if not doctor_appointments:
            print("No appointments found.")
            return
        
        for a in doctor_appointments:
            print(f"ID: {a['id']} | Patient ID: {a['patient_id']} | "
                  f"Date:{a['date']} | Time: {a['time']} | "
                  f"Completed: {a['completed']}")

#-----------------COMPLETE------------------        
        
    @staticmethod
    def complete(current_user):
        appointments = Appointment.load_data(APPOINTMENTS_FILE)
        
        try:
        
            appointment_id = int(input("Appointment ID:  "))
        except ValueError:
             print("Invalid appoint ID.")
             return
        
        
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
                
                
#--------------DELETE----------------     
                
    @staticmethod
    def delete():
        appointments = Appointment.load_data(APPOINTMENTS_FILE)
        
        try:
        
            appointment_id = int(input("APPOINTMENTS ID: "))
        except ValueError:
            print("Invalid appointment ID.")
            return
        
        for a in appointments:
            if a["id"] == appointment_id:
               appointments.remove(a)
               Appointment.save_data(APPOINTMENTS_FILE, appointments)
               print("Appointment deleted.")
               return
           
        print("Appointment not found.")
            
=======
appointments = []


