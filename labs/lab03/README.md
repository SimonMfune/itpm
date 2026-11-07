# Lab 3: Requirements architecture and backlog refinement

**Chapters:** Chapter 4 of *Information Technology Project Management: Traditional Foundations, Agile Delivery and AI-Enhanced Practice*  
**Files:** `data/healthsync_backlog.csv`

## Purpose
Turn HealthSync's requirements into a structured, ordered backlog.

## You will produce

1. A level 3 WBS for two HealthSync deliverables, with one WBS dictionary entry.
2. A backlog in Jira of at least 15 user stories that meet INVEST, with Given-When-Then acceptance criteria, covering authentication, billing, video and legacy data ingestion (**Assignment 2**).
3. A Definition of Ready and a Definition of Done.
4. A refinement session in which you split two epics into stories.

## The data

`data/healthsync_backlog.csv` is HealthSync's seed backlog: 8 epics and 52 stories, partly refined. Refined stories have points and acceptance criteria; others do not. Epics EP-05 (E-prescriptions) and EP-07 (Notifications) have not yet been split into stories: those are the two you split in step 4. Each item carries its WBS code and a MoSCoW priority.

## Steps

1. Import the CSV into Jira with its CSV importer (Atlassian's help pages explain the current steps), mapping `type`, `title`, `user_story` and `story_points`. Or work in a spreadsheet if your tutor agrees.
2. Choose two level 2 deliverables from Figure 4.2 and break them down to level 3. Write a WBS dictionary entry for one work package, using Table 4.4 as a model.
3. Write or refine at least 15 stories for Assignment 2. Each needs Given-When-Then criteria that include at least one unhappy path. Include consent and audit-log scenarios where personal data is involved.
4. Run a refinement session: split EP-05 and EP-07 into vertical slices, using the splitting patterns in Section 4.4.1.
5. Agree a Definition of Ready and a Definition of Done for your team.

## Tips

- "Build the payments table" is a horizontal slice. Nobody can use it on its own.
- Legacy data ingestion is not one story. Look at the MIG items for the pieces.

## Optional AI extension (Appendix A, Table A.5)

Generate five user stories with data protection constraints from interview notes, then refine them through at least two rounds. Patterns: A.4.4. Submit: Each round's prompt and output; traceability of every story to the notes.

The lab deliverable must stand on its own, and your critique of the AI output is the part that is assessed. See `appendixA/`.

## Before you submit

- Check every figure you report. Recompute anything a tool or an AI assistant produced.
- If you used AI, keep a prompt log (`appendixA/prompt_log_template.csv`) and add a one- or two-sentence disclosure to your deliverable.
- Name each file with your team or student ID and the lab number.

Your tutor marks this lab out of 20 against the deliverables above.
