from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Decision, DecisionUpdate
from app.schemas import DecisionCreate, DecisionUpdatePayload
from app.ai_explainer import explain
from app.auth import authenticate

router = APIRouter()


@router.post("/decision/create")
def create_decision(
    payload: DecisionCreate,
    db: Session = Depends(get_db),
    _=Depends(authenticate)
):
    if db.query(Decision).filter_by(decision_id=payload.decision_id).first():
        raise HTTPException(status_code=400, detail="Decision exists")

    decision = Decision(
        decision_id=payload.decision_id,
        company_id=payload.company_id
    )

    db.add(decision)
    db.commit()

    return {"decision_id": payload.decision_id}


@router.post("/decision/{decision_id}/update")
def update_decision(
    decision_id: str,
    payload: DecisionUpdatePayload,
    db: Session = Depends(get_db),
    _=Depends(authenticate)
):
    decision = db.query(Decision).filter_by(decision_id=decision_id).first()
    if not decision:
        raise HTTPException(status_code=404, detail="Decision not found")

    best = min(payload.alternatives)
    regret = payload.chosen_cost - best

    risk = "LOW" if regret <= 3 else "MEDIUM" if regret <= 8 else "CRITICAL"

    explanation = explain(decision_id, regret, risk, payload.alternatives)

    update = DecisionUpdate(
        decision_id=decision_id,
        chosen_cost=payload.chosen_cost,
        alternatives=payload.alternatives,
        regret=regret,
        risk=risk,
        explanation=explanation
    )

    db.add(update)
    db.commit()

    return {
        "decision_id": decision_id,
        "regret": regret,
        "risk": risk,
        "explanation": explanation
    }


@router.get("/decision/{decision_id}/history")
def decision_history(
    decision_id: str,
    db: Session = Depends(get_db),
    _=Depends(authenticate)
):
    return db.query(DecisionUpdate)\
        .filter_by(decision_id=decision_id)\
        .order_by(DecisionUpdate.created_at.asc())\
        .all()
