"""
Program 12: Find the index of the first occurrence of a substring
Author: Python Programs Collection
Description: Returns the index where a substring first appears
"""

def find_substring_index(s, substring):
    """
    Find index of first occurrence using find method.
    
    Args:
        s (str): The input string
        substring (str): Substring to find
        
    Returns:
        int: Index of first occurrence or -1 if not found
    """
    return s.find(substring)


def find_substring_index_manual(s, substring):
    """
    Find substring index without using find() method.
    
    Args:
        s (str): The input string
        substring (str): Substring to find
        
    Returns:
        int: Index of first occurrence or -1 if not found
    """
    if not substring:
        return 0
    
    for i in range(len(s) - len(substring) + 1):
        if s[i:i+len(substring)] == substring:
            return i
    
    return -1


if __name__ == "__main__":
    # Test cases
    test_cases = [
        ("hello world", "world"),
        ("python programming", "prog"),
        ("test string", "xyz"),
        ("aaaa", "aa"),
        ("hello", "l")
    ]
    
    for s, substring in test_cases:
        index1 = find_substring_index(s, substring)
        index2 = find_substring_index_manual(s, substring)
        print(f"String: '{s}', substring: '{substring}'")
        print(f"  find(): {index1}, manual: {index2}")
