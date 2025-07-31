import streamlit as st
from agents.ingestion_agent import IngestionAgent
from agents.retrieval_agent import RetrievalAgent
from agents.query_agent import QueryAgent
from agents.llm_response_agent import LLMResponseAgent

st.title("🧠 AI RAG Chatbot")
st.markdown("Ask questions from your uploaded documents!")

# Upload file
uploaded_file = st.file_uploader("Upload a file", type=["pdf", "docx", "txt", "csv", "pptx"])

query = st.text_input("Enter your question")

if st.button("Ask") and uploaded_file and query:
    # Save uploaded file temporarily
    with open(f"data/{uploaded_file.name}", "wb") as f:
        f.write(uploaded_file.read())
    file_path = f"data/{uploaded_file.name}"

    # Step 1: Ingest the file
    ingestion_agent = IngestionAgent(file_path)
    ingested_msg = ingestion_agent.run()

    # Step 2: Embed the document
    retrieval_agent = RetrievalAgent()
    retrieval_msg = retrieval_agent.run(ingested_msg)

    # Step 3: Create query message
    query_msg = {
        "sender": "User",
        "receiver": "QueryAgent",
        "type": "QUERY",
        "trace_id": retrieval_msg["trace_id"],
        "payload": {
            "user_query": query
        }
    }

    # Step 4: Get matching chunk
    query_agent = QueryAgent()
    response_msg = query_agent.run(query_msg)

    # Step 5: Simulate LLM Answer
    llm_agent = LLMResponseAgent()
    final_msg = llm_agent.run(response_msg)

    st.success("Answer:")
    st.write(final_msg["payload"]["llm_answer"])
