# Prompt library

The fourteen prompt patterns from Appendix A of *Information Technology Project Management: Traditional Foundations, Agile Delivery and AI-Enhanced Practice*, one for each chapter. Each entry gives the purpose, when to use it, the template and the checks to make. Replace everything in [SQUARE BRACKETS]. The book gives worked examples, variations and known failures for each pattern.


## A.4.1 Role-based prompting (Chapter 1)

**Purpose:** Role-based prompting asks the model to answer from a defined professional point of view, for a defined audience. A role focuses the answer and makes it more critical than a generic request such as "Check this brief". It suits reviews of project briefs, business cases, charters and plans, and the early search for failure patterns that Chapter 1 described.

**Use it when** you want a document challenged from a perspective you lack, such as an auditor's, a finance director's or a regulator's. **Avoid it when** the role would need knowledge the model cannot have, such as your organisation's history, or when you would be tempted to treat the role's opinion as expert advice.


**Template:**

```text
You are [ROLE] reviewing [DOCUMENT TYPE] for [AUDIENCE].
Be direct and specific.

Context: [THE FACTS OF THE PROJECT, WITH NAMES OF PRIVATE
INDIVIDUALS REMOVED]

Task: Identify the [NUMBER] most serious [RISKS / WEAKNESSES
/ GAPS] that [AUDIENCE] may not have noticed. For each, say
why it matters and what evidence you would ask for.

Constraints: Use only the facts given. Label any assumption
as an assumption. Do not rank by confidence you do not have;
explain the basis of any ranking.

Output format: A numbered list, then one paragraph of
overall opinion.
```


**Checks:** Compare each risk with the facts you hold. Add the risks the model could not see, especially those about people, history and politics. Ask a domain expert to challenge the ranking before it reaches a decision-maker. Treat the "overall opinion" as a prompt for discussion, not a finding.


## A.4.2 Few-shot prompting (Chapter 2)

**Purpose:** Few-shot prompting gives the model two or three worked examples of a task before asking it to do a new one (Brown et al., 2020). The examples teach the format and the kind of reasoning wanted, which a plain instruction often fails to convey. It suits classification and recommendation tasks that must be done consistently, such as choosing a delivery approach, categorising change requests or tagging risks.

**Use it when** you can show what good looks like more easily than you can describe it, and when consistency across many items matters. **Avoid it when** your examples are few, similar or unrepresentative, because the model will copy their limits as faithfully as their strengths.


**Template:**

```text
You [DO THE TASK, e.g. recommend delivery approaches for IT
projects]. Follow the format of the examples exactly.

Example 1
[INPUT]: [A CLEAR CASE]
[OUTPUT]: [THE ANSWER]
Reason: [THE REASONING, NAMING THE FACTORS THAT DECIDED IT]

Example 2
[INPUT]: [A CONTRASTING CASE]
[OUTPUT]: [A DIFFERENT ANSWER]
Reason: [THE REASONING, USING DIFFERENT FACTORS]

Now do this one
[INPUT]: [THE NEW CASE]
If the information is not enough to decide, say what else
you would need to know.
```


**Checks:** Run the suitability filter from Section 2.7.1 on the same case and compare. Where the filter raises a factor the model ignored, add an example that reasons from that factor and run the prompt again. Swap the order of the examples and see whether the answer changes; if it does, the model is pattern-matching rather than reasoning.


## A.4.3 Template-enforced prompting (Chapter 3)

**Purpose:** Template-enforced prompting gives the model a fixed document structure and strict rules about what it may and may not write. It suits formal documents with standard headings, such as charters, business case summaries, terms of reference and closure reports, where the main risk is that the model invents facts to fill gaps.

**Use it when** the headings are known and the source facts exist in documents you can supply. **Avoid it when** the hard part of the document is agreement, not drafting. Decision rights, tolerances and approvals have to be negotiated with people; a model can format them but cannot settle them.


**Template:**

```text
You are drafting a [DOCUMENT TYPE]. Use ONLY the facts below.
Where a heading has no supporting fact, write [TO CONFIRM].
Do not invent names, dates, figures or commitments.

Template headings, in this order:
[1 HEADING  2 HEADING  3 HEADING ...]

Facts: [PASTE THE SOURCE SECTIONS]

Output: the headings in order, each with short bullet
points. After each bullet, give the source section in
brackets.
```


**Checks:** Read every line against the source and highlight anything you cannot trace. Check that [TO CONFIRM] appears wherever it should; a template output with no gaps is suspicious. Write the judgement sections yourself, especially decision rights, tolerances and success criteria, and agree them with the people concerned.


## A.4.4 Contextual breakdown prompting (Chapter 4)

**Purpose:** Contextual breakdown prompting gives the model the context it needs to break a large input into structured pieces: the users, the constraints, the required format and what to do when the input is unclear. It suits turning interview notes, workshop transcripts and support tickets into draft user stories with acceptance criteria.

**Use it when** you have raw material from users and need a first structured draft for refinement. **Avoid it when** there is no source material, because the model will then generate requirements from general knowledge, which is how products end up with features nobody asked for.


**Template:**

```text
Context: [PRODUCT AND USERS]. Users: [USER TYPES, WITH ANY
CONDITIONS SUCH AS SLOW MOBILE DATA].
Constraints: [REGULATORY AND DESIGN CONSTRAINTS, e.g. every
read of patient data is audit-logged; consent is required
before processing personal data].

Task: From the notes below, write user stories.
Rules:
- Use "As a ..., I want ..., so that ...".
- Each story must meet INVEST; split any that are too large.
- Give 2 or 3 Given-When-Then scenarios per story,
  including at least one unhappy path.
- For each story, state which constraint applies, if any.
- List non-functional needs separately, not as stories.
- Do not add needs the notes do not mention. For each
  story, quote the sentence in the notes it comes from.
- List anything unclear under "Questions for the
  Product Owner".

Notes: [PASTE NOTES, NAMES REPLACED WITH ROLES]
```


**Checks:** Trace every story and scenario to a sentence in the notes, and delete anything you cannot trace. Check each story against INVEST yourself. Go through the constraints one by one and ask which stories each affects; add the scenarios the model missed. Give the "Questions for the Product Owner" list to the Product Owner, not back to the model.


## A.4.5 Chain-of-thought prompting (Chapter 5)

**Purpose:** Chain-of-thought prompting asks the model to work through a problem step by step and show every step. It suits checking calculations such as critical path analysis, PERT estimates, function point counts, story point conversions, NPV and earned value. Research showed that asking for intermediate steps improves the accuracy of large models on multi-step problems (Wei et al., 2022). For project work, its main value is that it makes the working visible, so that a person can check each step.

**Use it when** you have already done a calculation and want a second, independent working to compare with, or when you want the method laid out so you can follow it. **Avoid it when** you would accept the final number without reading the steps. Chain-of-thought does not stop a model making mistakes; it shows where they are, but only to someone who looks.


**Template:**

```text
Check this calculation. Work step by step and show every
step. Do not skip to the answer.

Data: [PASTE THE TABLE OR INPUTS]
Method: [NAME THE METHOD, e.g. CPM forward and backward
pass, then PERT]

Steps:
1. [FIRST STEP, e.g. forward pass: ES and EF]
2. [SECOND STEP]
3. [...]
For every step that applies a formula, write the formula
first, then substitute the numbers.
After the last step, re-check each step against the rule
it uses and list any corrections.
```


**Checks:** Rebuild the calculation in a spreadsheet or in code. Check the step that applies a formula against a textbook source, here Worked Examples 5.3 and 5.4. If two independent methods disagree, find the first step where they part, rather than choosing the answer you prefer.


## A.4.6 Data-informed prompting (Chapter 6)

**Purpose:** Data-informed prompting gives the model the actual data it should reason from, with the context, the audience and the rules for using the data, and tells it not to go beyond the data. It suits turning raw exports, such as a cloud pricing calculator estimate, a cost report or a timesheet extract, into a short report for decision-makers.

**Use it when** the data is in hand and the task is to summarise it, convert it or compare it with a threshold. **Avoid it when** the decision depends mostly on information that is not in the data, such as future usage or supplier negotiations, because the model will fill the gap with general knowledge presented as fact.


**Template:**

```text
Role: [ROLE, e.g. FinOps analyst] writing for [AUDIENCE].
Context: [THE PROJECT, THRESHOLDS AND RULES, e.g. running-
cost cap K95,000 a month; convert USD at USD 1 = K26].
Data: [PASTE THE EXPORT OR TABLE]
Offers or options available: [ONLY THE ONES YOU HAVE]

Task: A one-page report with (1) [FIRST FIGURE]; (2) the
position against [THRESHOLD]; (3) [SENSITIVITY, e.g. the
exchange rate at which the cap is breached]; (4) [NUMBER]
recommendations.
Rules: Use only the data above. Show the calculation for
every figure. If you need a figure that is not given, say
so instead of guessing. For each recommendation, name the
data it rests on and the main risk of following it.
```


**Checks:** Recalculate every figure. For each recommendation, ask what data it depends on and whether that data was supplied. Check any percentage or price that did not come from your data against the supplier's own published terms, and remove it if you cannot.


## A.4.7 Adversarial prompting (Chapter 7)

**Purpose:** Adversarial prompting, or red teaming, asks the model to attack a design instead of helping to build it: to play an attacker, a sceptical auditor or a regulator and find what could go wrong. It suits threat modelling, pre-mortems and reviews of architectures, plans and business cases, where the people who designed something find it hardest to see its weaknesses.

**Use it when** a design or plan exists and you want to widen the search for failure modes before a review with experts. **Avoid it when** you would enter real security findings, credentials or configuration details into the tool, which CareGrid's policy prohibits, or when you would treat the output as a security assessment.


**Template:**

```text
Role: [ADVERSARY, e.g. an experienced attacker and a
sceptical security auditor, working together].
Context: [SYSTEM OR PLAN, AND ITS SETTING, e.g. a telehealth
platform; health data is sensitive personal data under the
Data Protection Act 2021].
Design: [COMPONENT LIST AND DATA FLOWS, WITH NO SECRETS]
Treat every external system and supplier as untrusted. For
each trust boundary, list what the other side could do
wrong.

Task: (1) Using [FRAMEWORK, e.g. STRIDE], list the [NUMBER]
most serious ways [THE SYSTEM OR PLAN] could fail or be
attacked. (2) For each, give the component, the likely
attack or failure and one control. (3) Name the three you
would fix first and why. (4) Say what you could not assess
from the information given.
```


**Checks:** Reread the prompt for words that tell the model what to trust, and remove them. Check every legal and numerical claim against its source. Compare the output with a structured method, such as STRIDE applied by the team, and add the threats the model missed. Have a security specialist review anything that will change the design.


## A.4.8 Code-to-test prompting (Chapter 8)

**Purpose:** Code-to-test prompting asks the model to generate test scenarios, and often test code, from code, an interface or a description of the architecture. It is quick and good at the routine cases that people find tedious to write. It suits building a first test suite, filling coverage gaps and drafting acceptance tests from stories.

**Use it when** you have the requirements and the risk register as well as the code, so that tests can be generated from what the system should do, not only from what it does. **Avoid it when** the tests would be the only evidence of quality, or when you cannot run them against a deliberately broken version.


**Template:**

```text
Role: senior test engineer for [TYPE OF SYSTEM].
Context: [THE SERVICE AND ITS USERS]. Requirements: [PASTE
THE RELEVANT STORIES, ACCEPTANCE CRITERIA AND NON-FUNCTIONAL
REQUIREMENTS]. Known risks: [PASTE RELEVANT RISKS].
Code: [PASTE THE FUNCTION AND ITS INTERFACES, NO SECRETS]

Task: (1) List the test scenarios needed for confidence
that [FEATURE] works, starting from the requirements and
risks, not the code. (2) Add scenarios designed to break
the design: concurrent requests, partial failures, retries,
time zones and data from more than one [SITE OR TENANT].
(3) Write unit tests for the five most important, using
[TEST FRAMEWORK] and mocks for [DEPENDENCIES]. (4) For
each test, name the defect it would catch.
```


**Checks:** Test the tests. Introduce a known defect, or run mutation testing, and confirm that the generated tests fail. A test that cannot fail is not testing anything. Check each standard and version the model names against the project's own requirements. CareGrid's policy requires AI-generated tests to fail against a deliberately broken version before they are trusted.


## A.4.9 Persona-driven simulation (Chapter 9)

**Purpose:** Persona-driven simulation asks the model to play a stakeholder so that you can rehearse a difficult conversation before having it. You describe the persona's role, interests, pressures and style, play your own part and then ask for feedback. It suits preparing negotiations, delivering bad news, handling conflict and practising communication with a sponsor or a resistant user group.

**Use it when** you want to practise your own words and responses, and to anticipate objections. **Avoid it when** you would treat the simulation as a prediction of what a real person will do, or when describing the person would mean entering personal data about a real colleague into a tool not approved for it.


**Template:**

```text
Play [ROLE, NOT A REAL NAME], [POSITION] in [ORGANISATION
TYPE]. Your interests: [WHAT THEY WANT]. Your pressures:
[DEADLINES, TARGETS, COMPETITORS]. Your style: [e.g.
confident and direct].
Stay difficult. Do not concede anything unless I address
your underlying interest directly, and push back at least
twice before agreeing to any proposal.

I am [YOUR ROLE]. I will open the conversation. Stay in
character. After [NUMBER] exchanges, step out of character
and give feedback: what I did well, where I argued from
positions instead of interests and one thing to try next
time.
```


**Checks:** Use role descriptions, not names and personal details. Instruct the model to stay difficult, and run the rehearsal more than once. Treat the feedback as one view; ask a trusted colleague to role-play the hardest version of the conversation. Treat the output as practice, not prediction.


## A.4.10 Comparative analysis prompting (Chapter 10)

**Purpose:** Comparative analysis prompting asks the model to put several documents side by side against the same criteria, usually as a table. It suits contract and SLA reviews, supplier bid evaluations, RFP response checks and policy gap analysis, where reading several long documents in parallel is slow and differences are easily missed.

**Use it when** you have the full documents and a clear set of criteria, and when a person will read the clauses that matter. **Avoid it when** the table would replace legal or procurement review, or when the documents are confidential and the tool is not approved for confidential business data.


**Template:**

```text
Role: [ROLE, e.g. IT contracts analyst] advising [CLIENT].
Documents: [PASTE THE DOCUMENTS, EACH LABELLED]

Task: Build a table with one row per [SUPPLIER OR DOCUMENT]
and these columns: [CRITERIA]. For every cell, give the
clause number and a verbatim quotation of no more than 20
words. If a document does not address a criterion, write
"Not found", and list the sections you searched.
Then list the [NUMBER] most serious differences or hidden
liabilities for [CLIENT], in order, each citing the cells
it rests on.
```


**Checks:** Check every quotation against the source. Treat any cell without a quotation as unverified. Search the documents yourself for the words that matter, such as "sole", "exclusive", "terminate" and "liability", including definitions and schedules. Use the model to organise the review and a person to read the contract.


## A.4.11 Insight extraction prompting (Chapter 11)

**Purpose:** Insight extraction prompting gives the model structured project data, such as sprint metrics, earned value figures, defect counts and risk scores, and asks it to identify what matters for a named audience and draft a status summary. It suits status reports, dashboard commentary and the preparation of steering group packs, and it can spot patterns across data sources that a busy project manager misses.

**Use it when** the data is current, labelled and complete, and you will check every number before the report is sent. **Avoid it when** the report carries bad news you have not yet framed yourself, because models tend to soften it.


**Template:**

```text
Role: [ROLE] writing for [AUDIENCE], who has [TIME].
Data: [PASTE THE DATA, MARKING EACH VALUE AS CURRENT OR
HISTORICAL, WITH THE DATE OF EACH]
Thresholds: [PASTE THE TOLERANCES AND ESCALATION RULES]

Task: (1) Calculate the current indices, showing every
calculation. (2) State any threshold breaches. (3) Give an
overall RAG status with one sentence of justification,
based on the forecast, not the average. (4) List the three
things that would most change [AUDIENCE]'s decisions, each
with its supporting number. (5) Draft the first paragraph
of a status report, starting with the most important news.
Do not speculate about causes the data does not show.
```


**Checks:** Recompute every index yourself. Check that each value used is the current one. Read the RAG status against the thresholds, not against the model's justification. Rewrite the first sentence so that the most important news comes first. The person who signs the report owns it.


## A.4.12 Synthesis and lessons-learned prompting (Chapter 12)

**Purpose:** Synthesis prompting gives the model a large set of unstructured records, such as retrospective notes, chat exports, incident reports and change logs, and asks it for recurring themes with evidence and proposed lessons. It suits preparing for post-project reviews, lessons-learned workshops and post-implementation reviews, because it reads far more than a facilitator can.

**Use it when** the records have been cleaned of names and personal data and the output will be the starting point for a workshop. **Avoid it when** the synthesis would replace the conversation with the people who did the work, or when the records are one-sided.


**Template:**

```text
Role: an experienced facilitator preparing a blameless
review of [PROJECT].
Material: [PASTE THE RECORDS: RETROSPECTIVES, GOVERNANCE
MINUTES, CHANGE LOG, INCIDENT REPORTS. NAMES REPLACED WITH
ROLES; NO PERSONAL OR HEALTH DATA]

Task: (1) Identify up to [NUMBER] themes. For each, give
the evidence with the source and date of each item.
(2) For each theme, state a lesson as a specific change to
future practice. (3) List any theme where the sources
disagree, and any record later corrected by another.
(4) Do not assign blame to individuals or roles.
(5) Say what the material cannot tell us, and which
records would be needed to find out.
```


**Checks:** Read the sources each theme cites, and check them against later records that may correct them. Include governance records as well as the team's. Delete or rewrite any theme that blames. Let the people who did the work decide the lessons; the synthesis is a draft for the workshop.


## A.4.13 System prompts and structured output (Chapter 13)

**Purpose:** A system prompt sets standing instructions for a reusable assistant: its role, its rules, its output format and what it must refuse. Structured output asks for a fixed format, such as a table or JSON, so that answers can be checked consistently and loaded into other tools. Together they turn a one-off prompt into a small, testable tool. They suit recurring tasks such as drafting risk entries, triaging change requests and producing weekly summaries.

**Use it when** the same task recurs and consistency matters, and when the assistant can be tested on known cases before use. **Avoid it when** the task needs judgement that the rules cannot capture, such as scoring the probability of a risk.


**Template:**

```text
You are [ROLE] for [ORGANISATION OR PROJECT].
Rules:
(1) Use only the information provided. If something is
missing, write "Not provided".
(2) Never [DECISION RESERVED FOR PEOPLE, e.g. estimate
probability or impact]; mark it "For the owner".
(3) [QUALITY RULE, e.g. each risk must have a cause, an
event and an effect].
(4) Do not include names of [PATIENTS, CUSTOMERS OR STAFF].
(5) For every item, give the source sentence.
Output: [TABLE WITH NAMED COLUMNS, OR JSON WITH THE
FIELDS BELOW]
[FIELD LIST, e.g. id, cause, event, effect,
early_warning, source]
```


**Checks:** Test the system prompt on a small set of documents whose correct output you already know, and keep the results as a regression test for future versions. Read the sources it cites. Add what it could not see. Retest after any change to the prompt or the tool.


## A.4.14 Socratic review prompting (Chapter 14)

**Purpose:** Socratic review prompting asks the model to act as an examiner or tutor that asks you questions one at a time and probes your answers, rather than explaining the material. It suits revision and preparation for examinations, interviews and certification, because retrieving and applying knowledge builds understanding better than rereading.

**Use it when** you have studied a topic and want to test yourself. **Avoid it when** you are learning a topic for the first time, because you cannot yet tell when the examiner's marking is wrong.


**Template:**

```text
Act as a demanding but fair examiner for [COURSE OR
CERTIFICATION]. Ask me one question at a time about
[TOPICS], using realistic [TYPE OF PROJECT] scenarios.
Combine topics in at least two questions.
Wait for my answer. Then: (1) say what was correct;
(2) point out any error or gap, without giving the full
answer; (3) ask a follow-up question that tests the gap.
When you mark an answer correct, show the calculation or
reasoning you checked it against.
After [NUMBER] questions, summarise my weak points and
set [NUMBER] practice problems.
Do not give answers unless I ask.
```


**Checks:** Check every answer the model marks correct against the worked examples in the book. Ask for the reasoning behind each mark. Finish each session by attempting end-of-chapter problems without help.
