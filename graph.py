edges = [
    ("A", "B", 2),
    ("B", "C", 3),
    ("C", "D", 1),
    ("D", "A", 4),
]
total_cost = 0
for _, _, cost in edges:
    total_cost += cost
print(f"\nTotal cost of all edges: {total_cost}")
