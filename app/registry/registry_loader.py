import json

def load_registry():
    with open("app/registry/adapters.json", "r") as f:
        return json.load(f)