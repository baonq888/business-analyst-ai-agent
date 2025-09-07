class DocumentWriterAgent:
    """Creates and updates Google Docs from structured content."""

    def __init__(self, docs_client=None):
        self.docs = docs_client

    def create_project_doc(self, title: str, content: str) -> dict:
        # Placeholder: build Google Docs requests from content
        if not self.docs:
            return {"error": "no docs client"}
        return self.docs.create_doc(title)
