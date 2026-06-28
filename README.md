# Redrob AI Ranker

### AI-Powered Candidate Ranking System for Recruiters

## Overview

This project was built for the **INDIA RUNS 2026 – Data & AI Challenge by Redrob AI and Hack2Skill**.

The goal is to build an intelligent candidate ranking system that mimics how recruiters evaluate profiles rather than relying solely on keyword matching.

The system combines:

* Job understanding
* Behavioral signals
* Semantic similarity
* Evidence extraction
* Consistency validation
* Explainable AI

to recommend the most relevant candidates for a job description.

---

# Problem Statement

Given:

* A Job Description (JD)
* 100,000 candidate profiles

Build an AI system capable of ranking candidates similarly to an experienced recruiter.

Challenges:

* Noisy candidate profiles
* Incomplete information
* Sparse signals
* Semantic mismatch between resumes and JDs
* Need for explainable recommendations

---

# Dataset

## Candidate Dataset

* Total Candidates: 100,000
* Fields:

  * Profile
  * Career History
  * Education
  * Skills
  * Certifications
  * Behavioral Signals

## Behavioral Signals Used

* Profile Completeness
* Recruiter Response Rate
* Open To Work Status
* Interview Completion Rate
* Offer Acceptance Rate
* GitHub Activity
* Search Appearance
* Saved By Recruiters
* Notice Period
* Verification Signals

---

# System Architecture

```text
Job Description
        ↓
Job Understanding
        ↓
Job Match Score
        ↓

Candidate Profiles
        ↓
Feature Engineering
        ↓
 ┌────────────┬────────────┬────────────┬────────────┐
 │ Behavior   │ Intent     │ Trust      │ Evidence   │
 └────────────┴────────────┴────────────┴────────────┘
        ↓
Semantic Similarity (Sentence Transformers)
        ↓
Consistency Scoring
        ↓
Hybrid Ranking V2
        ↓
Explainable Recommendations
        ↓
Top Candidate Recommendations
```

---

# Methodology

## 1. Candidate Retrieval

Candidate profiles are converted into rich textual representations containing:

* Headline
* Summary
* Skills
* Career History
* Education

---

## 2. Job Understanding

The job description is analyzed to identify:

* AI expertise
* Retrieval systems experience
* Ranking systems experience
* MLOps capabilities

---

## 3. Feature Engineering

The system computes:

### Relevance Score

Measures AI, retrieval, ranking, and MLOps alignment.

### Behavior Score

Measures recruiter engagement and activity.

### Intent Score

Measures candidate responsiveness and openness.

### Trust Score

Measures profile verification and reliability.

### Evidence Score

Measures production impact and demonstrated achievements.

---

## 4. Semantic Similarity

Implemented using:

* Sentence Transformers
* Embedding-based candidate matching

This allows the system to understand semantic relationships beyond keyword overlap.

---

## 5. Consistency Score

Measures whether the candidate's:

* Skills
* Career history
* Profile claims

are mutually consistent.

This reduces profile inflation and rewards candidates with supporting evidence.

---

## 6. Hybrid Ranking V2

Final ranking combines:

* Recruiter Score
* Job Match Score
* Semantic Similarity
* Consistency Score

to produce the final candidate ranking.

---

# Explainability

For every recommendation, the system generates:

* Reasons for recommendation
* Supporting evidence
* Profile snippets
* Semantic alignment indicators

Example:

Candidate:
CAND_0018499

Reasons:

* Experience building ranking systems
* Experience with embeddings and RAG pipelines
* High semantic similarity

Profile Evidence:

* Built a RAG-based ranking pipeline serving 50M+ queries per month.
* Combined dense retrieval and LLM re-ranking.
* Designed evaluation frameworks using NDCG and MRR.

---

# Results

The final system successfully:

* Ranked 100,000 candidates
* Generated explainable recommendations
* Improved ranking quality using semantic similarity
* Validated consistency-based ranking signals
* Produced recruiter-style candidate justifications

---

# Tech Stack

* Python
* Pandas
* NumPy
* Scikit-learn
* Sentence Transformers
* PyTorch

---

# Repository Structure

```text
data/
docs/
outputs/
src/

main.py
hybrid_ranking.py
compare_rankings.py
generate_explanations.py
requirements.txt
README.md
```

---

# Future Work

* Cross-Encoder Re-ranking
* Learning-to-Rank models
* Feedback-driven ranking optimization
* Online evaluation and active learning
* See docs/future_improvements.md for planned extensions toward a production-grade multi-domain recruitment platform.     
---

# Team

Built for:

INDIA RUNS 2026 – Data & AI Challenge
Redrob AI × Hack2Skill
