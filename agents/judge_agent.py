from autogen_agentchat.agents import AssistantAgent
from agents.config import model_client

judge_agent = AssistantAgent(
    name="Compliance_Judge",
    system_message="""
You are the final compliance judge.

After hearing arguments from RBI and EU officers,
make the final decision.

Possible outcomes:
APPROVE
FLAG_SUSPICIOUS
ESCALATE_INVESTIGATION
""",
    model_client=model_client
)