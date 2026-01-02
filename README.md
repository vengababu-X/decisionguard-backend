# DecisionGuard

DecisionGuard is a decision monitoring system that detects early
when a chosen decision is becoming risky under changing conditions.

The system computes decision regret mathematically and uses OpenAI
only to explain risk in clear business language.

## Use Cases
- Logistics route monitoring
- Factory scheduling
- Cloud workload placement

## Run
```bash
export OPENAI_API_KEY=your_key
uvicorn app.main:app --reload
