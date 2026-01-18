from fastapi import FastAPI
from backend.orchestrator import run_orchestrator

app = FastAPI()

@app.get("/")
def health():
    return {"status": "backend alive"}

@app.post("/run-orchestrator")
def run_ai_endpoint(languages: list | None = None):
    return {"uploaded": run_orchestrator(languages)}
