### Candidate Concepts
| Candidate    | Class? | Reason                                                                                           |
|--------------|--------|--------------------------------------------------------------------------------------------------|
| Patient      | Yes    | A core business entity with unique identity, behaviors, and multiple attributes.               |
| Practitioner | Yes    | A primary domain entity with unique identity, availability, and specific operations.       |
| Appointment  | Yes    | A key business event linking entities, containing state, date, time, and business rules.         |
| Name    | No     | An attribute of Patient or Practitioner rather than a separate class.                            |
| Clinic  | Yes    | Represents a distinct entity that may contain practitioners and manage appointments or patients. |
| Database   | No   | A technical component, not usually a domain class in the problem model.                          |
| Cancellation  | No  | An action or state change associated with an Appointment, rather than an independent entity.     |
| Status  | No   | An attribute of Appointment, such as Scheduled, Completed, or Cancelled.                         |

### CRC Cards
#### Class: Patient
| Responsibilities	| Collaborators |
|----------------|-------------|
| Maintain personal and contact information | Appointment |
| Book appointments with practitioners | Practitioner, Appointment |
| Cancel or reschedule appointments	| Appointment |
| View appointment history and status | Appointment |

#### Class: Practitioner
| Responsibilities	                      | Collaborators        |
|----------------------------------------|----------------------|
| Maintain practitioner details          | Clinic               |
| Manage appointment                     | Appointment          |
| Accept or reject appointment requests  | Appointment, Patient |
| View patient appointment information   | Appointment, Patient |

#### Class: Appointment
| Responsibilities	| Collaborators |
|----------------|-------------|
| Store appointment date, time, and status | Patient, Practitioner |
| Link a patient with a practitioner | Patient, Practitioner |
| Update appointment status	| Patient, Practitioner |

### Relationship Reasoning
#### Patient to Appointment: which relationship and why?
Relationship: one-to-many <br />
Reason: <br />
- A patient can have multiple appointments over time.
- Each appointment belongs to one patient.
- The appointment acts as a link between the patient and practitioner.

#### Practitioner to Appointment: what multiplicity?
Relationship: one-to-many <br />
Multiplicity: 1 Practitioner to (0..n) Appointments <br />
Meaning: <br />
- One Practitioner can conduct many Appointments.
- Each Appointment is conducted by one Practitioner.

#### Should Appointment inherit from Patient?
**No.** <br />
Inheritance represents an "is-a" relationship. <br />
An Appointment is an event, not a person or patient. It connects a Patient and a Practitioner. < br/>

#### Does Clinic need to own every object?
**No** <br />
The Clinic generally has relationships with the main entities but does not need to own everything. <br />
- Practitioners work at a clinic.
- Appointments are scheduled at a clinic.
- Patients may visit multiple clinics, so making Patient a part of a Clinic can be too restrictive.

### AI Model Critique
#### Critique AI proposals: PatientManager, PractitionerManager, AppointmentManager, ClinicController, NotificationManager, ScheduleEngine.
The AI proposed classes PatientManager, PractitionerManager, AppointmentManager, ClinicController, NotificationManager, and ScheduleEngine are primarily implementation-oriented classes rather than domain entities. They describe how the software may be structured internally rather than the real objects involved in clinic appointment management. For an analysis level class diagram, classes such as Patient, Practitioner, Appointment, and Clinic are more appropriate because they represent key business concepts with their own attributes and relationships.