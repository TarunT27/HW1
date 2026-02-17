"""
Program 81: Check if a number is positive, negative, or zero
This program categorizes numbers by sign.
"""

def check_sign(num):
    """Check if number is positive, negative, or zero"""
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"


# Main program
if __name__ == "__main__":
    test_nums = [10, -5, 0, 100, -25, 0.5]
    
    print("Number Sign Checker")
    print("-" * 40)
    for num in test_nums:
        result = check_sign(num)
        print(f"{num} -> {result}")

"""
OUTPUT:
Number Sign Checker
----------------------------------------
10 -> Positive
-5 -> Negative
0 -> Zero
100 -> Positive
-25 -> Negative
0.5 -> Positive
"""
