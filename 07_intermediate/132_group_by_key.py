# Group by key
data = [{"key": "a", "val": 1}, {"key": "b", "val": 2}, {"key": "a", "val": 3}]
grouped = {}

for item in data:
    key = item["key"]
    if key not in grouped:
        grouped[key] = []
    grouped[key].append(item["val"])

print(grouped)
