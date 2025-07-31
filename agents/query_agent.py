import chromadb
from sentence_transformers import SentenceTransformer

class QueryAgent:
    def __init__(self):
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        self.client = chromadb.Client()
        self.collection = self.client.get_or_create_collection(name="documents")

    def run(self, message):
        print("[QueryAgent] Received user query")
        query = message['payload']['user_query']
        
        # Embed the query
        query_embedding = self.model.encode(query).tolist()
        
        # Search the collection
        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=1
        )

        best_result = results['documents'][0][0] if results['documents'][0] else "No relevant content found."

        return {
            "sender": "QueryAgent",
            "receiver": "User",
            "type": "QUERY_RESULT",
            "trace_id": message["trace_id"],
            "payload": {
                "query": query,
                "answer_chunk": best_result
            }
        }
