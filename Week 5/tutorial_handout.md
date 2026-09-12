### Activity 1 - Stakeholder Map
| Stakeholder           | Need                                                                       | Potential conflict                                                                                  |
|-----------------------|----------------------------------------------------------------------------|-------------------------------------------------------------------------------------------|
| Admin/Reception Staff | Simple booking workflows   | Detailed data entry demanded by management or practitioners can slow down check-in and booking times |
| Practitioners (GPs)   | Appointment histories, protected schedules without overbooking  | Clinic management wanting high patient throughput or reception trying to squeeze in urgent walk ins |
| Clinic Management     | Low maintenance costs, staff accountability, and operational efficiency metrics | Strict controls and detailed reporting requirements can create friction and extra administrative burden for staff  |
| Patients              | Flexible rescheduling, and zero booking mix-ups or lost records | Practitioner availability and strict clinic cancellation or late-arrival rules |

### Activity 2 - Functional or Non-Functional?
- The system shall allow staff to cancel an appointment. **Functional**
- The system should remain responsive for the course-scale dataset. **Non-functional**
- The system shall retain cancelled appointments. **Functional**
- Core business logic should be independently testable. **Non-functional**
- The system shall search for a patient by ID. **Functional**

### Activity 3 - Repair Ambiguous Requirements
1. The system should be easy to use. <br />
**Problem:** Subjective and untestable; "easy" varies by user familiarity and role.<br />
**Clarification question:** What specific benchmark defines usability (e.g., maximum number of clicks, or can a new staff member complete a booking within 2 minutes after 15 minutes of training)? <br />
2. Patient search should be fast. <br />
**Problem:** "Fast" provides no quantifiable performance threshold. <br />
**Clarification question:** What is the acceptable maximum response time in milliseconds/seconds under standard concurrent load (e.g., under 1.5 seconds for a query on 20,000 records)?<br />
3. The system should securely manage data. <br />
**Problem:** Lacks concrete security standards, access control models, or compliance targets. <br />
**Clarification question:** Which specific access roles, authentication protocols, and data privacy regulations (e.g., role-based access control, password hashing) must be implemented?<br />
4. Appointments should normally be easy to cancel. <br />
**Problem:** "Normally" indicates unstated exceptions, and "easy" is not a measurable criterion. <br />
**Clarification question:** Under what specific circumstances can an appointment be cancelled, who is authorized, and what mandatory inputs (such as a cancellation reason) are required?<br />

### Activity 4 - AI Requirements Audit
#### Classify each suggestion: Confirmed / Assumption requiring validation / Unsupported / Out of scope.

| AI suggestion           | Classification | Evidence / reason        |
|-----------------------|---------------|--------------------------|
| Patients receive SMS reminders. | Assumption requiring validation | While common in clinic systems, automated notifications were not confirmed in the core client brief and introduce external gateway costs. |
| Facial recognition login.  | Unsupported   | Unnecessary biometric complexity; contradicts the brief’s requirement for a "small, maintainable" system. |
| Receptionists create appointments.    | Confirmed     | Directly supported by the client brief to eliminate duplicate bookings and replace spreadsheets. |
| Online payment.              | Out of scope  | Payment processing and billing are not mentioned in scope |
| Practitioners view schedules. | Confirmed     | Supported by staff reporting inconsistent appointment statuses and the need for practitioners to see consult lists. |
| AI recommends treatments. | Unsupported   | Not mentioned in scope   |
| Cancelled appointments remain in history. | Confirmed | Directly supported by staff reporting "limited appointment history" as an operational failure. |

### Exit question
#### Why is 'AI suggested it' not sufficient evidence for a requirement?
AI-generated suggestions can sometimes extend beyond the information provided by the client, introducing generic industry features or assumptions that are not supported by evidence. If these recommendations are adopted without validation through stakeholder consultation or documented requirements, they can contribute to scope creep, increased development costs, and solutions that do not address the client's actual needs. Therefore, every requirement should be traceable to a verified business need and supported by evidence obtained from stakeholders, interviews, or approved documentation.