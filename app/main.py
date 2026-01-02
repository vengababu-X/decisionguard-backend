from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse

from app.routes import router

app = FastAPI(
    title="DecisionGuard v3",
    version="0.1.0"
)

# API routes
app.include_router(router)

# Serve UI
app.mount("/ui", StaticFiles(directory="app/static", html=True), name="ui")

# Redirect root to UI
@app.get("/")
def root():
    return RedirectResponse(url="/ui")
