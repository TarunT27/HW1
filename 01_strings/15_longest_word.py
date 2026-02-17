"""
Program 15: Find the longest word in a string
This program identifies the word with the maximum length.
"""

def find_longest_word(s):
    """Find the longest word in a string"""
    words = s.split()
    if not words:
        return ""
    longest = words[0]
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest


# Main program
if __name__ == "__main__":
    test_strings = [
        "hello world programming",
        "the quick brown fox",
        "python",
        "a bb ccc dddd",
        "I am learning Python programming"
    ]
    
    print("Longest Word Finder")
    print("-" * 40)
    for test in test_strings:
        longest = find_longest_word(test)
        print(f"'{test}' -> '{longest}' (length: {len(longest)})")

"""
OUTPUT:
Longest Word Finder
----------------------------------------
'hello world programming' -> 'programming' (length: 11)
'the quick brown fox' -> 'quick' (length: 5)
'python' -> 'python' (length: 6)
'a bb ccc dddd' -> 'dddd' (length: 4)
'I am learning Python programming' -> 'programming' (length: 11)
"""
