# Cumulative sum
lst = [1, 2, 3, 4]
result = []
total = 0

for num in lst:
    total += num
    result.append(total)

print("Cumulative sum:", result)
