"""
Program 116: Check if a string is a valid palindrome (ignoring spaces and case)
This program validates palindromes with preprocessing.
"""

def is_valid_palindrome(s):
    """Check if string is valid palindrome ignoring spaces and case"""
    cleaned = ""
    for char in s:
        if char.isalnum():
            cleaned += char.lower()
    
    return cleaned == cleaned[::-1]


# Main program
if __name__ == "__main__":
    test_strings = [
        "A man a plan a canal Panama",
        "race car",
        "hello",
        "Was it a car or a cat I saw",
        "No"
    ]
    
    print("Valid Palindrome Checker")
    print("-" * 40)
    for s in test_strings:
        result = is_valid_palindrome(s)
        print(f"'{s}' -> {result}")

"""
OUTPUT:
Valid Palindrome Checker
----------------------------------------
'A man a plan a canal Panama' -> True
'race car' -> True
'hello' -> False
'Was it a car or a cat I saw' -> True
'No' -> False
"""
