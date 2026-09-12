### 1. Problem and Scope
**Problem:** <br />
The current manual system is inefficient and prone to errors. SmartCare requires a small, maintainable information system to manage patients, practitioners, and appointments in a consistent and reliable manner.<br />
**Scope** <br />
Develop a system that enables staff to:
- Maintain patient records.
- Maintain practitioner records.
- Schedule and manage appointments.

### 2. Stakeholders
| Stakeholder           | Need                                                                       | Evidence                                                                                  |
|-----------------------|----------------------------------------------------------------------------|-------------------------------------------------------------------------------------------|
| Admin/Reception Staff | easy patient lookup and conflict free booking tools                        | Staff report duplicate bookings and difficulties finding patient records in spreadsheets. |
| Practitioners (GPs)   | Reliable daily schedules and quick access to prior visit history           | Staff report inconsistent appointment statuses and limited access to longitudinal history |
| Clinic Management     | Operational visibility, minimal maintenance overhead, and data consistency | Management requested a small, maintainable system to replace spreadsheets and paper       |
| Patients              | Reliable appointment scheduling without double-booked time slots or delays | Duplicate bookings cause service delays and scheduling conflicts for patients             |
| System Admin          | easy to maintained system                                                  | A lightweight, reliable, and maintainable software system                                 |

### 3. Functional Requirements
- FR-01: The system shall allow authorized users to create a new patient record.
- FR-02: The system shall allow authorized users to view and update existing patient records.
- FR-03: The system shall allow authorized users to create a practitioner record.
- FR-04: The system shall allow authorized users to view and update practitioner records.
- FR-05: The system shall allow authorized users to schedule appointments between patients and practitioners.
- FR-06: The system shall prevent appointments from being created when a practitioner is already booked for the selected time slot.
- FR-07: The system shall allow authorized users to reschedule an existing appointment to a new date and time, subject to schedule collision validation.
- FR-08: The system shall allow authorized users to cancel appointments.
- FR-09: The system shall allow authorized users to search for patient records.
- FR-10: The system shall display the appointment history associated with a selected patient.
- FR-11: The system shall display a practitioner's upcoming appointments.
- FR-12: The system shall mark a patient profile as inactive rather than deleting the underlying data when a user initiates a profile deletion.

### 4. Non-Functional Requirements
- NFR-01 Reliability: The system shall maintain appointment and patient records without data loss during normal operation.
- NFR-02 Usability: Reception staff shall be able to perform common appointment booking tasks with minimal training.
- NFR-03 Maintainability: The system shall be designed so that updates and bug fixes can be implemented without major changes to core functionality.
- NFR-04 Data Integrity: The system shall ensure that patient, practitioner, and appointment records remain consistent and free from duplicate entries where possible.
- NFR-05 Testability: All functional requirements shall have observable outcomes that can be validated through testing.
- NFR-06 Availability: The system shall be available during clinic operating hours unless scheduled maintenance is being performed.

### 5. User Stories
#### User Story 1 <br/>
As a receptionist, I want to create a patient record so that patient information can be stored and retrieved later. <br />
#### User Story 2 <br />
As a receptionist, I want to schedule appointments so that patients can see practitioners at a specific time.<br />
#### User Story 3 <br />
As a practitioner, I want to view my upcoming appointments.<br />
#### User Story 4<br />
As a receptionist, I want to update appointment status so that appointment records remain accurate.<br />
#### User Story 5<br />
As a practitioner, I want to view patient appointment history so that I can understand previous visits.<br />

### 6. Acceptance Criteria
**User Story 1 Acceptance Criteria**<br />
**Given** I am logged into the system<br />
**When** I enter valid patient details and save the record<br />
**Then** a new patient record is created.<br />
**Negative Scenario**<br />
**Given** I am creating a patient record<br />
**When** mandatory information is missing<br />
**Then** the system shall display an error message and prevent saving.<br />

**User Story 2 Acceptance Criteria**<br />
**Given** a practitioner is available<br />
**When** I schedule an appointment in an empty time slot<br />
**Then** the appointment shall be created successfully.<br />
**Negative Scenario**<br />
**Given** a practitioner already has an appointment in a time slot<br />
**When** I attempt to create another appointment in the same slot<br />
**Then** the system shall reject the booking and display a warning.<br />

**User Story 3 Acceptance Criteria**<br />
**Given** appointments exist for me<br />
**When** I view my schedule<br />
**Then** my upcoming appointments shall be displayed.<br />
**Negative Scenario**<br />
**Given** no appointments are scheduled<br />
**When** I view my schedule<br />
**Then** the system shall display that no appointments exist.<br />

**User Story 4 Acceptance Criteria**<br />
**Given** an appointment exists<br />
**When** I change its status and save<br />
**Then** the updated status shall be stored.<br />

**User Story 5 Acceptance Criteria**<br />
**Given** a patient exists with appointment history<br />
**When** I open the patient's record<br />
**Then** previous appointments shall be displayed.<br />
**Negative Scenario**<br />
**Given** a patient on the first visit<br />
**When** I open the patient's record<br />
**Then** the system shall display that no appointments history exist.<br />

### 7. Assumptions and Open Questions
**Assumption 1:** Standard appointment duration defaults to 15 minutes unless specified otherwise by the booking clerk.
**Assumption 2:** The system will run locally on the clinic's internal network; external web hosting or public internet exposure is not required for v0.2.
**Question 1:** What specific cancellation cutoff period requires a mandatory cancellation reason?
**Question 2:** Does clinic policy allow patients to be assigned to multiple practitioners on the same day if time slots do not overlap?

### 8. AI Requirements Review Record
| AI suggestion | Evidence? | Decision | Reason                                                                 | Verification                           |
|-----|-----------|----------|------------------------------------------------------------------------|----------------------------------------|
| Check patient-side double booking in addition to practitioner booking | Yes       | Accepted | Prevents booking one patient with multiple doctors    | Verified against NFR-04 Data Integrity |
| Integrate national health identifier API for patient lookup | No        | Rejected | Adds unnecessary external dependencies, costs, and compliance overhead | Out of scope                           |
| Clarify authentication requirements  | Yes       | Modified | unclear authentication requirements for stockholders                   | Requires confirmation                  |
| Clarify patient search criteria | Yes    | Accepted | nessasery for making booking and prevent duplicated bookings      | Requires detailed information          |
