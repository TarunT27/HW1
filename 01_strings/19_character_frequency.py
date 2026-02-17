"""
Program 19: Count the frequency of each character in a string
Author: Python Programs Collection
Description: Creates a frequency map of all characters in a string
"""

def character_frequency(s):
    """
    Count frequency of each character using dictionary.
    
    Args:
        s (str): The input string
        
    Returns:
        dict: Dictionary with character frequencies
    """
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    return freq


def character_frequency_collections(s):
    """
    Count frequency using Counter from collections.
    
    Args:
        s (str): The input string
        
    Returns:
        dict: Dictionary with character frequencies
    """
    from collections import Counter
    return dict(Counter(s))


if __name__ == "__main__":
    # Test cases
    test_strings = ["hello", "programming", "aabbcc", "mississippi"]
    
    for test in test_strings:
        freq = character_frequency(test)
        print(f"String: '{test}'")
        print(f"  Frequencies: {freq}\n")
