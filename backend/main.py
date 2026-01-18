from fastapi import FastAPI
from orchestrator import run_orchestrator

app = FastAPI()

@app.post("/run-orchestrator")
def run_ai_endpoint(languages: list = None):
    """
    Trigger the AI Orchestrator to generate videos and upload to Wasabi.
    Optional: list of language codes
    """
    uploaded_urls = run_orchestrator(languages)
    return {"uploaded": uploaded_urls}




    
