# Find second largest
lst = [1, 5, 3, 9, 2]
lst = list(set(lst))
lst.sort()

print("Second Largest:", lst[-2])
