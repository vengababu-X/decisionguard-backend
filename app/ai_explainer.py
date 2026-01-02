from openai import OpenAI
from config import OPENAI_API_KEY, OPENAI_MODEL

client = OpenAI(api_key=OPENAI_API_KEY)

def explain(decision_id, regret, risk, recent_states):
    prompt = f"""
Decision ID: {decision_id}
Risk Level: {risk}
Regret Value: {regret}
Recent History: {recent_states}

Explain clearly:
- Why risk increased
- What changed compared to alternatives
- What operators should watch next
"""

    response = client.chat.completions.create(
        model=OPENAI_MODEL,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )

    return response.choices[0].message.content
