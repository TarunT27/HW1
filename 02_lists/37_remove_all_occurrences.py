# Remove all occurrences
lst = [1, 2, 3, 2, 4, 2]
value = 2
result = [x for x in lst if x != value]
print("Result:", result)
