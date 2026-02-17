"""
Program 105: Find the sum of digits of a number using a loop
This program adds up individual digits.
"""

def sum_of_digits(num):
    """Find sum of digits"""
    num = abs(num)
    digit_sum = 0
    while num > 0:
        digit = num % 10
        digit_sum += digit
        num //= 10
    return digit_sum


# Main program
if __name__ == "__main__":
    test_nums = [123, 456, 1000, -789, 0]
    
    print("Sum of Digits Calculator")
    print("-" * 40)
    for num in test_nums:
        digit_sum = sum_of_digits(num)
        print(f"{num} -> Sum: {digit_sum}")

"""
OUTPUT:
Sum of Digits Calculator
----------------------------------------
123 -> Sum: 6
456 -> Sum: 15
1000 -> Sum: 1
-789 -> Sum: 24
0 -> Sum: 0
"""
