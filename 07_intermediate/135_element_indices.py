# Find element indices
lst = [1, 2, 3, 2, 4]
target = 2
indices = [i for i, val in enumerate(lst) if val == target]

print(indices)
