# Lab 5: Scheduling, critical path and PERT

**Chapters:** Chapter 5 of *Information Technology Project Management: Traditional Foundations, Agile Delivery and AI-Enhanced Practice*  
**Files:** `data/healthsync_schedule.xlsx`

## Purpose
Build HealthSync's migration and cutover network and decide how to protect the go-live date.

## You will produce

1. The migration and cutover network in Microsoft Project desktop or ProjectLibre.
2. The critical path and the total slack for every activity.
3. A PERT probability for the go-live date.
4. A recommended crashing option, with its cost.

## The data

`data/healthsync_schedule.xlsx` has the thirteen activities of Table 5.3 with predecessors, WBS codes and three-point estimates, and the crash options from Worked Example 5.5.

## Steps

1. Enter the activities in ProjectLibre (free) or Microsoft Project desktop. Use the "Planned" durations and finish-to-start links. Make K a milestone.
2. Show the critical path and the total slack column. Check your result against the forward and backward pass in Worked Example 5.3.
3. Calculate the PERT expected duration and standard deviation of the critical path from the three-point estimates. Find the probability of finishing within 100 working days.
4. Using the crash options, find the cheapest way to bring the finish forward to day 92. Watch for a second critical path appearing after the first crash.
5. Write a short recommendation, including the risks of crashing software work.

## Tips

- Add variances along the path, not standard deviations.
- Crashing an activity that is not critical buys nothing.

## Optional AI extension (Appendix A, Table A.5)

Ask the model to validate your critical path and PERT probability step by step. Patterns: A.4.5. Submit: Model working with the formula step checked; corrections.

The lab deliverable must stand on its own, and your critique of the AI output is the part that is assessed. See `appendixA/`.

## Before you submit

- Check every figure you report. Recompute anything a tool or an AI assistant produced.
- If you used AI, keep a prompt log (`appendixA/prompt_log_template.csv`) and add a one- or two-sentence disclosure to your deliverable.
- Name each file with your team or student ID and the lab number.

Your tutor marks this lab out of 20 against the deliverables above.
