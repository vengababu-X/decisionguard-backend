from fastapi import FastAPI
from app.database import engine
from app.models import Base
from app.routes import router as decision_router
from app.dashboard import router as dashboard_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="DecisionGuard")

app.include_router(decision_router)
app.include_router(dashboard_router)
