# Find all subsets
lst = [1, 2, 3]
subsets = []

for i in range(1 << len(lst)):
    subset = []
    for j in range(len(lst)):
        if i & (1 << j):
            subset.append(lst[j])
    subsets.append(subset)

print(subsets)
