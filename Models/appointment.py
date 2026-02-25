appointments = [
    {"id": 1, "patient_id": 1, "doctor_username": "doc1", "date": "2026-02-25", "status": "Scheduled"},
    {"id": 2, "patient_id": 2, "doctor_username": "doc1", "date": "2026-02-26", "status": "Scheduled"},
]


def list_appointments_for_doctor(doctor_username):
    return [a for a in appointments if a["doctor_username"] == doctor_username]
