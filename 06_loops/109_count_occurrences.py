# Count occurrences
lst = [1, 2, 2, 3, 2, 4]
target = 2
count = 0

for item in lst:
    if item == target:
        count += 1

print("Count:", count)
