from app.parser.brd_parser import parse_brd
from app.registry.registry_loader import load_registry
from app.engine.config_generator import generate_config
from app.simulation.simulator import simulate_integration

with open("data/sample_brd.txt") as f:
    brd = f.read()

parsed = parse_brd(brd)
registry = load_registry()
config = generate_config(parsed, registry)

results = simulate_integration(config)

# print("\nSimulation Results:\n")
# for r in results:
#     print(r)
print("\nSimulation Results:\n")

print("Overall Status:", results["overall_status"])

print("\nDetails:\n")
for r in results["results"]:
    print(r)