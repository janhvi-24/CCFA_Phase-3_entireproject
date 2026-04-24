from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.conditions import TextMentionTermination

from agents.rbi_agent import rbi_agent
from agents.eu_agent import eu_agent
from agents.judge_agent import judge_agent


async def run_courtroom(account_id, risk_score, rules):

    rules_text = "\n".join(rules)

    task = f"""
Account Under Investigation: {account_id}

Risk Score: {risk_score}

Relevant AML Regulations:
{rules_text}

Debate whether this account should be flagged for money laundering.

Debate Structure:
1. RBI Compliance Officer argues first.
2. EU Compliance Officer responds.
3. Compliance Judge gives FINAL DECISION.

Judge must output one of:
APPROVE
FLAG_SUSPICIOUS
ESCALATE_INVESTIGATION
"""

    termination = TextMentionTermination("Final decision")

    team = RoundRobinGroupChat(
        participants=[
            rbi_agent,
            eu_agent,
            judge_agent
        ],
        termination_condition=termination,
        max_turns=3
    )

    result = await team.run(task=task)

    transcript = []

    for msg in result.messages:
        transcript.append({
            "speaker": msg.source,
            "content": msg.content
        })

    return transcript