# Remove duplicates
lst = [1, 2, 2, 3, 3, 3]
result = list(dict.fromkeys(lst))
print("Without duplicates:", result)
