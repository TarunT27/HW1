"""
Program 1: Check if a string is a palindrome
A palindrome is a string that reads the same forwards and backwards.
"""

def is_palindrome(s):
    """Check if a string is a palindrome (ignoring spaces and case)"""
    # Remove spaces and convert to lowercase
    cleaned = s.replace(" ", "").lower()
    # Check if the string equals its reverse
    return cleaned == cleaned[::-1]


# Main program
if __name__ == "__main__":
    test_strings = ["racecar", "hello", "A man a plan a canal Panama", "12321", "12345"]
    
    print("Palindrome Checker")
    print("-" * 40)
    for test in test_strings:
        result = is_palindrome(test)
        print(f"'{test}' -> {result}")

"""
OUTPUT:
Palindrome Checker
----------------------------------------
'racecar' -> True
'hello' -> False
'A man a plan a canal Panama' -> True
'12321' -> True
'12345' -> False
"""
