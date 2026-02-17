"""
Program 88: Check if a number is prime
This program validates if a number is prime.
"""

def is_prime(num):
    """Check if number is prime"""
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    return True


# Main program
if __name__ == "__main__":
    test_nums = [2, 3, 4, 5, 10, 11, 17, 20, 23, 1, 0]
    
    print("Prime Number Checker")
    print("-" * 40)
    for num in test_nums:
        result = is_prime(num)
        print(f"{num} -> Prime: {result}")

"""
OUTPUT:
Prime Number Checker
----------------------------------------
2 -> Prime: True
3 -> Prime: True
4 -> Prime: False
5 -> Prime: True
10 -> Prime: False
11 -> Prime: True
17 -> Prime: True
20 -> Prime: False
23 -> Prime: True
1 -> Prime: False
0 -> Prime: False
"""
