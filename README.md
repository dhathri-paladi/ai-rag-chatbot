# AI RAG Chatbot

A smart chatbot that can read and understand different types of documents (**PDF, DOCX, PPTX, CSV, TXT**) and answer questions using **RAG (Retrieval-Augmented Generation)** principles.

This project uses:
- Python Agents (Ingestion, Retrieval, Query, LLM)
- HuggingFace Embeddings (via `sentence-transformers`)
- Mock LLM to simulate response generation
- Supports multiple file formats

---

## Features

- Multi-document support: PDF, DOCX, PPTX, CSV, TXT
- Agent-based architecture using message passing
- Vector embeddings using HuggingFace
- MockLLM included (no API key needed)
- Simple CLI-based interaction
- Modular design for easy extension

---

## Project Folder Structure

ai-rag-chatbot/
│
├── agents/
│ ├── ingestion_agent.py
│ ├── retrieval_agent.py
│ ├── query_agent.py
│ └── llm_response_agent.py
│
├── utils/
│ └── file_parser.py
│
├── data/
│ ├── sample.pdf
│ ├── sample.docx
│ ├── sample.pptx
│ ├── sample.csv
│ └── sample.txt
│
├── main.py
├── requirements.txt
└── README.md


---

## How to Run This Project

### 1. Clone the Repository

git clone https://github.com/your-username/ai-rag-chatbot.git
cd ai-rag-chatbot

### 2. Create Virtual Environment

python -m venv venv


### 3. Activate Virtual Environment

On Windows:
venv\Scripts\activate

On Mac/Linux:
source venv/bin/activate


### 4. Install Requirements

pip install -r requirements.txt

### 5. Run the App

python main.py

---

## Sample Output

===============================
Processing file: data/sample.pdf
[IngestionAgent] Reading file: data/sample.pdf
[RetrievalAgent] Received message from IngestionAgent
[QueryAgent] Received user query

Final LLM Answer:
Based on the document: "Quarter 1 KPIs Report Revenue increased by 20% from last quarter. Customer retention rate was 87%..."
Answer to your question "What is the customer retention rate?" is summarized above.

---

## Notes

This project uses **MockLLM** to avoid OpenAI or API integration since it’s for demo/evaluation purposes.  
You can easily switch to OpenAI or other providers by updating the `llm_response_agent.py` agent.

---

## Tech Stack

- Python 3.10+
- sentence-transformers
- PyMuPDF
- python-docx
- python-pptx
- pandas
- torch

---

## Author

**Sree Gnyana Dhathri Paladi**

- GitHub: [dhathri-paladi](https://github.com/dhathri-paladi)  
- LinkedIn: [paladisreegnyanadhathri09](https://www.linkedin.com/in/paladisreegnyanadhathri09/)
      