# test_parser.py

from app.parser.brd_parser import parse_brd

# Load sample BRD
with open("data/sample_brd.txt", "r") as f:
    brd_text = f.read()

result = parse_brd(brd_text)

print("Parsed Output:\n")
print(result)