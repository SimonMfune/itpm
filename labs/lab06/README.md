# Lab 6: Cloud economics and FinOps budgeting

**Chapters:** Chapter 6 of *Information Technology Project Management: Traditional Foundations, Agile Delivery and AI-Enhanced Practice*  
**Files:** `data/cloud_pricing_export.csv`

## Purpose
Build HealthSync's cloud cost model and the controls that keep it within the K95,000 monthly cap.

## You will produce

1. A cost model for AWS and Azure under low, expected and peak load, in US dollars and kwacha at the book rate (USD 1 = K26), with and without commitments (**Assignment 3**).
2. An exchange-rate sensitivity table.
3. A tagging policy.
4. Budgets and forecast alerts for each environment.
5. An EVM spreadsheet reproducing Worked Example 6.4.

## The data

`data/cloud_pricing_export.csv` is an illustrative calculator export: one row per component, for each provider and load. `commitment_eligible` marks the resources that run all the time, and `one_year_commitment_discount` gives the discount for a one-year commitment. The AWS expected-load rows reproduce Worked Example 6.2. *The prices are illustrative, not current list prices.*

## Steps

1. Load the CSV into a spreadsheet. Total each provider and load on demand, then apply commitments only to the eligible rows.
2. Convert to kwacha and compare each total with the K95,000 cap.
3. Build a sensitivity table for exchange rates from K22 to K34 to the dollar. Find the rate at which each option breaks the cap.
4. Write a tagging policy using Table 6.3: mandatory tags, how they are enforced and what happens to untagged resources.
5. Set out budgets and forecast alerts for development, test and production, with thresholds and named recipients. If you have an Azure or AWS free account, configure one for real (the Tool spotlight in Chapter 6 shows Azure).
6. Reproduce Worked Example 6.4 in a spreadsheet with formulas, and interpret TCPI.

## Tips

- Commit only to the steady baseline. Committing peak capacity pays for machines that sit idle.
- Compare like with like: the same machine sizes and the same services on both providers.

## Optional AI extension (Appendix A, Table A.5)

Produce a FinOps report from a pricing export; compare SLAs. Patterns: A.4.6, A.4.10. Submit: Report with every figure recomputed; recommendations rewritten with evidence.

The lab deliverable must stand on its own, and your critique of the AI output is the part that is assessed. See `appendixA/`.

## Before you submit

- Check every figure you report. Recompute anything a tool or an AI assistant produced.
- If you used AI, keep a prompt log (`appendixA/prompt_log_template.csv`) and add a one- or two-sentence disclosure to your deliverable.
- Name each file with your team or student ID and the lab number.

Your tutor marks this lab out of 20 against the deliverables above.
