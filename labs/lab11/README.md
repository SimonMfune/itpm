# Lab 11: Deployment, cutover planning and rolling out

**Chapters:** Chapter 12 of *Information Technology Project Management: Traditional Foundations, Agile Delivery and AI-Enhanced Practice*  
**Files:** `data/healthsync_incidents.csv`

## Purpose
Plan and rehearse a cutover.

## You will produce

1. A minute-by-minute cutover runbook for a parallel run of HealthSync and CareBook at one provincial clinic for one week, including checkpoints and the daily comparison of bookings.
2. A rollback plan with a rollback deadline.
3. A go/no-go checklist with evidence for each criterion.

## The data

`data/healthsync_incidents.csv` lists the incidents logged in the ten days of hypercare in each of HealthSync's three phases (Figure 12.5), with priorities, categories and times. Use it to plan support for your clinic and to set realistic exit criteria.

## Steps

1. Choose a provincial clinic. List what runs in parallel, who enters what in each system and how differences are reconciled each day.
2. Write the runbook: timed tasks with owners, dependencies and a completion check for each; checkpoints where the team decides to continue.
3. Work out the rollback deadline from the service start time, the rehearsed rollback duration and a buffer. State the triggers for rollback.
4. Write the go/no-go checklist using Table 12.3 as a model: criteria agreed in advance, the evidence for each and a named decision-maker. Allow for "go with conditions".
5. From the incidents file, work out on which day each phase met the hypercare exit criteria in Section 12.7.2.

## Tips

- An assurance ("the team is confident") is not evidence. Ask what would show it.
- Round the rehearsed rollback time up, not down.

## Optional AI extension (Appendix A, Table A.5)

Generate a first draft of the cutover runbook from your plan; red-team it for missing checkpoints and rollback triggers. Patterns: A.4.3, A.4.7. Submit: Draft runbook; red-team findings; final runbook with changes marked.

The lab deliverable must stand on its own, and your critique of the AI output is the part that is assessed. See `appendixA/`.

## Before you submit

- Check every figure you report. Recompute anything a tool or an AI assistant produced.
- If you used AI, keep a prompt log (`appendixA/prompt_log_template.csv`) and add a one- or two-sentence disclosure to your deliverable.
- Name each file with your team or student ID and the lab number.

Your tutor marks this lab out of 20 against the deliverables above.
