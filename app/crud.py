from sqlalchemy.orm import Session
from .models import Decision, DecisionState
from .risk import assess_risk
from .ai_explainer import explain

def create_decision(db: Session, data):
    decision = Decision(
        decision_id=data.decision_id,
        company_id=data.company_id
    )
    db.add(decision)
    db.commit()
    db.refresh(decision)
    return decision

def update_decision(db: Session, decision: Decision, chosen, alternatives):
    best_alt = min(alternatives)
    regret = chosen - best_alt
    risk = assess_risk(regret)

    recent = db.query(DecisionState)\
        .filter_by(decision_id=decision.id)\
        .order_by(DecisionState.id.desc())\
        .limit(3).all()

    explanation = None
    if risk != "STABLE":
        explanation = explain(
            decision.decision_id,
            regret,
            risk,
            [r.regret for r in recent]
        )

    state = DecisionState(
        decision_id=decision.id,
        chosen_cost=chosen,
        best_alternative=best_alt,
        regret=regret,
        risk=risk,
        explanation=explanation
    )
    db.add(state)
    db.commit()

    return {
        "regret": regret,
        "risk": risk,
        "explanation": explanation
    }
