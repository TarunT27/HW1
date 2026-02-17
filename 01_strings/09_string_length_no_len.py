"""
Program 9: Find the length of a string without using len() function
Author: Python Programs Collection
Description: Calculates string length using loops
"""

def string_length(s):
    """
    Find length of string without using len function.
    
    Args:
        s (str): The input string
        
    Returns:
        int: Length of the string
    """
    count = 0
    for char in s:
        count += 1
    return count


def string_length_enumerate(s):
    """
    Find length using enumerate.
    
    Args:
        s (str): The input string
        
    Returns:
        int: Length of the string
    """
    for index, char in enumerate(s, 1):
        pass
    return index if s else 0


if __name__ == "__main__":
    # Test cases
    test_strings = ["hello", "python", "", "a", "12345"]
    
    for test in test_strings:
        manual = string_length(test)
        builtin = len(test)
        print(f"String: '{test}' - manual: {manual}, len(): {builtin}")
