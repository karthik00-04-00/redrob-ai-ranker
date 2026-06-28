# System Architecture V2

## High-Level Pipeline

```text
                    ┌──────────────────┐
                    │  Job Description │
                    └────────┬─────────┘
                             │
                             ▼
                  ┌────────────────────┐
                  │  Job Understanding │
                  └────────┬───────────┘
                           │
                           ▼
                  ┌────────────────────┐
                  │   Job Match Score  │
                  └────────┬───────────┘
                           │
                           │
────────────────────────────────────────────────────

                  ┌────────────────────┐
                  │ Candidate Dataset  │
                  │     (100,000)      │
                  └────────┬───────────┘
                           │
                           ▼
                  ┌────────────────────┐
                  │ Profile Processing │
                  └────────┬───────────┘
                           │
                           ▼
                  ┌────────────────────┐
                  │ Feature Engineering│
                  └────────┬───────────┘
                           │
      ┌────────────────────┼────────────────────┐
      │                    │                    │
      ▼                    ▼                    ▼
┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│ Behavior    │    │ Intent      │    │ Trust       │
│ Score        │    │ Score        │    │ Score       │
└─────────────┘    └─────────────┘    └─────────────┘
                           │
                           ▼
                  ┌────────────────────┐
                  │  Evidence Score    │
                  └────────┬───────────┘
                           │
                           ▼
                  ┌────────────────────┐
                  │ Recruiter Score    │
                  └────────┬───────────┘
                           │
                           ▼
                  ┌────────────────────┐
                  │ Sentence Transformer│
                  │ Semantic Similarity │
                  └────────┬───────────┘
                           │
                           ▼
                  ┌────────────────────┐
                  │ Consistency Scorer │
                  │ Skills ↔ Experience│
                  └────────┬───────────┘
                           │
                           ▼
                  ┌────────────────────┐
                  │ Hybrid Ranking V2  │
                  └────────┬───────────┘
                           │
                           ▼
                  ┌────────────────────┐
                  │ Explainability     │
                  │ + Evidence Engine  │
                  └────────┬───────────┘
                           │
                           ▼
                  ┌────────────────────┐
                  │ Top Candidates     │
                  │ Recommendations    │
                  └────────────────────┘
```

---

# Components

## 1. Job Understanding

Extracts:

* AI requirements
* Retrieval requirements
* Ranking requirements
* MLOps requirements

Produces:

* Job Match Score

---

## 2. Feature Engineering

Produces:

* Relevance Score
* Behavior Score
* Intent Score
* Trust Score
* Evidence Score

---

## 3. Semantic Similarity Engine

Model:

* Sentence Transformers

Purpose:

* Capture semantic alignment between candidates and the job description.

---

## 4. Consistency Engine

Measures alignment between:

* Skills
* Profile claims
* Career history

Purpose:

* Penalize inflated profiles.
* Reward evidence-backed experience.

---

## 5. Hybrid Ranking Engine

Final score combines:

* Recruiter Score
* Job Match Score
* Semantic Similarity
* Consistency Score

Produces:

* Final candidate ranking.

---

## 6. Explainability Engine

Generates:

* Recommendation reasons
* Evidence indicators
* Profile snippets
* Recruiter-style justifications
