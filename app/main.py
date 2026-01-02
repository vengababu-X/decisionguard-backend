from fastapi import FastAPI
from .database import Base, engine
from .routes import router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="DecisionGuard v3")
app.include_router(router)

@app.get("/health")
def health():
    return {"status": "ok"}
