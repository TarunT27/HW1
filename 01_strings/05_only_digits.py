"""
Program 5: Check if a string contains only digits
This program validates if all characters in a string are digits.
"""

def contains_only_digits(s):
    """Check if string contains only digits"""
    if not s:  # Empty string
        return False
    for char in s:
        if not char.isdigit():
            return False
    return True


# Main program
if __name__ == "__main__":
    test_strings = ["12345", "123abc", "0", "00001", "abc123", ""]
    
    print("Digit Checker")
    print("-" * 40)
    for test in test_strings:
        result = contains_only_digits(test)
        print(f"'{test}' -> {result}")

"""
OUTPUT:
Digit Checker
----------------------------------------
'12345' -> True
'123abc' -> False
'0' -> True
'00001' -> True
'abc123' -> False
'' -> False
"""
