"""
Program 85: Check if a string contains a vowel
This program checks for presence of vowels.
"""

def contains_vowel(s):
    """Check if string contains a vowel"""
    vowels = "aeiouAEIOU"
    for char in s:
        if char in vowels:
            return True
    return False


# Main program
if __name__ == "__main__":
    test_strings = ["hello", "xyz", "aEiOu", "bcdfg", "Python"]
    
    print("Vowel Checker")
    print("-" * 40)
    for s in test_strings:
        result = contains_vowel(s)
        print(f"'{s}' -> Contains vowel: {result}")

"""
OUTPUT:
Vowel Checker
----------------------------------------
'hello' -> Contains vowel: True
'xyz' -> Contains vowel: False
'aEiOu' -> Contains vowel: True
'bcdfg' -> Contains vowel: False
'Python' -> Contains vowel: True
"""
