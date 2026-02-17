"""
Program 11: Replace all occurrences of a substring in a string
Author: Python Programs Collection
Description: Replaces all instances of a substring with another substring
"""

def replace_substring(s, old, new):
    """
    Replace all occurrences of a substring using replace method.
    
    Args:
        s (str): The input string
        old (str): Substring to replace
        new (str): Replacement substring
        
    Returns:
        str: String with replacements
    """
    return s.replace(old, new)


def replace_substring_manual(s, old, new):
    """
    Replace substring without using replace() method.
    
    Args:
        s (str): The input string
        old (str): Substring to replace
        new (str): Replacement substring
        
    Returns:
        str: String with replacements
    """
    result = ""
    i = 0
    while i < len(s):
        if s[i:i+len(old)] == old:
            result += new
            i += len(old)
        else:
            result += s[i]
            i += 1
    return result


if __name__ == "__main__":
    # Test cases
    test_cases = [
        ("hello world", "world", "python"),
        ("aaaa", "aa", "b"),
        ("no match", "xyz", "abc"),
        ("test test test", "test", "exam")
    ]
    
    for s, old, new in test_cases:
        result1 = replace_substring(s, old, new)
        result2 = replace_substring_manual(s, old, new)
        print(f"String: '{s}'")
        print(f"  Replace '{old}' with '{new}'")
        print(f"  Using replace(): '{result1}'")
        print(f"  Manual: '{result2}'\n")
