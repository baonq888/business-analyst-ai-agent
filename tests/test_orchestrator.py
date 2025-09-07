import asyncio
from src.agents.orchestrator import OrchestratorAgent


def test_run_flow_stub():
    orch = OrchestratorAgent()
    result = asyncio.get_event_loop().run_until_complete(orch.run_full_flow([{"q":"hello"}]))
    assert "structured" in result
    assert "plan" in result
