from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse

from app.database import engine
from app.models import Base
from app.routes import router as decision_router
from app.dashboard import router as dashboard_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="DecisionGuard")

app.include_router(decision_router)
app.include_router(dashboard_router)

# Serve UI at /ui
app.mount("/ui", StaticFiles(directory="app/static", html=True), name="ui")

# Redirect root to UI
@app.get("/")
def root():
    return RedirectResponse(url="/ui")
