"""
Program 119: Find the first non-repeating character in a string
This program identifies the first unique character.
"""

def first_non_repeating(s):
    """Find first non-repeating character"""
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    
    for char in s:
        if freq[char] == 1:
            return char
    return None


# Main program
if __name__ == "__main__":
    test_strings = ["hello", "aabbcc", "abcabc", "aaa", ""]
    
    print("First Non-Repeating Character Finder")
    print("-" * 40)
    for s in test_strings:
        result = first_non_repeating(s)
        print(f"'{s}' -> {result}")

"""
OUTPUT:
First Non-Repeating Character Finder
----------------------------------------
'hello' -> 'h'
'aabbcc' -> None
'abcabc' -> None
'aaa' -> None
'' -> None
"""
