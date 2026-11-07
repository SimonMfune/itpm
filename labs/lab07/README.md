# Lab 7: Continuous integration and automated quality gates

**Chapters:** Chapter 8 of *Information Technology Project Management: Traditional Foundations, Agile Delivery and AI-Enhanced Practice*  
**Files:** `data/healthsync_quality.xlsx`, `labs/lab07/starter/`

## Purpose
Build a working CI pipeline with automated quality gates for a small HealthSync service, and use quality data to make a decision.

## You will produce

1. A GitHub repository with a GitHub Actions workflow that builds, tests and analyses the code on every pull request.
2. A SonarQube quality gate on new code with at least four conditions.
3. Branch protection that blocks merges failing the gate.
4. A concurrency test that fails against the original booking code and passes against the fixed version.
5. A Pareto chart and an XmR chart from the HealthSync quality dataset.
6. A one-page note to the Product Owner recommending how much capacity to give to technical debt.

## The starter code

`starter/` is a tiny booking service in Python, in two versions:

- `booking_original.py` checks that a slot is free and then saves the booking. It passed review and every single-request test, and it caused the double booking in the pilot (Chapter 8).
- `booking_fixed.py` adds a database constraint so that two bookings for the same clinician and slot cannot be saved.

`tests/test_booking_basic.py` runs the same single-request tests on both versions. They all pass, which is why they missed the problem. `.github/workflows/ci.yml` runs the tests on every pull request.

## Steps

1. Create a new GitHub repository. Copy everything in `starter/` into it, including the hidden `.github` folder, and push. Check that the workflow runs and passes on the Actions tab.
2. Set up SonarQube analysis. SonarQube Cloud is free for public repositories; follow its GitHub Actions instructions, add the `SONAR_TOKEN` secret, complete `sonar-project.properties` and add the scan step to the workflow. Define a quality gate on new code with at least four conditions, using Table 8.4 as a guide.
3. Protect the main branch: require pull requests and require the CI and SonarQube checks to pass.
4. Write `tests/test_concurrency.py`: start two bookings for the same clinician and slot at the same moment (for example, two threads that wait on a `threading.Barrier`) and assert that exactly one booking exists. Show that it fails against `booking_original` and passes against `booking_fixed`. Explain in two sentences why the single-request tests missed the defect.
5. Open `data/healthsync_quality.xlsx`. Draw a Pareto chart from the *Defect log* sheet and an XmR chart from the *Pipeline* sheet. Check your limits against Worked Example 8.4.
6. Write the note on technical debt capacity, using the *Code quality* and *Defects by sprint* sheets.

## Tips

- A concurrency test must run the requests in parallel. Two calls one after the other prove nothing.
- Calculate XmR limits from the average moving range, not the standard deviation.
- Put the gate on new code, so that the team is not blocked by debt it inherited.

## Optional AI extension (Appendix A, Table A.5)

Generate tests from requirements and risks; prove they fail against a broken version. Patterns: A.4.8. Submit: Tests; mutation or broken-version results.

The lab deliverable must stand on its own, and your critique of the AI output is the part that is assessed. See `appendixA/`.

## Before you submit

- Check every figure you report. Recompute anything a tool or an AI assistant produced.
- If you used AI, keep a prompt log (`appendixA/prompt_log_template.csv`) and add a one- or two-sentence disclosure to your deliverable.
- Name each file with your team or student ID and the lab number.

Your tutor marks this lab out of 20 against the deliverables above.
