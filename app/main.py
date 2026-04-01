from fastapi import FastAPI
from pydantic import BaseModel

from app.parser.brd_parser import parse_brd
from app.registry.registry_loader import load_registry
from app.engine.config_generator import generate_config
from app.simulation.simulator import simulate_integration

app = FastAPI(title="AI Integration Orchestrator")


# Request schema
class BRDRequest(BaseModel):
    brd_text: str


# Load registry once
registry = load_registry()


# 🔹 1. Parse BRD
@app.post("/parse-brd")
def parse_brd_api(request: BRDRequest):
    parsed = parse_brd(request.brd_text)
    return {"parsed": parsed}


# 🔹 2. Generate Config
@app.post("/generate-config")
def generate_config_api(request: BRDRequest):
    parsed = parse_brd(request.brd_text)
    config = generate_config(parsed, registry)
    return {"config": config}


# 🔹 3. Full Pipeline (BEST ENDPOINT)
@app.post("/simulate")
def simulate_api(request: BRDRequest):
    parsed = parse_brd(request.brd_text)
    config = generate_config(parsed, registry)
    results = simulate_integration(config)

    return {
        "parsed": parsed,
        "config": config,
        "simulation": results
    }