import pinecone
from src.core.config import settings

class PineconeClient:
    def __init__(self):
        key = settings.pinecone_api_key
        env = settings.pinecone_env
        if key and env:
            pinecone.init(api_key=key, environment=env)
        self.index = None

    def init_index(self, name: str):
        if name in pinecone.list_indexes():
            self.index = pinecone.Index(name)
        else:
            pinecone.create_index(name, dimension=1536)
            self.index = pinecone.Index(name)

    def upsert(self, vectors: list):
        if not self.index:
            raise RuntimeError("Index not initialized")
        return self.index.upsert(vectors)
