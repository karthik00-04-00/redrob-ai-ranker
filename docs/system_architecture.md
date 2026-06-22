# Redrob AI Ranker

## Problem Statement

Traditional candidate screening relies heavily on keyword matching and manual filtering. This approach often ignores behavioral signals, candidate intent, profile quality, and contextual job relevance.

Our objective is to build a job-aware candidate recommendation engine capable of generating ranked shortlists using both structured and unstructured candidate data.

---

## System Architecture

Job Description
→ Job Understanding
→ Job Profile

Candidate Profile
→ Feature Engineering

Feature Groups:

1. Relevance
2. Behavior
3. Intent
4. Trust
5. Evidence

Feature Scores
→ Candidate Score

Job Profile + Candidate Profile
→ Job Match Score

Candidate Score + Job Match Score
→ Recruiter Score

Recruiter Score
→ Ranked Candidate List

---

## Feature Categories

### Relevance

Measures alignment with:

* AI
* Machine Learning
* Retrieval
* Ranking
* Recommendation Systems
* Search Technologies

### Behavior

Measures:

* Recruiter engagement
* GitHub activity
* Profile visibility
* Interview completion

### Intent

Measures:

* Open-to-work status
* Recruiter response rate
* Offer acceptance behavior

### Trust

Measures:

* Profile completeness
* Verification status
* LinkedIn connectivity

### Evidence

Measures demonstrated experience with:

* Production ML systems
* Ranking systems
* Recommendation systems
* Search infrastructure

---

## Ranking Formula

Candidate Score

= 0.35 × Relevance

* 0.25 × Behavior
* 0.20 × Intent
* 0.10 × Trust
* 0.10 × Evidence

Recruiter Score

= 0.70 × Candidate Score
+ 0.30 × Job Match Score

---

## Outputs

The system generates:

* Ranked candidate recommendations
* Submission CSV
* Candidate explanations
* Job-aware rankings
