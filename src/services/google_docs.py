from googleapiclient.discovery import build
from src.core.config import settings

class GoogleDocsClient:
    def __init__(self, creds=None):
        # creds: google.oauth2.credentials.Credentials or similar
        self.creds = creds
        if creds:
            self.service = build("docs", "v1", credentials=creds)
        else:
            self.service = None

    def create_doc(self, title: str) -> dict:
        if not self.service:
            raise RuntimeError("Google credentials not configured")
        doc = {"title": title}
        return self.service.documents().create(body=doc).execute()

    def update_doc(self, document_id: str, requests: list):
        if not self.service:
            raise RuntimeError("Google credentials not configured")
        return self.service.documents().batchUpdate(documentId=document_id, body={"requests": requests}).execute()
