"""
Program 110: Find GCD (Greatest Common Divisor) of two numbers using a loop
This program calculates GCD.
"""

def gcd(a, b):
    """Find GCD using Euclidean algorithm"""
    a, b = abs(a), abs(b)
    while b != 0:
        a, b = b, a % b
    return a


# Main program
if __name__ == "__main__":
    test_cases = [
        (12, 8),
        (50, 15),
        (100, 25),
        (17, 19),
        (0, 5)
    ]
    
    print("GCD Calculator")
    print("-" * 40)
    for a, b in test_cases:
        result = gcd(a, b)
        print(f"GCD({a}, {b}) = {result}")

"""
OUTPUT:
GCD Calculator
----------------------------------------
GCD(12, 8) = 4
GCD(50, 15) = 5
GCD(100, 25) = 25
GCD(17, 19) = 1
GCD(0, 5) = 5
"""
