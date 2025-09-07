from pydantic import BaseSettings

class Settings(BaseSettings):
    openai_api_key: str | None = None
    neo4j_uri: str | None = None
    neo4j_user: str | None = None
    neo4j_password: str | None = None
    pinecone_api_key: str | None = None
    pinecone_env: str | None = None

    class Config:
        env_file = ".env"

settings = Settings()
