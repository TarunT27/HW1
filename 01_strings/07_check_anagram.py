"""
Program 7: Check if a string is an anagram of another string
Author: Python Programs Collection
Description: Verifies if two strings are anagrams of each other
"""

def is_anagram(s1, s2):
    """
    Check if two strings are anagrams.
    
    Args:
        s1 (str): First string
        s2 (str): Second string
        
    Returns:
        bool: True if anagrams, False otherwise
    """
    # Remove spaces and convert to lowercase
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()
    
    # Compare sorted characters
    return sorted(s1) == sorted(s2)


def is_anagram_counting(s1, s2):
    """
    Check anagrams by counting character frequencies.
    
    Args:
        s1 (str): First string
        s2 (str): Second string
        
    Returns:
        bool: True if anagrams, False otherwise
    """
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()
    
    if len(s1) != len(s2):
        return False
    
    char_count = {}
    for char in s1:
        char_count[char] = char_count.get(char, 0) + 1
    
    for char in s2:
        if char not in char_count:
            return False
        char_count[char] -= 1
        if char_count[char] < 0:
            return False
    
    return True


if __name__ == "__main__":
    # Test cases
    test_pairs = [("listen", "silent"), ("hello", "world"), ("dormitory", "dirty room"),
                  ("abc", "bca"), ("12345", "54321")]
    
    for s1, s2 in test_pairs:
        result1 = is_anagram(s1, s2)
        result2 = is_anagram_counting(s1, s2)
        print(f"'{s1}' and '{s2}' - sorted: {result1}, counting: {result2}")
