"""
Program 114: Find the factorial of a number using a while loop
This program calculates factorial with while loop.
"""

def factorial_while(n):
    """Calculate factorial using while loop"""
    if n < 0:
        return "Negative number"
    result = 1
    i = n
    while i > 0:
        result *= i
        i -= 1
    return result


# Main program
if __name__ == "__main__":
    test_nums = [0, 1, 5, 10, 3]
    
    print("Factorial Calculator (while loop)")
    print("-" * 40)
    for num in test_nums:
        fact = factorial_while(num)
        print(f"{num}! = {fact}")

"""
OUTPUT:
Factorial Calculator (while loop)
----------------------------------------
0! = 1
1! = 1
5! = 120
10! = 3628800
3! = 6
"""
