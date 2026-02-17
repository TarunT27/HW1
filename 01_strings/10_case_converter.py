"""
Program 10: Convert a string to uppercase and lowercase
This program demonstrates string case conversion.
"""

def convert_case(s):
    """Convert string to uppercase and lowercase"""
    uppercase = s.upper()
    lowercase = s.lower()
    return uppercase, lowercase


# Main program
if __name__ == "__main__":
    test_strings = ["Hello World", "PYTHON", "pYtHoN", "123abc"]
    
    print("String Case Converter")
    print("-" * 40)
    for test in test_strings:
        upper, lower = convert_case(test)
        print(f"Original: '{test}'")
        print(f"Uppercase: '{upper}'")
        print(f"Lowercase: '{lower}'\n")

"""
OUTPUT:
String Case Converter
----------------------------------------
Original: 'Hello World'
Uppercase: 'HELLO WORLD'
Lowercase: 'hello world'

Original: 'PYTHON'
Uppercase: 'PYTHON'
Lowercase: 'python'

Original: 'pYtHoN'
Uppercase: 'PYTHON'
Lowercase: 'python'

Original: '123abc'
Uppercase: '123ABC'
Lowercase: '123abc'
"""
