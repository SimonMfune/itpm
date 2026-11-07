# Capstone project

The capstone asks your team to take an IT project from initiation to a working product and an honest look back, as HealthSync's people did. Chapter 14 (Section 14.8) of *Information Technology Project Management: Traditional Foundations, Agile Delivery and AI-Enhanced Practice* sets out the full brief.

## Choose a case

HealthSync itself (the Case Bible in `case/`), one of the alternative cases in `case_briefs.md`, or a case your tutor approves. Your tutor will release complications during the semester; see `complication_cards/`.

## Team

Four to six people: a project manager, a Product Owner, and members responsible for the backlog and build, quality and testing, and risk and finance. Roles can rotate between sprints, but every deliverable has a named owner.

## Timeline (Figure 14.5)

| Weeks | Work | Points |
|---|---|---|
| 1 to 3 | Initiate: charter and stakeholders | 15 |
| 3 to 5 | Scope, backlog and WBS | 20 |
| 4 to 6 | Estimate, schedule and budget | 20 |
| 5 to 14 | Sprints 1 to 5 in Jira or Azure DevOps | 10 |
| 5 to 14 | Risk register and quality gates | 15 |
| 14 to 15 | Showcase and post-mortem | 20 |

Checkpoints: charter approved in week 3, plan baselined in week 6, mid-point review in week 10, final presentation in week 15.

## Deliverables and rubric (Table 14.5, 100 points)

| Rubric area (points) | Deliverables | What good looks like | Chapters |
|---|---|---|---|
| Initiation and strategic alignment (15) | Charter (10); stakeholder register with communication plan (5) | Measurable objectives and benefits; constraints and decision rules; scope in and out; engagement levels and actions | 1, 3, 9 |
| Scope and backlog (20) | Backlog of INVEST stories with Given-When-Then criteria (10); WBS or epic structure (10) | Stories that a tester could check; non-functional requirements; a WBS covering front end, back end, data, infrastructure and QA | 4 |
| Scheduling, estimation and financials (20) | Estimates with justification and critical path (10); budget and cloud cost projection (10) | Reference stories; ranges, not single numbers; full-cost budget including running costs | 5, 6 |
| Execution, quality and risk (25) | Live tool use across sprints (10); risk register with owners and triggers (10); quality gates (5) | Authentic task history; risks specific to your system, scored and triggered; automated checks and review steps | 7, 8, 11 |
| Presentation and retrospective (20) | Showcase of a working MVP or high-fidelity simulation (10); post-mortem (10) | A demonstration tied to the backlog; velocity, variance and lessons stated honestly, with evidence | 12 |

`rubric.csv` is the same rubric as a scoring sheet.

## Folders

| Folder | Use |
|---|---|
| `sprint1/` | Capstone sprint I (Chapter 9): team charter, RACI, skills matrix, communication plan, health check |
| `sprint2/` | Capstone sprint II (Chapter 10): make, buy or subscribe; supplier criteria; SLA review; licence check |
| `templates/` | Templates for the capstone deliverables. The project document templates are in `/templates` (Appendix C) |
| `complication_cards/` | How complications are released |

## Using AI in the capstone (Section 14.8.6)

- Use only tools your institution allows, and never enter personal data, credentials or confidential data from a real organisation.
- Keep a prompt log for every AI-assisted deliverable (`appendixA/prompt_log_template.csv`).
- Check every number, citation and claim an AI produces; recompute calculations yourself.
- Disclose AI use in each deliverable in one or two sentences.
- Be able to explain everything you submit, including AI-generated code, in your own words.

## Three habits of strong capstones

**Connect the artefacts:** your risks appear in your backlog and budget, your benefits in your charter and post-mortem, your velocity in your forecast. **Use evidence:** every claim in the post-mortem points to something in your tool, repository or records. **Tell the truth:** a team that missed its forecast, understands why and changed course scores better than one whose every chart is green.
