"""
Program 115: Calculate sum of squares of first n natural numbers using a loop
This program calculates 1^2 + 2^2 + ... + n^2
"""

def sum_of_squares(n):
    """Calculate sum of squares of first n numbers"""
    total = 0
    for i in range(1, n + 1):
        total += i * i
    return total


# Main program
if __name__ == "__main__":
    test_nums = [1, 5, 10, 3]
    
    print("Sum of Squares Calculator")
    print("-" * 40)
    for n in test_nums:
        total = sum_of_squares(n)
        print(f"Sum of squares of first {n} numbers = {total}")

"""
OUTPUT:
Sum of Squares Calculator
----------------------------------------
Sum of squares of first 1 numbers = 1
Sum of squares of first 5 numbers = 55
Sum of squares of first 10 numbers = 385
Sum of squares of first 3 numbers = 14
"""
