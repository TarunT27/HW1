"""
Program 118: Count the frequency of each character in a string
This program creates a character frequency map.
"""

def char_frequency_dict(s):
    """Count frequency of each character"""
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    return freq


# Main program
if __name__ == "__main__":
    test_strings = ["hello", "mississippi", "aaa", "abc"]
    
    print("Character Frequency Counter")
    print("-" * 40)
    for s in test_strings:
        freq = char_frequency_dict(s)
        print(f"'{s}' -> {freq}")

"""
OUTPUT:
Character Frequency Counter
----------------------------------------
'hello' -> {'h': 1, 'e': 1, 'l': 2, 'o': 1}
'mississippi' -> {'m': 1, 'i': 4, 's': 4, 'p': 2}
'aaa' -> {'a': 3}
'abc' -> {'a': 1, 'b': 1, 'c': 1}
"""
