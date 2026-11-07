# Lab 9: Tracking performance via dashboards

**Chapters:** Chapter 11 of *Information Technology Project Management: Traditional Foundations, Agile Delivery and AI-Enhanced Practice*  
**Files:** `data/healthsync_sprints.csv`, `data/healthsync_work_items.csv`, `data/healthsync_atlas_cfd.csv`

## Purpose
Build and interpret a project dashboard from the HealthSync data.

## You will produce

1. A dashboard with a burn-up, a cumulative flow diagram, a cycle-time chart and a created-versus-resolved chart, in Jira, Azure DevOps or a spreadsheet.
2. AgileEVM calculations for Sprints 6 and 9.
3. A one-page status report with a RAG rating and a request for decision.

## The data

- `data/healthsync_sprints.csv`: Sprints 1 to 9, both teams combined. Points done, MVP points done, release scope, actual cost (K), escaped defects, open SonarQube issues, risk exposure and the team safety check.
- `data/healthsync_work_items.csv`: 60 items Team Atlas finished in Sprints 7 to 9, with the working day each was created, started and finished. Day 1 is the first day of Sprint 7; a negative day means the item started in Sprint 6.
- `data/healthsync_atlas_cfd.csv`: daily counts of Team Atlas items by status in Sprints 8 and 9.

## Steps

1. Build the release burn-up from the sprints file: cumulative points done against release scope.
2. Build the cumulative flow diagram from the CFD file, and the cycle-time scatter plot and created-versus-resolved chart from the work items file. Check your 50th and 85th percentiles against Figure 11.3.
3. If you use Jira or Azure DevOps, configure the same four charts on your capstone project, where the tool collects the history itself.
4. Calculate AgileEVM for Sprints 6 and 9: the software budget is K2,600,000 for the 640-point MVP over ten sprints at 68 points a sprint. Use MVP points only for earned value.
5. Write the status report: most important news first, a RAG rating that the forecast supports and a clear request for decision.

## Tips

- Use the current figures. The Sprint 6 CPI is history by Sprint 9.
- The 34 points outside the MVP cost money but earn nothing against the MVP baseline.

## Optional AI extension (Appendix A, Table A.5)

Draft the status report with insight extraction; recompute every index. Patterns: A.4.11. Submit: Draft; your recomputation; final report with disclosure.

The lab deliverable must stand on its own, and your critique of the AI output is the part that is assessed. See `appendixA/`.

## Before you submit

- Check every figure you report. Recompute anything a tool or an AI assistant produced.
- If you used AI, keep a prompt log (`appendixA/prompt_log_template.csv`) and add a one- or two-sentence disclosure to your deliverable.
- Name each file with your team or student ID and the lab number.

Your tutor marks this lab out of 20 against the deliverables above.
