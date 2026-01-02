import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

def explain(decision_id, regret, risk, recent_states):
    try:
        prompt = f"""
Decision ID: {decision_id}
Risk: {risk}
Regret: {regret}
Alternatives: {recent_states}

Explain the decision risk clearly.
"""
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3,
            timeout=10
        )
        return response.choices[0].message.content
    except Exception:
        return "AI explanation unavailable"
