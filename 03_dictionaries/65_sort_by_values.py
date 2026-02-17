# Sort by values
d = {'c': 3, 'a': 1, 'b': 2}
sorted_d = dict(sorted(d.items(), key=lambda x: x[1]))
print("Sorted:", sorted_d)
