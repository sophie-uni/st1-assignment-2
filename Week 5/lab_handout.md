### Part A - Client Brief: AI OFF
### SmartCare uses spreadsheets and paper records. Staff report duplicate bookings, difficulty finding patient information, inconsistent appointment status and limited appointment history. Management wants a small, maintainable patient, practitioner and appointment system.<br/>
**Project:** Small Patient, Practitioner and Appointment Management System <br />
SmartCare currently manages patient and appointment information using spreadsheets and paper records. This process has resulted in duplicate bookings, difficulty locating patient information, inconsistent appointment statuses and limited access to appointment history.
SmartCare wants a lightweight, reliable and maintainable system to centralize manage essential information about patients, practitioners and appointments. The system should help staff find patient records quickly, reduce duplicate bookings, maintain consistent appointment statuses and provide a usable history of appointments.
The proposed system should be simple to operate, reliable for day-to-day administrative work and maintainable as SmartCare’s needs develop. Detailed features, scope boundaries and data requirements will be confirmed with stakeholders before development.

### Part B - Stakeholders and Scope: AI OFF
### Identify at least four stakeholders. Create In Scope and Out of Scope lists. Label uncertain features as provisional rather than confirmed.
Stakeholders:
- Admin/Reception Staff: Responsible for scheduling appointments, updating patient details, and checking in patients upon arrival.
- Healthcare Practitioners (GPs): Access daily consultation schedules, view patient appointment histories, and verify visit statuses.
- Clinic Management: Oversees clinic operations, staff assignments, workflow efficiency, and system operational costs.
- Patients: Service recipients who require accurate scheduling, reduced waiting times, and record keeping.
- System Admin: Maintains and support the system

Project Scope
<p>In Scope:<br />
- Centralized patient directory: creation, view, and edit of patient data.<br />
- Practitioner profile directory: name, specialty, and contact details.<br />
- Appointment scheduling, rescheduling, and cancellation management.<br />
- (provisional) Appointment status lifecycle tracking: Scheduled, Checked-In, Completed, Cancelled, No-Show.<br />
- (provisional) Patient appointment history log: list of past and upcoming visits.<br />
- Basic schedule collision detection to prevent double-booking.</p>
<p>Out of Scope:<br />
- Direct clinical notes, diagnostic imaging, and Electronic Medical Record.<br />
- Billing, invoicing, insurance claim processing, and online payment gateway integration.<br />
- External public facing patient self scheduling portal.<br />
- Integration with national health databases or external laboratory information systems.</p>


### Part C - Functional Requirements: AI OFF
### Write 8-12 numbered functional requirements using FR-01, FR-02 and so on. Each should describe one observable capability.
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

### Part D - Non-Functional Requirements: AI OFF
### Write 4-6 numbered non-functional requirements covering appropriate qualities such as reliability, maintainability, usability, data integrity or testability.
- NFR-01 Reliability: The system shall maintain appointment and patient records without data loss during normal operation.
- NFR-02 Usability: Reception staff shall be able to perform common appointment booking tasks with minimal training.
- NFR-03 Maintainability: The system shall be designed so that updates and bug fixes can be implemented without major changes to core functionality.
- NFR-04 Data Integrity: The system shall ensure that patient, practitioner, and appointment records remain consistent and free from duplicate entries where possible.
- NFR-05 Testability: All functional requirements shall have observable outcomes that can be validated through testing.
- NFR-06 Availability: The system shall be available during clinic operating hours unless scheduled maintenance is being performed.

### Part E - User Stories and Acceptance Criteria: AI OFF
### Write 4-6 user stories. For at least three, create Given-When-Then acceptance criteria including one negative or failure scenario.
#### User Story 1 <br/>
As a receptionist, I want to create a patient record so that patient information can be stored and retrieved later. <br />
**Acceptance Criteria**<br />
**Given** I am logged into the system<br />
**When** I enter valid patient details and save the record<br />
**Then** a new patient record is created.<br />
**Negative Scenario**<br />
**Given** I am creating a patient record<br />
**When** mandatory information is missing<br />
**Then** the system shall display an error message and prevent saving.<br />

#### User Story 2 <br />
As a receptionist, I want to schedule appointments so that patients can see practitioners at a specific time.<br />
**Acceptance Criteria**<br />
**Given** a practitioner is available<br />
**When** I schedule an appointment in an empty time slot<br />
**Then** the appointment shall be created successfully.<br />
**Negative Scenario**<br />
**Given** a practitioner already has an appointment in a time slot<br />
**When** I attempt to create another appointment in the same slot<br />
**Then** the system shall reject the booking and display a warning.<br />

#### User Story 3 <br />
As a practitioner, I want to view my upcoming appointments.<br />
**Acceptance Criteria**<br />
**Given** appointments exist for me<br />
**When** I view my schedule<br />
**Then** my upcoming appointments shall be displayed.<br />
**Negative Scenario**<br />
**Given** no appointments are scheduled<br />
**When** I view my schedule<br />
**Then** the system shall display that no appointments exist.<br />

#### User Story 4<br />
As a receptionist, I want to update appointment status so that appointment records remain accurate.<br />
**Acceptance Criteria**<br />
**Given** an appointment exists<br />
**When** I change its status and save<br />
**Then** the updated status shall be stored.<br />

#### User Story 5<br />
As a practitioner, I want to view patient appointment history so that I can understand previous visits.<br />
**Acceptance Criteria**<br />
**Given** a patient exists with appointment history<br />
**When** I open the patient's record<br />
**Then** previous appointments shall be displayed.<br />
**Negative Scenario**<br />
**Given** a patient on the first visit<br />
**When** I open the patient's record<br />
**Then** the system shall display that no appointments history exist.<br />

### Part F - AI Requirements Review: AI ON
### Prompt: Act as a software requirements reviewer. Review the SmartCare requirements for ambiguity, inconsistency, missing clarification questions and testability. Do NOT invent new client requirements. For every suggestion, state whether it is based on evidence or is only a question/assumption requiring validation.
1. **Ambiguity:** Appointment duplicate <br />
**Observation:** FR-06 refers to prevent overlapping appointments for the same practitioner, but doesn't define what happens if a patient is booked for two practitioners.<br />
**Recommendation:** Clarify different double booking situations.<br />
**Classification:** Question requiring validation.<br />

2. **Ambiguity:** Patient Identifying Information <br />
**Observation:** FR-09 states "search for patient records" but does not specify search fields.<br />
**Recommendation:** Clarify whether searching should use patient name, patient ID, phone number, or multiple criteria.<br />
**Classification:** Question requiring validation.<br />

3. **Missing Clarification:** User Authentication <br />
**Observation:** Requirements mention staff and practitioners using the system but do not specify login requirements.<br />
**Recommendation:** Ask the client whether authentication and role-based access are required.<br />
**Classification:** Question requiring validation.<br />

4. **Testability Issue:** Minimal Training <br />
**Observation:** NFR-02 uses the phrase "minimal training," which is difficult to measure.<br />
**Recommendation:** Replace with a measurable criterion.<br />
**Classification:** Evidence-based issue.<br />

5. **Appointment History Definition**<br />
**Observation:** FR-10 requires appointment history but does not define whether canceled appointments should be included.<br />
**Recommendation:** Clarify historical record requirements.<br />
**Classification:** Question requiring validation.<br />

### Part G - VERIFY the AI Review
### Classify each significant AI suggestion as Accepted, Modified, Rejected, or Unverified. Explain the evidence used.
| AI Suggestion                        | Decision | Evidence                                                                                     |
| ------------------------------------ | -------- | ------------------------------------------------------------------------------------------------ |
| Clarify duplicate patient records    | Accepted | Duplicate records are a common data quality concern and need confirmation.                           |
| Clarify patient search criteria      | Accepted | FR-09 is not sufficiently specific for testing.                                                                               |
| Clarify authentication requirements  | Modified | User access exists but client brief does not explicitly mention security requirements. Added as open question instead of requirement. |
| Replace "minimal training"           | Accepted | NFR-02 is difficult to test objectively.                                                                                      |
| Clarify appointment history contents | Accepted | Requirement lacks enough detail for testing.                                                                                  |

### Part H - Finalise SmartCare v0.2
### Submit stakeholder analysis, scope, 8-12 FRs, 4-6 NFRs, 4-6 user stories, acceptance criteria, assumptions/open questions and selected AI review evidence.
- Stakeholder analysis and scope detailed in Part B
- 12 FRs detailed in Part C
- 6 NFRs detailed in Part D
- 5 user stories detailed in Part E
- Assumptions
  - Reception staff manage appointment creation and updates.
  - Practitioners may view patient information relevant to appointments.
  - Appointment history includes completed appointments.
  - Multiple practitioners may use the system simultaneously.
- Open Questions
  - What appointment status values should be supported?
  - What patient fields should be searchable?
  - Is user authentication required?
  - Should duplicate patient detection be implemented?
  - Should canceled appointments appear in appointment history?
- Selected AI Review detailed in Part G

### Reflection
### In 150-250 words: What did AI notice that you missed? What did AI invent or overreach on? Which requirement changed after review? Why must requirements have evidence?
The AI review identified several specification weaknesses that were not immediately obvious during the initial requirements drafting process. One important thing is the AI highlighted vague terminology such as "patient identifying information" and "minimal training," both of which could lead to different interpretations by developers and testers.<br />
Some AI suggestions went beyond the evidence provided in the client brief. For example, the recommendation to include authentication requirements was not explicitly supported by the brief. While authentication may be appropriate for a healthcare system, it remains an assumption that requires client confirmation rather than a confirmed requirement.<br />
The requirement that changed most after review was NFR-02. The original wording, "minimal training," was subjective and impossible to test consistently. It was revised to specify a measurable booking task outcome, making it more testable. <br />
Software requirements must be supported by evidence because unsupported assumptions can result in developing features that the client never requested. Evidence ensures requirements remain aligned with stakeholder needs, reduces project risk, and improves validation and acceptance during system delivery.