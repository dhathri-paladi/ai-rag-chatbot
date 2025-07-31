from utils.file_parser import parse_file

class IngestionAgent:
    def __init__(self, file_path):
        self.file_path = file_path
        self.cleaned_text = None

    def run(self):
        print("[IngestionAgent] Reading file:", self.file_path)
        raw_text = parse_file(self.file_path)

        # Clean text: remove empty lines and extra spaces
        self.cleaned_text = self.clean_text(raw_text)

        # Return as MCP-style message
        return {
            "sender": "IngestionAgent",
            "receiver": "RetrievalAgent",
            "type": "DOCUMENT_INGESTED",
            "trace_id": "trace-001",
            "payload": {
                "document_text": self.cleaned_text
            }
        }

    def clean_text(self, text):
        lines = [line.strip() for line in text.splitlines() if line.strip()]
        return "\n".join(lines)
