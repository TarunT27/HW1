"""
Program 97: Find the factorial of a number using a loop
This program calculates n! = n * (n-1) * ... * 1
"""

def factorial(n):
    """Calculate factorial using loop"""
    if n < 0:
        return "Negative number"
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


# Main program
if __name__ == "__main__":
    test_nums = [0, 1, 5, 10, 3]
    
    print("Factorial Calculator")
    print("-" * 40)
    for num in test_nums:
        fact = factorial(num)
        print(f"{num}! = {fact}")

"""
OUTPUT:
Factorial Calculator
----------------------------------------
0! = 1
1! = 1
5! = 120
10! = 3628800
3! = 6
"""
