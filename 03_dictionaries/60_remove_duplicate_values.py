# Remove duplicate values
d = {'a': 1, 'b': 2, 'c': 1}
seen = set()
result = {}

for k, v in d.items():
    if v not in seen:
        result[k] = v
        seen.add(v)

print("Result:", result)
