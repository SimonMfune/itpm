# Capstone sprint II: procurement and contracts

**Chapter:** 10 of *Information Technology Project Management: Traditional Foundations, Agile Delivery and AI-Enhanced Practice*

## You will produce

1. A make, buy or subscribe analysis for one significant component of your capstone, with three-year costs and non-financial criteria (`make_buy_subscribe.csv`).
2. A set of mandatory and weighted criteria for selecting one supplier or service (`supplier_criteria.csv`).
3. A review of one real cloud or SaaS SLA your project depends on, covering availability, credits, exclusions, data location and exit (`sla_review_checklist.md`).
4. A licence check of your repository with an exported SBOM and a note on any exceptions.

## Steps for the licence check

1. On GitHub, open your repository's **Insights**, then **Dependency graph**, and use **Export SBOM** (SPDX format). Other tools, such as an SBOM generator in your CI pipeline, also work.
2. List each dependency's licence. Flag copyleft licences (GPL, AGPL) and any unknown licences.
3. Write a short note on each exception and what you will do about it.

## Tips

- Three-year costs include running and exit costs, not only the price of year one.
- A mandatory criterion is pass or fail. Do not give it a weight.
