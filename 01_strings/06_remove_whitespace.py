"""
Program 6: Remove all whitespaces from a string
Author: Python Programs Collection
Description: Removes all whitespace characters from a string
"""

def remove_whitespace(s):
    """
    Remove all whitespaces from a string using replace.
    
    Args:
        s (str): The input string
        
    Returns:
        str: String without whitespaces
    """
    return s.replace(" ", "")


def remove_whitespace_join(s):
    """
    Remove whitespaces using join and split.
    
    Args:
        s (str): The input string
        
    Returns:
        str: String without whitespaces
    """
    return "".join(s.split())


def remove_whitespace_manual(s):
    """
    Remove whitespaces without using built-in string methods.
    
    Args:
        s (str): The input string
        
    Returns:
        str: String without whitespaces
    """
    result = ""
    for char in s:
        if char != ' ' and char != '\t' and char != '\n':
            result += char
    return result


if __name__ == "__main__":
    # Test cases
    test_strings = ["hello world", "  python  ", "a b c d e", "\thello\nworld\t"]
    
    for test in test_strings:
        print(f"Original: '{test}'")
        print(f"Removed (replace): '{remove_whitespace(test)}'")
        print(f"Removed (join): '{remove_whitespace_join(test)}'")
        print(f"Removed (manual): '{remove_whitespace_manual(test)}'\n")
