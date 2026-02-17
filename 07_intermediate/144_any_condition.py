# Check if any element satisfies condition
lst = [1, 2, 3, 4]

if any(x > 3 for x in lst):
    print("Has element > 3")
else:
    print("No element > 3")
