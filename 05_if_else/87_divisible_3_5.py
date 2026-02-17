"""
Program 87: Check if a number is divisible by both 3 and 5
This program validates divisibility conditions.
"""

def divisible_by_3_and_5(num):
    """Check if divisible by both 3 and 5"""
    if num % 3 == 0 and num % 5 == 0:
        return True
    else:
        return False


# Main program
if __name__ == "__main__":
    test_nums = [15, 30, 10, 9, 45, 20, 0]
    
    print("Divisibility Checker (3 and 5)")
    print("-" * 40)
    for num in test_nums:
        result = divisible_by_3_and_5(num)
        print(f"{num} -> Divisible by 3 and 5: {result}")

"""
OUTPUT:
Divisibility Checker (3 and 5)
----------------------------------------
15 -> Divisible by 3 and 5: True
30 -> Divisible by 3 and 5: True
10 -> Divisible by 3 and 5: False
9 -> Divisible by 3 and 5: False
45 -> Divisible by 3 and 5: True
20 -> Divisible by 3 and 5: False
0 -> Divisible by 3 and 5: True
"""
