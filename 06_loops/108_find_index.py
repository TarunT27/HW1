# Find index of element
lst = [1, 2, 3, 4, 5]
num = 3

for i, val in enumerate(lst):
    if val == num:
        print("Index:", i)
        break
