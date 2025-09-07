from neo4j import GraphDatabase
from src.core.config import settings

class Neo4jClient:
    def __init__(self):
        uri = settings.neo4j_uri or "bolt://localhost:7687"
        user = settings.neo4j_user or "neo4j"
        password = settings.neo4j_password or "changeme"
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def run_query(self, cypher: str, params: dict | None = None):
        with self.driver.session() as session:
            result = session.run(cypher, params or {})
            return [record.data() for record in result]
