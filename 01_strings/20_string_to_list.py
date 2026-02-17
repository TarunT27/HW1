"""
Program 20: Convert a string to a list of characters
Author: Python Programs Collection
Description: Converts a string into a list containing individual characters
"""

def string_to_list(s):
    """
    Convert string to list of characters using list().
    
    Args:
        s (str): The input string
        
    Returns:
        list: List of characters
    """
    return list(s)


def string_to_list_manual(s):
    """
    Convert string to list without using list() constructor.
    
    Args:
        s (str): The input string
        
    Returns:
        list: List of characters
    """
    char_list = []
    for char in s:
        char_list.append(char)
    return char_list


def string_to_list_comprehension(s):
    """
    Convert using list comprehension.
    
    Args:
        s (str): The input string
        
    Returns:
        list: List of characters
    """
    return [char for char in s]


if __name__ == "__main__":
    # Test cases
    test_strings = ["hello", "python", "123", "a b c"]
    
    for test in test_strings:
        result1 = string_to_list(test)
        result2 = string_to_list_manual(test)
        result3 = string_to_list_comprehension(test)
        print(f"String: '{test}'")
        print(f"  list(): {result1}")
        print(f"  manual: {result2}")
        print(f"  comprehension: {result3}\n")
