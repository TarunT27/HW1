"""
Program 19: Count the frequency of each character in a string
This program creates a frequency map of all characters.
"""

def character_frequency(s):
    """Count frequency of each character in a string"""
    freq = {}
    for char in s:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    return freq


# Main program
if __name__ == "__main__":
    test_strings = ["hello", "mississippi", "aabbcc", "programming"]
    
    print("Character Frequency Counter")
    print("-" * 40)
    for test in test_strings:
        freq = character_frequency(test)
        print(f"'{test}':")
        for char, count in sorted(freq.items()):
            print(f"  '{char}': {count}")
        print()

"""
OUTPUT:
Character Frequency Counter
----------------------------------------
'hello':
  'e': 1
  'h': 1
  'l': 2
  'o': 1

'mississippi':
  'i': 4
  'm': 1
  'p': 2
  's': 4

'aabbcc':
  'a': 2
  'b': 2
  'c': 2

'programming':
  'a': 1
  'g': 2
  'm': 2
  'o': 1
  'p': 1
  'r': 2
"""
