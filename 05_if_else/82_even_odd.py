"""
Program 82: Check if a number is odd or even
This program categorizes numbers as odd or even.
"""

def is_even_or_odd(num):
    """Check if number is even or odd"""
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"


# Main program
if __name__ == "__main__":
    test_nums = [1, 2, 3, 4, 5, 10, 15, 20, 0, -3]
    
    print("Even/Odd Checker")
    print("-" * 40)
    for num in test_nums:
        result = is_even_or_odd(num)
        print(f"{num} -> {result}")

"""
OUTPUT:
Even/Odd Checker
----------------------------------------
1 -> Odd
2 -> Even
3 -> Odd
4 -> Even
5 -> Odd
10 -> Even
15 -> Odd
20 -> Even
0 -> Even
-3 -> Odd
"""
