"""
Program 15: Find the longest word in a string
Author: Python Programs Collection
Description: Returns the longest word from a string
"""

def find_longest_word(s):
    """
    Find the longest word in a string.
    
    Args:
        s (str): The input string
        
    Returns:
        str: The longest word
    """
    words = s.split()
    if not words:
        return ""
    
    return max(words, key=len)


def find_longest_word_manual(s):
    """
    Find longest word with manual iteration.
    
    Args:
        s (str): The input string
        
    Returns:
        str: The longest word
    """
    words = s.split()
    if not words:
        return ""
    
    longest = words[0]
    for word in words:
        if len(word) > len(longest):
            longest = word
    
    return longest


if __name__ == "__main__":
    # Test cases
    test_strings = [
        "hello world",
        "python programming language",
        "a quick brown fox",
        "the cat sat",
        ""
    ]
    
    for test in test_strings:
        result1 = find_longest_word(test)
        result2 = find_longest_word_manual(test)
        print(f"String: '{test}'")
        print(f"  max with key: '{result1}'")
        print(f"  manual: '{result2}'\n")
