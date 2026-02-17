# Sorted with key function
data = [("Alice", 25), ("Bob", 20), ("Charlie", 30)]
sorted_data = sorted(data, key=lambda x: x[1])

print(sorted_data)
