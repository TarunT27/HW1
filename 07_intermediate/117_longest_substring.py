"""
Program 117: Find the longest substring without repeating characters
This program finds longest non-repeating substring.
"""

def longest_substring_without_repeat(s):
    """Find longest substring without repeating chars"""
    char_index = {}
    max_length = 0
    start = 0
    
    for i, char in enumerate(s):
        if char in char_index and char_index[char] >= start:
            start = char_index[char] + 1
        char_index[char] = i
        max_length = max(max_length, i - start + 1)
    
    return max_length


# Main program
if __name__ == "__main__":
    test_strings = ["hello", "abcabcbb", "bbbbb", "pwwkew", ""]
    
    print("Longest Non-Repeating Substring Finder")
    print("-" * 40)
    for s in test_strings:
        length = longest_substring_without_repeat(s)
        print(f"'{s}' -> Length: {length}")

"""
OUTPUT:
Longest Non-Repeating Substring Finder
----------------------------------------
'hello' -> Length: 4
'abcabcbb' -> Length: 3
'bbbbb' -> Length: 1
'pwwkew' -> Length: 3
'' -> Length: 0
"""
