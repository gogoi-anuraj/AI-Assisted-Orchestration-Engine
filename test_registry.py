# from app.registry.registry_loader import load_registry

# registry = load_registry()

# print("Available services:")
# for service in registry:
#     print("-", service)


from app.parser.brd_parser import parse_brd
from app.registry.registry_loader import load_registry

with open("data/sample_brd.txt") as f:
    brd = f.read()

parsed = parse_brd(brd)
registry = load_registry()

print("\nRequested services:")
for s in parsed["services"]:
    print(s["name"], "→", "Available" if s["name"] in registry else "Not found")