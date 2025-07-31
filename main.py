from agents.ingestion_agent import IngestionAgent
from agents.retrieval_agent import RetrievalAgent
from agents.query_agent import QueryAgent
from agents.llm_response_agent import LLMResponseAgent

# ✅ List of all files to process
file_paths = [
    "data/sample.pdf",
    "data/sample.docx",
    "data/sample.txt",
    "data/sample.csv",
    "data/sample.pptx"
]

# ✅ Define your test question
query = "What is the customer retention rate?"

# ✅ Process each file one by one
for file_path in file_paths:
    print("\n===============================")
    print(f"📂 Processing file: {file_path}")

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

    print("\n🤖 Final LLM Answer:")
    print(final_msg["payload"]["llm_answer"])
