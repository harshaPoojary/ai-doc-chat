import streamlit as st
from utils import load_and_split_pdf
from qa_chain import build_vector_index, ask_question
import os
from dotenv import load_dotenv

load_dotenv()
st.set_page_config(page_title="AI PDF Q&A", layout="wide")
st.title("📄 Ask Your PDFs Anything")

uploaded_files = st.file_uploader("Upload PDF files", type="pdf", accept_multiple_files=True)

if uploaded_files:
    all_docs = []
    for file in uploaded_files:
        filepath = os.path.join("sample_docs", file.name)
        with open(filepath, "wb") as f:
            f.write(file.read())
        all_docs.extend(load_and_split_pdf(filepath))
    
    vector_index = build_vector_index(all_docs)
    st.success(f"{len(uploaded_files)} document(s) loaded successfully.")

    question = st.text_input("Enter your question:")

    if question:
        with st.spinner("Thinking..."):
            answer = ask_question(vector_index, question)
            st.markdown("**🧠 Answer:**")
            st.write(answer)
