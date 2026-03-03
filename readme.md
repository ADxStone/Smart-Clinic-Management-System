# Smart Clinic Management System

A lightweight, terminal-based clinic management system for managing patients, appointments, and users. Built in Python with a small modular codebase to support easy learning and extension.

**Repository Link**

```bash
https://adxstone.github.io/Smart-Clinic-Management-System/
```

**Features**

- **Patient management:** add, view and store patient records.
- **Appointment scheduling:** create and list appointments tied to patients.
- **User handling:** simple user records for access and ownership tracking.
- **JSON storage:** persistent data stored in `Storage/` as JSON files.

**Jira Space**

```bash
https://mathewstalel.atlassian.net/jira/software/projects/GR8/summary?atlOrigin=eyJpIjoiYzI4YTVmNzM3NzYxNGRiM2I1N2U2NDNlY2Q1NWFlZWUiLCJwIjoiaiJ9
```

**Quick Start**

1. Ensure you have Python 3.8+ installed.
2. (Optional) Create a virtual environment
3. Run the application

```bash
python main.py
```

**Project Layout**

- `main.py` – application entry point.
- `Parts/` – core modules:
  - `Parts/patient.py` – patient-related logic.
  - `Parts/appointment.py` – appointment-related logic.
  - `Parts/users.py` – user-related logic.
- `Storage/` – JSON data files (`patients.json`, `appointments.json`, `users.json`).
- `Utilities/` – helper utilities and decorators.

**Usage**

The app is interactive via the terminal. Running `python main.py` will present the available actions (add patient, schedule appointment, list records, etc.). Data is stored automatically in the `Storage/` folder.

**Development**

- Keep code modular under `Parts/` and `Utilities/`.
- Add tests or example scripts as needed.

**Contributors**

-Mark Wainaina
-Prexidazie Morara
-Nyaga Murimi
-Mathews Talel
