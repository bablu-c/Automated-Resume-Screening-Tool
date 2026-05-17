import os
import re
import pandas as pd
import pdfplumber
from docx import Document

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# ==========================================
# LOAD JOB DESCRIPTION
# ==========================================

with open("data/job_description.txt", "r", encoding="utf-8") as file:
    job_description = file.read()

# ==========================================
# SKILLS DATABASE
# ==========================================

skills = [
    "python",
    "sql",
    "machine learning",
    "data analysis",
    "excel",
    "power bi",
    "aws",
    "django",
    "flask",
    "numpy",
    "pandas",
    "scikit-learn",
    "tensorflow",
    "deep learning",
    "react",
    "nodejs",
    "mongodb",
    "git",
    "linux"
]

# ==========================================
# PDF TEXT EXTRACTION
# ==========================================

def extract_pdf_text(pdf_path):
    text = ""

    try:
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:

                extracted = page.extract_text()

                if extracted:
                    text += extracted + "\n"

    except Exception as e:
        print(f"Error reading PDF {pdf_path}: {e}")

    return text

# ==========================================
# DOCX TEXT EXTRACTION
# ==========================================

def extract_docx_text(docx_path):

    text = ""

    try:
        doc = Document(docx_path)

        for para in doc.paragraphs:
            text += para.text + "\n"

    except Exception as e:
        print(f"Error reading DOCX {docx_path}: {e}")

    return text

# ==========================================
# TEXT CLEANING
# ==========================================

def clean_text(text):

    text = text.lower()

    text = re.sub(r"[^a-zA-Z0-9 ]", " ", text)

    text = re.sub(r"\s+", " ", text)

    return text.strip()

# ==========================================
# SKILL EXTRACTION
# ==========================================

def extract_skills(text):

    found_skills = []

    for skill in skills:

        if skill.lower() in text.lower():

            found_skills.append(skill)

    return list(set(found_skills))

# ==========================================
# EXPERIENCE EXTRACTION
# ==========================================

def extract_experience(text):

    experience = re.findall(r"(\d+)\s+years", text.lower())

    if experience:
        return max([int(exp) for exp in experience])

    return 0

# ==========================================
# RESUME FOLDER
# ==========================================

resume_folder = "resume"

resume_data = []

# ==========================================
# CHECK RESUME FOLDER
# ==========================================

if not os.path.exists(resume_folder):

    print("Resume folder not found.")
    exit()

files = os.listdir(resume_folder)

if len(files) == 0:

    print("No resume files found.")
    exit()

# ==========================================
# PROCESS RESUMES
# ==========================================

for file in files:

    file_path = os.path.join(resume_folder, file)

    text = ""

    # --------------------------------------
    # READ FILES
    # --------------------------------------

    if file.endswith(".pdf"):

        text = extract_pdf_text(file_path)

    elif file.endswith(".docx"):

        text = extract_docx_text(file_path)

    elif file.endswith(".txt"):

        with open(file_path, "r", encoding="utf-8") as f:
            text = f.read()

    else:
        continue

    # --------------------------------------
    # CLEAN TEXT
    # --------------------------------------

    cleaned_resume = clean_text(text)

    cleaned_jd = clean_text(job_description)

    # --------------------------------------
    # SKILLS
    # --------------------------------------

    extracted_skills = extract_skills(cleaned_resume)

    matched_skills = len(extracted_skills)

    # --------------------------------------
    # EXPERIENCE
    # --------------------------------------

    experience_years = extract_experience(cleaned_resume)

    # --------------------------------------
    # TF-IDF SIMILARITY
    # --------------------------------------

    documents = [cleaned_jd, cleaned_resume]

    tfidf = TfidfVectorizer()

    matrix = tfidf.fit_transform(documents)

    similarity_score = cosine_similarity(
        matrix[0:1],
        matrix[1:2]
    )[0][0]

    similarity_percentage = round(similarity_score * 100, 2)

    # ======================================
    # BONUS SCORING SYSTEM
    # ======================================

    skill_bonus = matched_skills * 5

    experience_bonus = experience_years * 2

    final_score = similarity_percentage + skill_bonus + experience_bonus

    if final_score > 100:
        final_score = 100

    final_score = round(final_score, 2)

    # ======================================
    # SHORTLIST DECISION
    # ======================================

    if final_score >= 60:
        decision = "Highly Recommended"

    elif final_score >= 40:
        decision = "Shortlisted"

    else:
        decision = "Rejected"

    # ======================================
    # MISSING SKILLS
    # ======================================

    missing_skills = []

    for skill in skills:

        if skill not in extracted_skills:
            missing_skills.append(skill)

    # ======================================
    # SAVE DATA
    # ======================================

    resume_data.append({
        "Resume": file,
        "TF-IDF Score": similarity_percentage,
        "Skill Bonus": skill_bonus,
        "Experience Bonus": experience_bonus,
        "Final Score": final_score,
        "Experience (Years)": experience_years,
        "Matched Skills": ", ".join(extracted_skills),
        "Missing Skills": ", ".join(missing_skills[:5]),
        "Decision": decision
    })

# ==========================================
# CREATE DATAFRAME
# ==========================================

if len(resume_data) == 0:

    print("No valid resumes processed.")
    exit()

df = pd.DataFrame(resume_data)

# ==========================================
# SORT BY FINAL SCORE
# ==========================================

df = df.sort_values(by="Final Score", ascending=False)

# ==========================================
# CREATE OUTPUT FOLDER
# ==========================================

os.makedirs("outputs", exist_ok=True)

# ==========================================
# SAVE CSV REPORT
# ==========================================

output_path = "outputs/ranked_resumes.csv"

df.to_csv(output_path, index=False)

# ==========================================
# DISPLAY RESULTS
# ==========================================

print("\n========== Resume Screening Results ==========\n")

print(df)

print(f"\nCSV report saved at: {output_path}")

# ==========================================
# TOP CANDIDATE
# ==========================================

top_candidate = df.iloc[0]

print("\n========== Top Candidate ==========\n")

print(f"Resume: {top_candidate['Resume']}")

print(f"Final Score: {top_candidate['Final Score']}")

print(f"Decision: {top_candidate['Decision']}")

print(f"Skills: {top_candidate['Matched Skills']}")