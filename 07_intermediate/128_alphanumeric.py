"""
Program 128: Check if string contains only alphanumeric characters
This program validates alphanumeric content.
"""

def is_alphanumeric(s):
    """Check if string is alphanumeric only"""
    if not s:
        return False
    for char in s:
        if not char.isalnum():
            return False
    return True


# Main program
if __name__ == "__main__":
    test_strings = ["abc123", "hello", "hello!", "123", "", "a1b2c3"]
    
    print("Alphanumeric Checker")
    print("-" * 40)
    for s in test_strings:
        result = is_alphanumeric(s)
        print(f"'{s}' -> {result}")

"""
OUTPUT:
Alphanumeric Checker
----------------------------------------
'abc123' -> True
'hello' -> True
'hello!' -> False
'123' -> True
'' -> False
'a1b2c3' -> True
"""
