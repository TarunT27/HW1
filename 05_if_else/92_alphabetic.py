"""
Program 92: Check if string contains only alphabetic characters
This program validates alphabetic content.
"""

def only_alphabetic(s):
    """Check if string contains only alphabetic characters"""
    if len(s) == 0:
        return False
    for char in s:
        if not char.isalpha():
            return False
    return True


# Main program
if __name__ == "__main__":
    test_strings = ["hello", "hello123", "abc", "123", "Hello World", ""]
    
    print("Alphabetic Checker")
    print("-" * 40)
    for s in test_strings:
        result = only_alphabetic(s)
        print(f"'{s}' -> Only alphabetic: {result}")

"""
OUTPUT:
Alphabetic Checker
----------------------------------------
'hello' -> Only alphabetic: True
'hello123' -> Only alphabetic: False
'abc' -> Only alphabetic: True
'123' -> Only alphabetic: False
'Hello World' -> Only alphabetic: False
'' -> Only alphabetic: False
"""
