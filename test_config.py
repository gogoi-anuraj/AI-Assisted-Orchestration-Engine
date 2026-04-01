from app.parser.brd_parser import parse_brd
from app.registry.registry_loader import load_registry
from app.engine.config_generator import generate_config

with open("data/sample_brd.txt") as f:
    brd = f.read()

parsed = parse_brd(brd)
registry = load_registry()

config = generate_config(parsed, registry)

print("\nGenerated Config:\n")
print(config)