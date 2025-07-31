import chromadb
from sentence_transformers import SentenceTransformer

class RetrievalAgent:
    def __init__(self):
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        self.client = chromadb.Client()
        self.collection = self.client.get_or_create_collection(name="documents")

    def run(self, message):
        print("[RetrievalAgent] Received message from IngestionAgent")
        document_text = message['payload']['document_text']
        
        chunks = self.split_into_chunks(document_text)

        for i, chunk in enumerate(chunks):
            embedding = self.model.encode(chunk).tolist()
            self.collection.add(
                documents=[chunk],
                embeddings=[embedding],
                ids=[f"chunk-{i}"]
            )

        return {
            "sender": "RetrievalAgent",
            "receiver": "QueryAgent",
            "type": "DOCUMENT_EMBEDDED",
            "trace_id": message["trace_id"],
            "payload": {
                "num_chunks": len(chunks)
            }
        }

    def split_into_chunks(self, text, max_chunk_size=300):
        lines = text.split("\n")
        chunks = []
        current_chunk = ""
        for line in lines:
            if len(current_chunk) + len(line) <= max_chunk_size:
                current_chunk += line + " "
            else:
                chunks.append(current_chunk.strip())
                current_chunk = line + " "
        if current_chunk:
            chunks.append(current_chunk.strip())
        return chunks
