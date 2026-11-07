# HealthSync Case Bible: student edition

The fixed facts for the running case in *Information Technology Project Management: Traditional Foundations, Agile Delivery and AI-Enhanced Practice*, with the section numbers the book uses (for example "Case Bible, Section 6"). This edition contains Sections 2 to 10, 12 and 13. Section 11, the complication cards, is held by your tutor, who releases each card at the right week. Sections 1, 14 and 15 are production notes and are not included. A Word version for printing is in this folder.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>FICTIONAL CASE</strong></p>
<p>CareGrid Networks, Project HealthSync and every person, organisation,
figure and event in this case are fictional. Any resemblance to real
organisations or people is coincidental. Monetary amounts use a fixed
teaching exchange rate of <strong>USD 1 = K26</strong>.</p></td>
</tr>
</tbody>
</table>

## 2. CareGrid Networks

CareGrid Networks is a privately owned healthcare group founded in
Lusaka in 2004. It runs one hospital and seven clinics across four
provinces, serving salaried workers, insured families and a growing
number of self-paying patients.

| **Fact**                 | **Value**                                                                                                                              |
|--------------------------|----------------------------------------------------------------------------------------------------------------------------------------|
| Head office              | Lusaka                                                                                                                                 |
| Facilities               | CareGrid Central Hospital, Lusaka (120 beds); clinics in Kabulonga and Chilenje (Lusaka), Ndola, Kitwe, Kabwe, Livingstone and Chipata |
| Staff                    | About 1,150, including 140 doctors, 420 nurses and 18 IT staff                                                                         |
| Registered patients      | About 186,000                                                                                                                          |
| Outpatient consultations | About 24,000 a month across all facilities                                                                                             |
| Annual revenue           | About K480 million                                                                                                                     |
| Payment channels today   | Cash, card at reception, insurance; no mobile money                                                                                    |
| Connectivity             | Fibre at the hospital and Lusaka clinics; slower links at provincial clinics; many patients rely on mobile data                        |

#### Why change now

- Patients increasingly expect to book and consult by phone. A competing
  provider launched video consultations last year and is winning insured
  corporate clients.

- Doctors at provincial clinics want specialist support from Lusaka
  without patients travelling.

- The board wants CareGrid to comply fully with the Data Protection Act
  No. 3 of 2021 before its next corporate insurance renewals.

## 3. The legacy system: CareBook

CareBook is the patient scheduling and records system built for CareGrid
in 2012 by a local software house that has since closed. Nobody on the
current team wrote it.

| **Aspect**           | **Detail**                                                                                                            |
|----------------------|-----------------------------------------------------------------------------------------------------------------------|
| Technology           | ASP.NET Web Forms application on Microsoft SQL Server 2008 R2 (out of vendor support since 2019)                      |
| Hosting              | Two physical servers in the server room at CareGrid Central Hospital                                                  |
| Data                 | About 2.4 million patient records and 9.8 million visit records; free-text fields; duplicate patients estimated at 6% |
| Integration          | No web APIs. Provincial clinics sync through a nightly batch over VPN                                                 |
| Reliability          | Crashes under Monday-morning peak load about three times a month; 61 hours of unplanned downtime last year            |
| Security gaps        | Shared logins at reception, no encryption at rest, audit trail switched off to save disk space                        |
| Functions missing    | Video consultation, online booking, mobile access, e-prescribing, online payment                                      |
| Key knowledge holder | Joseph Daka (DBA), who has maintained CareBook since 2015                                                             |

## 4. Project HealthSync

In Month 0 the board authorised Project HealthSync: migrate CareGrid's
core scheduling and records to a cloud-native platform and launch a
secure mobile and web service for video consultations, e-prescriptions
and payments.

### 4.1 Objectives

| **\#** | **Objective**                                                                | **Measure**                                                                                                             |
|--------|------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|
| O1     | Migrate all patient records active in the last seven years with no data loss | 100% reconciliation of record counts and checksums at cutover                                                           |
| O2     | Launch video consultations at all eight facilities                           | Live at all sites by end of Month 6; 1,500 video consultations a month within three months of go-live (benefit measure) |
| O3     | Provide a reliable service                                                   | 99.5% monthly availability for patient-facing services                                                                  |
| O4     | Meet data protection and security obligations                                | Data protection impact assessment approved and independent security test passed before go-live                          |
| O5     | Deliver within budget                                                        | Capital spend within K6,500,000; cloud running costs within K95,000 a month                                             |

### 4.2 Scope

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>In scope</strong></th>
<th><strong>Out of scope (later phases)</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Patient identity, registration and consent</p>
<p>Appointment scheduling for all facilities</p>
<p>Patient records: demographics and visit history</p>
<p>Video consultation (mobile and web)</p>
<p>E-prescriptions through PrescribeLink</p>
<p>Payments through PayBridge (mobile money and card)</p>
<p>SMS and push notifications</p>
<p>Data migration from CareBook</p>
<p>Training for staff at all eight facilities</p></td>
<td><p>Laboratory information system</p>
<p>Pharmacy stock management</p>
<p>Insurance claims processing</p>
<p>HR and payroll</p>
<p>AI symptom checker (until Complication 1)</p>
<p>Full clinical notes and imaging</p></td>
</tr>
</tbody>
</table>

### 4.3 Constraints

- **Time:** fixed six-month delivery window (Month 1 to Month 6).

- **Capital budget:** K6,500,000, released in three tranches (Section
  6).

- **Running costs:** cloud spend capped at K95,000 a month from go-live.

- **Compliance:** the Data Protection Officer must approve where and how
  patient data is processed, including any processing outside Zambia.
  This is a deliberate decision point in Chapters 6 and 10.

- **Security:** encryption in transit and at rest, end-to-end encryption
  for video, role-based access, full audit logging.

- **Connectivity:** the patient app must work on slow mobile
  connections, with an audio-only fallback for video calls.

## 5. Target solution

The agreed direction is a cloud-native platform built as a small set of
services behind an API gateway. Students design the detail; these facts
are fixed.

| **Component**    | **Fixed facts**                                                                                                                  |
|------------------|----------------------------------------------------------------------------------------------------------------------------------|
| Hosting          | Public cloud, provider to be chosen between AWS and Microsoft Azure (Assignment 3)                                               |
| Services         | Identity and access; patient records; scheduling; video consultation; e-prescription adapter; payments; notifications; audit log |
| Clients          | Android app first (most patients), iOS app, web portal for clinicians and reception                                              |
| Legacy access    | CareBook data migrated in rehearsed batches; CareBook kept read-only for 12 months after cutover                                 |
| E-prescriptions  | PrescribeLink Africa Ltd, Johannesburg, REST API v2                                                                              |
| Payments         | PayBridge Payments Ltd, Lusaka: mobile money and card                                                                            |
| Delivery tooling | Jira for backlog and sprints, GitHub with GitHub Actions for CI/CD, SonarQube for code quality                                   |

## 6. Budget and financial assumptions

| **Capital budget line**                                                              | **Amount (K)** |
|--------------------------------------------------------------------------------------|----------------|
| Internal staff time charged to the project                                           | 3,250,000      |
| Contract developers (mobile and video)                                               | 780,000        |
| Cloud set-up and data migration                                                      | 610,000        |
| Security and compliance (penetration test, data protection impact assessment, audit) | 540,000        |
| Software licences and delivery tools                                                 | 420,000        |
| Training and change management                                                       | 260,000        |
| Contingency reserve (about 10%)                                                      | 640,000        |
| **Total capital budget**                                                             | **6,500,000**  |

| **Tranche** | **Released**     | **Amount (K)** | **Condition**                                         |
|-------------|------------------|----------------|-------------------------------------------------------|
| 1           | Start of Month 1 | 2,500,000      | Charter approved                                      |
| 2           | Start of Month 3 | 2,500,000      | Investment committee review of Month 2 progress       |
| 3           | Start of Month 5 | 1,500,000      | Security test plan and migration rehearsal 1 complete |

#### Assumptions

- Teaching exchange rate: **USD 1 = K26**, fixed for every calculation
  in the book.

- Cloud services are priced by the providers in US dollars and paid
  monthly. The running-cost cap of K95,000 is about USD 3,650.

- Average loaded cost of an internal team member: K1,300 a day.

- Discount rate for NPV in Chapter 3: 18% a year.

- Expected benefits (for the business case): K2.1 million a year in new
  video-consultation revenue from Year 1, rising to K3.4 million in Year
  3; K0.6 million a year saved on CareBook support and downtime.

## 7. Timeline, teams and velocity

| **Month** | **Planned milestones**                                                                   |
|-----------|------------------------------------------------------------------------------------------|
| 1         | Charter approved; architecture agreed; backlog refined; Sprints 1 and 2                  |
| 2         | Identity and scheduling services working end to end; migration design complete           |
| 3         | Video consultation pilot at CareGrid Central Hospital; PrescribeLink integration started |
| 4         | Payments live in test; migration rehearsal 1                                             |
| 5         | User acceptance testing; independent security test; migration rehearsal 2                |
| 6         | Phased cutover by facility; go-live; two weeks of hypercare                              |

| **Team**    | **Focus**                                   | **Members**                                                                        |
|-------------|---------------------------------------------|------------------------------------------------------------------------------------|
| Team Atlas  | Platform, back-end services, data migration | Brian Kapata (lead), 3 developers, 1 QA engineer, Chipo Mumba (DevOps, shared)     |
| Team Baobab | Mobile apps, video, web portal              | Lucy Hamoonga (UI/UX), 2 internal developers, 2 contract developers, 1 QA engineer |

- Both teams run two-week sprints: 12 sprints in six months.

- Baseline velocity: 34 story points per team per sprint, 68 combined.

- Agreed minimum viable product backlog at the start: 640 story points.

- Combined capacity at baseline velocity: 816 points across 12 sprints,
  leaving 176 points of headroom.

## 8. Cast of characters

Use these people consistently. Their stances create the tensions the
chapters explore.

| **Name**               | **Role**                                             | **What they care about**                                                      |
|------------------------|------------------------------------------------------|-------------------------------------------------------------------------------|
| Ruth Mulenga           | Chief Executive Officer; executive sponsor           | Launching before the competitor wins more corporate clients; reputation       |
| Daniel Chileshe        | Chief Information Officer                            | A platform the IT team can run; moving off unsupported servers                |
| Thandiwe Moyo          | Project Manager (PMP); the book's main point of view | Delivering on time and budget with a hybrid approach; keeping everyone honest |
| Samuel Okafor          | Product Owner                                        | Patient experience; a clean, ordered backlog                                  |
| Priya Nair             | Scrum Master and Agile coach (contract)              | Team health, flow and sustainable pace                                        |
| Dr Mwila Sakala        | Medical Director; clinical lead                      | Fast, simple screens for busy doctors; patient safety                         |
| Sister Beatrice Chirwa | Senior Nursing Officer                               | Reception and triage workflows; staff training                                |
| Grace Tembo            | Data Protection Officer and Head of Compliance       | Lawful processing, consent, encryption, audit trails                          |
| Agnes Lungu            | Finance Director                                     | CapEx versus OpEx; tranche conditions; cloud bills in dollars                 |
| Kelvin Zulu            | Marketing Director; investment committee member      | Features that sell; the AI symptom checker                                    |
| Brian Kapata           | Senior Back-end Developer; Team Atlas lead           | Doing the migration properly; fears legacy surprises                          |
| Chipo Mumba            | Lead DevOps Engineer                                 | Automation and pipelines; holds most of the infrastructure knowledge          |
| Esther Ngoma           | QA Lead                                              | Test automation and quality gates                                             |
| Lucy Hamoonga          | UI/UX Designer                                       | Accessible design for low-literacy and low-bandwidth users                    |
| Joseph Daka            | Database Administrator                               | CareBook's quirks; worried about his role after cutover                       |
| Nomvula Dlamini        | Account Manager, PrescribeLink Africa Ltd            | Keeping CareGrid as a client                                                  |
| Peter Siame            | Chair, CareGrid Patient Forum                        | Privacy and cost for patients                                                 |

## 9. Stakeholder map

| **Quadrant**                                | **Stakeholders**                                                                        |
|---------------------------------------------|-----------------------------------------------------------------------------------------|
| High power, high interest (manage closely)  | Ruth Mulenga, Daniel Chileshe, Grace Tembo, Agnes Lungu, Dr Mwila Sakala                |
| High power, lower interest (keep satisfied) | CareGrid board, Kelvin Zulu (rises to high interest at Complication 1)                  |
| Lower power, high interest (keep informed)  | Sister Beatrice Chirwa, clinic staff, Joseph Daka, Peter Siame and the Patient Forum    |
| Lower power, lower interest (monitor)       | PayBridge, PrescribeLink (rises sharply at Complication 2), corporate insurance clients |

## 10. Seed risk register

Students start Lab 8 from these entries and extend them. Scores use a 1
to 5 scale for probability (P) and impact (I).

| **ID** | **Risk**                                                       | **P** | **I** | **Owner**       |
|--------|----------------------------------------------------------------|-------|-------|-----------------|
| R01    | CareBook data quality (duplicates, free text) delays migration | 4     | 4     | Brian Kapata    |
| R02    | Cloud costs exceed the K95,000 monthly cap as usage grows      | 3     | 3     | Agnes Lungu     |
| R03    | Kwacha weakens against the dollar, raising cloud costs         | 3     | 3     | Agnes Lungu     |
| R04    | Third-party API (PrescribeLink or PayBridge) changes or fails  | 3     | 4     | Thandiwe Moyo   |
| R05    | Video quality poor on provincial mobile networks               | 4     | 3     | Lucy Hamoonga   |
| R06    | Key-person dependency on Chipo Mumba for infrastructure        | 3     | 5     | Daniel Chileshe |
| R07    | Clinicians reject the new screens as slower than CareBook      | 3     | 4     | Dr Mwila Sakala |
| R08    | Data protection impact assessment not approved in time         | 2     | 5     | Grace Tembo     |

## 12. Assignments

| **\#** | **Assignment**            | **With chapter** | **Deliverable**                                                                                                                 |
|--------|---------------------------|------------------|---------------------------------------------------------------------------------------------------------------------------------|
| 1      | Project charter           | Ch 3             | Charter reconciling clinicians' usability needs with the compliance officer's security demands                                  |
| 2      | Product backlog           | Ch 4             | At least 15 INVEST user stories with Given-When-Then criteria covering authentication, billing, video and legacy data ingestion |
| 3      | Cloud cost projection     | Ch 6             | AWS versus Azure monthly cost model under low, expected and peak load, in K at the book rate                                    |
| 4      | Change control assessment | Ch 11            | Formal impact assessment of the symptom checker change request for the change control board                                     |

## 13. Where the case appears in the book

| **Chapter** | **HealthSync focus**                                                                           |
|-------------|------------------------------------------------------------------------------------------------|
| 1           | Why CareBook fails; what makes HealthSync an IT project rather than a building project         |
| 2           | Choosing hybrid delivery for a regulated migration                                             |
| 3           | Business case (NPV at 18%), charter, stakeholder register; Assignment 1                        |
| 4           | Backlog and WBS; Complication 1; Assignment 2                                                  |
| 5           | Release plan from velocity; critical path for migration and cutover milestones                 |
| 6           | Capital budget and tranches; cloud costs and exchange-rate risk; EVM at Month 3; Assignment 3  |
| 7           | Seed risk register; Monte Carlo on the migration; Complication 2                               |
| 8           | Quality gates in GitHub Actions and SonarQube; test strategy for video                         |
| 9           | Team Atlas and Team Baobab; distributed contractors; conflict between marketing and compliance |
| 10          | PrescribeLink and PayBridge contracts; cloud SLA review; data processing location              |
| 11          | Burn-up and cumulative flow; Complication 3; Assignment 4                                      |
| 12          | Recovery plan; phased cutover by facility; rollback; post-implementation review                |
| 13          | AI usage policy for the HealthSync team; prompt log examples                                   |
| 14          | Full capstone on HealthSync or an alternative domain                                           |
