# AI Doc Chat

AI Doc Chat is a Streamlit-based application that enables users to upload PDF, DOCX, and TXT documents and interact with them using natural language. Powered by advanced AI models, it allows real-time question-answering and summarization of document content.

---

##  Features

- Upload and parse PDF, DOCX, and TXT files
-  Ask questions about the uploaded document
-  Get AI-generated answers using context-aware document understanding
-  Summarize lengthy documents instantly
-  Easy-to-use Streamlit web interface

---

##  File Structure
ai-doc-chat/
├── app.py # Main Streamlit app file
├── requirements.txt # Required Python packages
├── utils.py # Utility functions for parsing and processing
├── README.md # Project documentation
└── .gitignore


---

##  Installation

### 1. Clone the repository

git clone https://github.com/harshaPoojary/ai-doc-chat.git
cd ai-doc-chat

2. Create a virtual environment (optional but recommended)
bash
Copy
Edit
python -m venv venv
source venv/bin/activate        # On macOS/Linux
venv\Scripts\activate           # On Windows
3. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt

 How to Run the App
bash
Copy
Edit
streamlit run app.py
Then open the displayed localhost URL in your browser.

Technologies Used
Python 3.10+

Streamlit

Langchain / Transformers

PyMuPDF, python-docx, etc. for document parsing

OpenAI / Hugging Face Models (optional for QA)

 Example Use Cases
Students extracting answers from textbooks

Lawyers querying legal documents

Researchers analyzing scientific papers

HR reading resumes and policies


 Deployment Options
 Streamlit Cloud

 Hugging Face Spaces

 Heroku or Render

Author
Harsha Poojary
GitHub |

License
This project is licensed under the MIT License.

