import streamlit as st
import fitz  # PyMuPDF
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

st.set_page_config(page_title="AI Resume Analyzer", page_icon="📄")
st.title("🤖 AI Resume Analyzer")

# Manual extraction function
def get_text(file):
    with open("temp.pdf", "wb") as f:
        f.write(file.getbuffer())
    doc = fitz.open("temp.pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text

jd = st.text_area("Paste Job Description here...")
uploaded_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])

if st.button("Analyze"):
    if uploaded_file and jd:
        resume_text = get_text(uploaded_file)
        
        # TF-IDF Matching (No Torch/RoBERTa required - No Errors!)
        vectorizer = TfidfVectorizer()
        vectors = vectorizer.fit_transform([resume_text, jd])
        similarity = cosine_similarity(vectors[0:1], vectors[1:2])
        score = round(float(similarity[0][0]) * 100, 2)
        
        st.subheader(f"Matching Score: {score}%")
        st.progress(score/100)
        st.info("Note: Using TF-IDF Vectorization for stable performance on Python 3.14.")
    else:
        st.error("Please provide both Resume and JD.")
