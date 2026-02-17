"""
Program 95: Determine if a number is divisible by a specific number
This program checks divisibility.
"""

def is_divisible(num, divisor):
    """Check if num is divisible by divisor"""
    if divisor == 0:
        return "Cannot divide by zero"
    elif num % divisor == 0:
        return True
    else:
        return False


# Main program
if __name__ == "__main__":
    test_cases = [
        (10, 5),
        (15, 3),
        (20, 7),
        (100, 10),
        (7, 2),
        (0, 5)
    ]
    
    print("Divisibility Checker")
    print("-" * 40)
    for num, divisor in test_cases:
        result = is_divisible(num, divisor)
        print(f"{num} divisible by {divisor} -> {result}")

"""
OUTPUT:
Divisibility Checker
----------------------------------------
10 divisible by 5 -> True
15 divisible by 3 -> True
20 divisible by 7 -> False
100 divisible by 10 -> True
7 divisible by 2 -> False
0 divisible by 5 -> True
"""
