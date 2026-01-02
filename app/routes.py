from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .database import SessionLocal
from .schemas import DecisionCreate, DecisionUpdate
from .crud import create_decision, update_decision
from .models import Decision
from .auth import verify_key

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/decision/create", dependencies=[Depends(verify_key)])
def create(data: DecisionCreate, db: Session = Depends(get_db)):
    return create_decision(db, data)

@router.post("/decision/{decision_id}/update", dependencies=[Depends(verify_key)])
def update(decision_id: str, data: DecisionUpdate, db: Session = Depends(get_db)):
    decision = db.query(Decision).filter_by(decision_id=decision_id).first()
    if not decision:
        raise HTTPException(status_code=404, detail="Decision not found")
    return update_decision(db, decision, data.chosen_cost, data.alternatives)
