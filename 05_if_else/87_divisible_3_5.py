# Check divisible by 3 and 5
n = int(input("Enter number: "))

if n % 3 == 0 and n % 5 == 0:
    print("Divisible by both")
else:
    print("Not divisible by both")
