"""
Program 17: Remove duplicate characters from a string
Author: Python Programs Collection
Description: Removes all duplicate characters from a string
"""

def remove_duplicates(s):
    """
    Remove duplicate characters using dict.fromkeys().
    
    Args:
        s (str): The input string
        
    Returns:
        str: String with duplicate characters removed
    """
    return "".join(dict.fromkeys(s))


def remove_duplicates_set(s):
    """
    Remove duplicates using set (order may not be preserved).
    
    Args:
        s (str): The input string
        
    Returns:
        str: String with duplicates removed
    """
    seen = set()
    result = ""
    for char in s:
        if char not in seen:
            seen.add(char)
            result += char
    return result


if __name__ == "__main__":
    # Test cases
    test_strings = ["hello", "programming", "aabbcc", "a", "mississippi"]
    
    for test in test_strings:
        result1 = remove_duplicates(test)
        result2 = remove_duplicates_set(test)
        print(f"String: '{test}'")
        print(f"  dict.fromkeys(): '{result1}'")
        print(f"  set method: '{result2}'\n")
