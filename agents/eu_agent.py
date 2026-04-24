from autogen_agentchat.agents import AssistantAgent
from agents.config import model_client

eu_agent = AssistantAgent(
    name="EU_Compliance_Officer",
    system_message="""
You are an EU AML compliance officer.

Evaluate the account risk score using EU AML directives.
""",
    model_client=model_client
)