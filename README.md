# AI Resume Analyzer

An AI-powered Resume Analyzer that evaluates the relevance of a candidate's resume against a given job description using Natural Language Processing (NLP) and text similarity techniques.

## 📌 Project Overview

The AI Resume Analyzer is designed to automate the initial resume screening process.

The system accepts a resume in PDF format, extracts the text from it, preprocesses the extracted content, and compares it with a job description. The text is converted into numerical representations using **TF-IDF (Term Frequency-Inverse Document Frequency)**, and **Cosine Similarity** is used to calculate how closely the resume matches the job requirements.

The system can generate a similarity/match score and use the score to determine the relevance of a resume.

## 🎯 Objective

The main objective of this project is to make the initial resume screening process faster and more structured by automatically comparing resumes with job requirements.

It aims to:

- Reduce manual effort during initial resume screening
- Identify resumes that are more relevant to a job description
- Generate a similarity score between resumes and job requirements
- Provide a consistent approach for resume comparison

## ⚙️ How It Works

The overall workflow of the system is:

1. Resume is provided in PDF format.
2. Text is extracted from the resume.
3. The extracted text is preprocessed.
4. Text preprocessing includes NLP techniques such as:
   - Tokenization
   - Stop-word removal
   - Lemmatization
5. The processed text is converted into numerical vectors using TF-IDF.
6. The resume and job description vectors are compared using Cosine Similarity.
7. A similarity/match score is generated.
8. Resumes can be ranked based on their relevance to the job requirements.

## 🧠 NLP & Machine Learning Techniques

### TF-IDF

TF-IDF is used to represent the textual content numerically by assigning importance to words based on their frequency within the text and across the documents.

### Cosine Similarity

Cosine Similarity is used to measure the similarity between the resume and the job description vectors.

A higher similarity score indicates that the resume contains more relevant terms and information related to the given job description.

## ✨ Features

- PDF resume processing
- Text extraction from resumes
- NLP-based text preprocessing
- Tokenization
- Stop-word removal
- Lemmatization
- TF-IDF feature extraction
- Cosine Similarity based comparison
- Resume match/similarity scoring
- Resume relevance evaluation

## 🛠️ Technologies Used

- Python
- Natural Language Processing (NLP)
- TF-IDF
- Cosine Similarity
- HTML
- Python-based web application components

## 📁 Project Structure

```text
AI-Resume-Analyzer/
│
├── app.py
├── st_app.py
├── utils.py
├── requirements.txt
├── runtime.txt
├── sample_job_description.txt
│
└── templates/
    ├── index.html
    └── result.html
