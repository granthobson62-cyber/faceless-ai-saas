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
from fastapi import FastAPI
import os


@app.get("/env-test")
def env_test():
    return {
        "WASABI_ACCESS_KEY": os.getenv("WASABI_ACCESS_KEY"),
        "WASABI_BUCKET": os.getenv("WASABI_BUCKET")

    }
