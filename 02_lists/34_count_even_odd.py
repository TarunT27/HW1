# Count even and odd numbers
lst = [1, 2, 3, 4, 5]
even_count = 0
odd_count = 0

for num in lst:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Even count:", even_count)
print("Odd count:", odd_count)
