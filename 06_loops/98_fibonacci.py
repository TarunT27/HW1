# Print Fibonacci series
n = int(input("Enter count: "))
a, b = 0, 1

for _ in range(n):
    print(a)
    a, b = b, a + b
