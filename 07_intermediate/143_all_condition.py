# Check if all elements satisfy condition
lst = [2, 4, 6, 8]

if all(x % 2 == 0 for x in lst):
    print("All even")
else:
    print("Not all even")
