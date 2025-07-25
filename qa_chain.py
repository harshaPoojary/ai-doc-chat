from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

def build_vector_index(documents):
    embeddings = OpenAIEmbeddings()
    return FAISS.from_documents(documents, embeddings)

def ask_question(vector_index, question):
    docs = vector_index.similarity_search(question)
    llm = OpenAI(temperature=0.3)
    chain = load_qa_chain(llm, chain_type="stuff")
    return chain.run(input_documents=docs, question=question)
