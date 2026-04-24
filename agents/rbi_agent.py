from autogen_agentchat.agents import AssistantAgent
from agents.config import model_client

rbi_agent = AssistantAgent(
    name="RBI_Compliance_Officer",
    system_message="""
You are an RBI AML compliance officer.

Analyze the account risk score and determine if the account
should be flagged under RBI anti-money laundering regulations.
""",
    model_client=model_client
)