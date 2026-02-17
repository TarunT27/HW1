# Generator expression
nums = [1, 2, 3, 4, 5]
gen = (x ** 2 for x in nums)

for val in gen:
    print(val)
