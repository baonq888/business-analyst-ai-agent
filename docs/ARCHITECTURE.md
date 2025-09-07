Business Analyst AI Agent - Architecture

Agents:
1. Stakeholder Interview Agent - conversational interface to capture stakeholder requirements.
2. Domain Knowledge Agent - queries Neo4j and enriches context.
3. Validation Agent - validates completeness/consistency of requirements.
4. Project Planning Agent - converts requirements into project plan and artifacts.
5. Document Writer Agent - creates Google Docs using Google Docs API.
6. Orchestrator Agent - coordinates the end-to-end flow.

Data stores:
- Neo4j: knowledge graph for domain data and past projects.
- Pinecone: vector store for semantic retrieval (embeddings).

LLM:
- LangChain abstraction with Gemini (or configured LLM provider).

Security:
- Use .env for credentials and never commit secrets.
