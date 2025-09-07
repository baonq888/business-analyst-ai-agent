# **Business Analyst AI Agent**

Business Analyst AI agent that interviews stakeholders, gathers requirements, validates them against domain knowledge, and generates project plans and documentation automatically.


## **Overview**

The goal of this system is to automate the **early stages of software project planning**:
- **Interview stakeholders** to capture objectives, scope, and constraints.
- **Leverage domain knowledge** (Neo4j knowledge graph) to ensure feasibility and reuse.
- **Validate requirements** for conflicts and compliance.
- **Generate project plans** with milestones and dependencies.
- **Write structured documentation** to Google Docs for stakeholders.


## **Tech Stack**

| Component            | Purpose |
|----------------------|---------|
| **FastAPI**          | REST API for chat endpoints and orchestration |
| **LangChain**        | Agent orchestration and tool integration |
| **Gemini 2.5 Flash** | Core LLM for conversation and reasoning |
| **Neo4j**            | Knowledge graph for domain-specific entities, rules, and relationships |
| **Pinecone**         | Vector database for storing and retrieving past conversations and documents |
| **Google Docs API**  | Create and update stakeholder-facing documentation |
| **Google Drive API** | Manage project-related files and documents |


## **Agents**

The system is composed of multiple specialized agents working together:

| Agent | Purpose |
|-------|---------|
| **Stakeholder Interview Agent** | Chats with stakeholders to gather requirements and scope, using guided questions. |
| **Domain Knowledge Agent** | Retrieves relevant facts from Neo4j to ground the conversation in domain context. |
| **Validation & Compliance Agent** | Checks for conflicts, feasibility, and compliance issues. |
| **Project Planning Agent** | Generates timelines, milestones, and deliverables from validated requirements. |
| **Document Writer Agent** | Creates and updates Google Docs with finalized requirements and project plans. |
| **Vector Retrieval Agent** | Finds similar past projects or documents using Pinecone. |
| **Orchestrator Agent** | Supervises all agents, ensuring outputs flow in the correct sequence. |



## **Core Flow**

# business-analyst-ai-agent
