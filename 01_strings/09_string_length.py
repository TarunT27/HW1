"""
Program 9: Find the length of a string without using len() function
This program manually calculates string length.
"""

def string_length(s):
    """Find length of string without using len()"""
    count = 0
    for _ in s:
        count += 1
    return count


# Main program
if __name__ == "__main__":
    test_strings = ["hello", "Python", "", "a", "12345", "Hello World"]
    
    print("String Length Finder (without len())")
    print("-" * 40)
    for test in test_strings:
        length = string_length(test)
        actual_len = len(test)
        print(f"'{test}' -> {length} (actual: {actual_len})")

"""
OUTPUT:
String Length Finder (without len())
----------------------------------------
'hello' -> 5 (actual: 5)
'Python' -> 6 (actual: 6)
'' -> 0 (actual: 0)
'a' -> 1 (actual: 1)
'12345' -> 5 (actual: 5)
'Hello World' -> 11 (actual: 11)
"""
