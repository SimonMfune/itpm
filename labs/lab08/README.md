# Lab 8: Quantifying IT risk and building a digital register

**Chapters:** Chapter 7 of *Information Technology Project Management: Traditional Foundations, Agile Delivery and AI-Enhanced Practice*  
**Files:** `data/healthsync_risks.xlsx`, `data/healthsync_schedule.xlsx`

## Purpose
Build HealthSync's risk register, and use simulation and decision analysis to support the decision about e-prescribing after Complication 2.

## You will produce

1. A digital risk register in a spreadsheet or Jira, extending the seed register with at least six new risks written as cause, event and effect, including two opportunities.
2. A probability and impact heat map.
3. A STRIDE table for one HealthSync component.
4. The decision tree from Worked Example 7.2, with a sensitivity check.
5. A Monte Carlo model of the migration network that reproduces Worked Example 7.3 within a few percentage points.
6. A two-page paper for the steering group that brings these together: the risks that matter most, the recommended responses and their cost, the forecast with its confidence, and the message to clinicians.

## The data

- `data/healthsync_risks.xlsx`: the eight seed risks, the scales (Table 7.3), the risk appetite (Table 7.1) and a heat map that counts the risks in the *Register* sheet automatically.
- `data/healthsync_schedule.xlsx`: three-point estimates for the migration network.

## Steps

1. Rewrite the seed risks in cause, event and effect form. Add at least six new risks, two of them opportunities, with owners, responses and triggers.
2. Check the heat map. Escalate anything that breaches the appetite thresholds.
3. Choose one component (the e-prescription adapter, payments or video) and complete a STRIDE table with controls.
4. Rebuild the decision tree in Worked Example 7.2 and find the point at which the decision changes.
5. Build the Monte Carlo model in a spreadsheet or in Python (Appendix D shows how), with 10,000 runs, as in Table 7.5. Report P50, P80 and the chance of finishing within 100 days.
6. Write the steering paper. Recommend; do not just repeat the register.

## Tips

- An opportunity is not a threat turned round. Ask what could go better than planned.
- Too few runs give unstable percentages. Rerun with a new seed and compare.

## Optional AI extension (Appendix A, Table A.5)

Build a risk-register assistant with structured output (JSON or Markdown); run a red-team review. Patterns: A.4.13, A.4.7. Submit: System prompt; known-answer test results; red-team findings mapped to the register.

The lab deliverable must stand on its own, and your critique of the AI output is the part that is assessed. See `appendixA/`.

## Before you submit

- Check every figure you report. Recompute anything a tool or an AI assistant produced.
- If you used AI, keep a prompt log (`appendixA/prompt_log_template.csv`) and add a one- or two-sentence disclosure to your deliverable.
- Name each file with your team or student ID and the lab number.

Your tutor marks this lab out of 20 against the deliverables above.
