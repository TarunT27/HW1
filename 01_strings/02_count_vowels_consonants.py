"""
Program 2: Count vowels and consonants in a string
Author: Python Programs Collection
Description: Counts the number of vowels and consonants in a given string
"""

def count_vowels_consonants(s):
    """
    Count vowels and consonants in a string.
    
    Args:
        s (str): The input string
        
    Returns:
        tuple: (vowel_count, consonant_count)
    """
    s = s.lower()
    vowels = "aeiou"
    vowel_count = 0
    consonant_count = 0
    
    for char in s:
        if char.isalpha():
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1
    
    return vowel_count, consonant_count


if __name__ == "__main__":
    # Test cases
    test_strings = ["hello", "programming", "aEiOu", "bcdfg"]
    
    for test in test_strings:
        vowels, consonants = count_vowels_consonants(test)
        print(f"String: '{test}'")
        print(f"  Vowels: {vowels}, Consonants: {consonants}\n")
