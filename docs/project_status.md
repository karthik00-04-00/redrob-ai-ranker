# REDROB AI RANKER — PROJECT STATUS

## Project

India Runs 2026 – Data & AI Challenge

Goal:
Build a recruiter-style AI ranking system that ranks candidates for a Senior AI Engineer role.

---

## Repository Structure

redrob-ai-ranker/

data/
├── raw/
├── processed/

docs/
├── project_status.md

notebooks/

outputs/

src/
├── **init**.py
├── preprocess.py
├── feature_engineering.py
├── scoring.py
├── embedding_ranker.py
├── generate_submission.py

main.py
requirements.txt

---

## Environment

Virtual Environment:

.venv

Installed Packages:

* pandas
* numpy
* scikit-learn
* sentence-transformers
* torch
* tqdm
* pyarrow
* openpyxl
* python-docx

Rule:

Use:

python -m ...

instead of directly executing files from src.

Examples:

python -m src.feature_engineering

---

## Dataset

Verified:

TOTAL_RECORDS = 100000

Dataset File:

data/raw/candidates.jsonl

Schema:

candidate_id
profile
career_history
education
skills
certifications
languages
redrob_signals

---

## Major Dataset Discovery

The dataset is intentionally noisy.

Examples observed:

* Marketing Manager with Mechanical Engineering experience
* Customer Support with Business Analyst experience
* Accountant with Apache Flink skills
* Backend Engineer with strong AI skills but mostly Data Engineering experience

Conclusion:

Do NOT trust:

* headline
* current_title
* skills

Trust more:

* career_history.description
* career_history.title
* years_of_experience
* redrob_signals

---

## Job Description Findings

File:

job_description.docx

Key Discovery:

The JD explicitly states:

"The right answer is NOT finding candidates whose skills section contains the most AI keywords."

The challenge intentionally contains keyword traps.

---

## What The JD Actually Wants

Strong Signals:

* ranking systems
* retrieval systems
* recommendation systems
* embeddings
* vector databases
* hybrid search
* evaluation frameworks
* NDCG
* MRR
* MAP
* production ML systems

Weak Signals:

* AI buzzwords
* generic LLM projects
* keyword stuffing

---

## Behavioral Signal Discovery

File:

redrob_signals_doc.docx

Key Discovery:

Behavioral signals should modify ranking.

Examples:

* recruiter_response_rate
* interview_completion_rate
* saved_by_recruiters_30d
* search_appearance_30d
* profile_completeness_score
* github_activity_score
* last_active_date

JD explicitly says inactive candidates should be down-weighted.

---

## Implemented Code

### preprocess.py

Purpose:

Convert candidate JSON into recruiter-readable text.

Produces:

candidate_text

---

### feature_engineering.py

Implemented:

get_ai_score(text)

get_retrieval_score(text)

get_mlops_score(text)

Keyword-based baseline only.

---

### scoring.py

Implemented:

calculate_feature_score()

Current baseline:

0.4 * ai_score

* 0.4 * retrieval_score
* 0.2 * mlops_score

Temporary baseline only.

---

### main.py

Working Pipeline:

candidate
→ build_candidate_text()
→ get_ai_score()
→ get_retrieval_score()
→ get_mlops_score()
→ calculate_feature_score()

Observed Output:

AI SCORE: 6
RETRIEVAL SCORE: 1
MLOPS SCORE: 4
FINAL SCORE: 3.6

---

## Current Architecture Hypothesis

Final system should be:

1. Semantic Fit
2. Career Evidence
3. Behavioral Signals
4. Consistency Check
5. Data Quality Check

Not:

* keyword matching
* pure embedding similarity

---

## Immediate Next Tasks

1. Read complete redrob_signals_doc.docx
2. Read candidate_schema.json
3. Design behavior_score
4. Design consistency_score
5. Refactor scoring.py
6. Build embedding_ranker.py
7. Rank first 100 candidates
8. Validate ranking logic
9. Scale to 100000 candidates
10. Generate ranked_candidates.csv

---

## Continuation Prompt

When starting a new chat:

"ACT AS A CONTINUATION ENGINE.

Read the project status below and reply only READY.

[PASTE THIS FILE]

Then continue exactly from the last completed step."
