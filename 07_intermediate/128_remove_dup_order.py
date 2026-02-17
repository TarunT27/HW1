# Remove duplicates preserving order
lst = [1, 2, 2, 3, 1, 4]
seen = set()
result = []

for item in lst:
    if item not in seen:
        seen.add(item)
        result.append(item)

print(result)
