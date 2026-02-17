# Filter by value
d = {'a': 10, 'b': 5, 'c': 20}
filtered = {k: v for k, v in d.items() if v > 10}
print("Filtered:", filtered)
