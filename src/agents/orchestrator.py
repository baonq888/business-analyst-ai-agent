from src.agents.stakeholder_agent import StakeholderInterviewAgent
from src.agents.domain_agent import DomainKnowledgeAgent
from src.agents.validation_agent import ValidationAgent
from src.agents.planning_agent import ProjectPlanningAgent
from src.agents.document_writer import DocumentWriterAgent

class OrchestratorAgent:
    """Coordinates other agents to produce project artifacts."""

    def __init__(self, llm_client=None, neo4j_client=None, docs_client=None):
        self.stakeholder = StakeholderInterviewAgent(llm_client)
        self.domain = DomainKnowledgeAgent(neo4j_client)
        self.validator = ValidationAgent(llm_client)
        self.planner = ProjectPlanningAgent(llm_client)
        self.writer = DocumentWriterAgent(docs_client)

    async def run_full_flow(self, conversation_history: list):
        structured = await self.stakeholder.interview(conversation_history)
        domain = self.domain.query(structured.get("requirements", ""))
        validation = self.validator.validate(structured)
        plan = self.planner.plan(structured if validation.get("valid") else {})
        doc = self.writer.create_project_doc("Project Scope", plan.get("summary", ""))
        return {
            "structured": structured,
            "domain": domain,
            "validation": validation,
            "plan": plan,
            "doc": doc,
        }
