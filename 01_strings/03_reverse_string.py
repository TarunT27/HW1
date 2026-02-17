"""
Program 3: Reverse a string
Author: Python Programs Collection
Description: Reverses a given string
"""

def reverse_string(s):
    """
    Reverse a string.
    
    Args:
        s (str): The input string
        
    Returns:
        str: The reversed string
    """
    return s[::-1]


def reverse_string_manual(s):
    """
    Reverse a string without using slicing.
    
    Args:
        s (str): The input string
        
    Returns:
        str: The reversed string
    """
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str


if __name__ == "__main__":
    # Test cases
    test_strings = ["hello", "python", "12345", "world"]
    
    for test in test_strings:
        print(f"Original: '{test}'")
        print(f"Reversed (slicing): '{reverse_string(test)}'")
        print(f"Reversed (manual): '{reverse_string_manual(test)}'\n")
