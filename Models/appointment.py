appointments = []


def list_appointments_for_doctor(doctor_username):
	return [a for a in appointments if a.get("doctor_username") == doctor_username]
