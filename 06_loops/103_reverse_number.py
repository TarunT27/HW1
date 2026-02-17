"""
Program 103: Find the reverse of a number using a loop
This program reverses number digits.
"""

def reverse_number(num):
    """Reverse a number"""
    reversed_num = 0
    original = num
    while num > 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num //= 10
    return reversed_num


# Main program
if __name__ == "__main__":
    test_nums = [123, 1000, 505, 9]
    
    print("Number Reverser")
    print("-" * 40)
    for num in test_nums:
        reversed_num = reverse_number(num)
        print(f"{num} -> {reversed_num}")

"""
OUTPUT:
Number Reverser
----------------------------------------
123 -> 321
1000 -> 1
505 -> 505
9 -> 9
"""
