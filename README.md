# Automated Resume Screening Tool

## Overview

The Automated Resume Screening Tool is an AI/NLP-powered ATS (Applicant Tracking System) simulator built using Python and Machine Learning techniques.

This project automatically:
- extracts resume content
- analyzes candidate skills
- compares resumes with job descriptions
- calculates resume match scores
- ranks candidates
- generates recruiter-friendly reports

The system simulates how modern HR Tech and ATS platforms shortlist candidates automatically.

---

# Industry Relevance

Recruiters and HR teams receive hundreds of resumes for a single job role.

Manual screening is:
- time-consuming
- repetitive
- error-prone

This project demonstrates how Artificial Intelligence and NLP can automate candidate screening using:
- keyword extraction
- TF-IDF vectorization
- cosine similarity
- automated scoring systems

---

# Features

- PDF Resume Parsing
- DOCX Resume Parsing
- TXT Resume Support
- Job Description Matching
- Skill Extraction
- TF-IDF Vectorization
- Cosine Similarity Matching
- ATS-style Resume Scoring
- Candidate Ranking
- Shortlist/Rejection Decision
- Missing Skill Detection
- CSV Report Generation
- Top Candidate Selection

---

# Project Workflow

```text
Resume Upload
      ↓
Text Extraction
      ↓
Text Cleaning
      ↓
Skill Extraction
      ↓
TF-IDF Vectorization
      ↓
Cosine Similarity Matching
      ↓
Resume Scoring
      ↓
Candidate Ranking
      ↓
CSV Report Generation
```

---

# Tech Stack

## Programming Language
- Python

## Libraries Used
- pandas
- scikit-learn
- pdfplumber
- python-docx
- numpy
- re (Regex)

## Machine Learning Concepts
- NLP
- TF-IDF
- Cosine Similarity
- Text Preprocessing

---

# Folder Structure

```text
Automated-Resume-Screening-Tool/
│
├── data/
│   └── job_description.txt
│
├── resume/
│   ├── resume1.txt
│   ├── resume2.pdf
│
├── outputs/
│   └── ranked_resumes.csv
│
├── images/
│   ├── terminal_output.png
│   ├── csv_output.png
│
├── src/
│
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

# Installation Guide

## Step 1 — Clone Repository

```bash
git clone https://github.com/yourusername/Automated-Resume-Screening-Tool.git
```

---

## Step 2 — Open Project Folder

```bash
cd Automated-Resume-Screening-Tool
```

---

## Step 3 — Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Mac/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## Step 4 — Install Dependencies

```bash
pip install -r requirements.txt
```

---

# requirements.txt

```txt
pandas
numpy
scikit-learn
pdfplumber
python-docx
```

---

# How To Run

```bash
python main.py
```

---

# Sample Job Description

```txt
We are looking for a Python Developer with experience in:
- Python
- SQL
- Machine Learning
- Pandas
- NumPy
- AWS
```

---

# Expected Output

```text
========== Resume Screening Results ==========

Resume         Final Score     Decision
resume1.txt       82.5         Highly Recommended
resume2.pdf       65.2         Shortlisted
resume3.docx      34.7         Rejected
```

---

# CSV Output

Generated file:

```text
outputs/ranked_resumes.csv
```

Contains:
- Resume Name
- TF-IDF Score
- Skill Bonus
- Experience Bonus
- Final Score
- Matched Skills
- Missing Skills
- Decision

---

# Screenshots

## Project Structure
Add screenshot here.

## Terminal Output
Add screenshot here.

## CSV Output
Add screenshot here.

## GitHub Repository
Add screenshot here.

---

# Future Improvements

- Streamlit Dashboard
- FastAPI Backend
- Next.js Frontend
- BERT Embeddings
- Named Entity Recognition (NER)
- Recruiter Analytics Dashboard
- Real-time Resume Upload
- Cloud Deployment

---

# Learning Outcomes

This project helped in learning:
- Python Automation
- NLP Basics
- Resume Parsing
- Machine Learning
- ATS Workflow
- Data Processing
- GitHub Project Management
- Real-world Problem Solving

---

# Interview Questions Covered

- What is TF-IDF?
- What is cosine similarity?
- How does ATS work?
- How are resumes ranked?
- How does NLP help in resume screening?

---

# Use Cases

- HR Tech
- ATS Platforms
- Resume Ranking Systems
- Recruitment Automation
- Candidate Filtering
- AI Hiring Platforms

---

# Author

Bablu kumar

---

# License

This project is for educational and portfolio purposes.