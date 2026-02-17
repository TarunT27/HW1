# Find median of list
lst = [1, 3, 2, 5, 4]
lst.sort()
n = len(lst)

if n % 2 == 1:
    print("Median:", lst[n // 2])
else:
    print("Median:", (lst[n // 2 - 1] + lst[n // 2]) / 2)
