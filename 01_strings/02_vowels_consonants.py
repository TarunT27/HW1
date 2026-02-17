"""
Program 2: Count vowels and consonants in a string
This program identifies and counts all vowels and consonants.
"""

def count_vowels_consonants(s):
    """Count the number of vowels and consonants in a string"""
    vowels = "aeiouAEIOU"
    vowel_count = 0
    consonant_count = 0
    
    for char in s:
        if char.isalpha():  # Check if character is alphabetic
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1
    
    return vowel_count, consonant_count


# Main program
if __name__ == "__main__":
    test_strings = ["Hello World", "Python Programming", "aeiou", "bcdfg"]
    
    print("Vowel and Consonant Counter")
    print("-" * 40)
    for test in test_strings:
        vowels, consonants = count_vowels_consonants(test)
        print(f"'{test}'")
        print(f"  Vowels: {vowels}, Consonants: {consonants}\n")

"""
OUTPUT:
Vowel and Consonant Counter
----------------------------------------
'Hello World'
  Vowels: 3, Consonants: 7

'Python Programming'
  Vowels: 4, Consonants: 11

'aeiou'
  Vowels: 5, Consonants: 0

'bcdfg'
  Vowels: 0, Consonants: 5
"""
