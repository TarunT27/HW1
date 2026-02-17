"""
Program 104: Count the number of digits in a number using a loop
This program counts digits.
"""

def count_digits(num):
    """Count number of digits"""
    if num == 0:
        return 1
    num = abs(num)
    count = 0
    while num > 0:
        count += 1
        num //= 10
    return count


# Main program
if __name__ == "__main__":
    test_nums = [123, 0, 1000, -505, 9]
    
    print("Digit Counter")
    print("-" * 40)
    for num in test_nums:
        count = count_digits(num)
        print(f"{num} -> {count} digits")

"""
OUTPUT:
Digit Counter
----------------------------------------
123 -> 3 digits
0 -> 1 digits
1000 -> 4 digits
-505 -> 3 digits
9 -> 1 digits
"""
