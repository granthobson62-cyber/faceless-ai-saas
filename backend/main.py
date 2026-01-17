from fastapi import FastAPI
import orchestrator

app = FastAPI()

@app.get("/")
def root():
    return {"status": "Backend alive"}

@app.post("/run-orchestrator")
def run_ai():
    orchestrator.run_orchestrator()
    return {"status": "Orchestrator executed"}
