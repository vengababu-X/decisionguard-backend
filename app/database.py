from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import DecisionUpdate
from app.auth import authenticate

router = APIRouter()

@router.get("/dashboard/summary")
def dashboard_summary(
    db: Session = Depends(get_db),
    _=Depends(authenticate)
):
    updates = db.query(DecisionUpdate).all()

    critical = sum(1 for u in updates if u.risk == "CRITICAL")
    medium = sum(1 for u in updates if u.risk == "MEDIUM")
    low = sum(1 for u in updates if u.risk == "LOW")

    return {
        "total_updates": len(updates),
        "critical": critical,
        "medium": medium,
        "low": low
    }
