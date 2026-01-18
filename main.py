from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def health():
    return {"status": "backend alive"}

@app.post("/run-orchestrator")
def run_orchestrator():
    return {"message": "orchestrator ready"}
