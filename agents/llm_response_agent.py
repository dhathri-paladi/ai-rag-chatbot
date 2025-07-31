# agents/llm_response_agent.py

class LLMResponseAgent:
    def run(self, query_msg):
        document_chunk = query_msg["payload"]["answer_chunk"]
        user_query = query_msg["payload"]["query"]

        # Simulated LLM response
        response = f"📖 Based on the document: \"{document_chunk}\"\n\n💡 Answer to your question \"{user_query}\" is summarized above."

        return {
            "sender": "LLMResponseAgent",
            "receiver": "User",
            "type": "FINAL_ANSWER",
            "trace_id": query_msg["trace_id"],
            "payload": {
                "user_query": user_query,
                "llm_answer": response
            }
        }
