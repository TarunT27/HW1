"""
Program 10: Convert a string to uppercase and lowercase
Author: Python Programs Collection
Description: Converts strings between uppercase and lowercase formats
"""

def to_uppercase(s):
    """
    Convert string to uppercase.
    
    Args:
        s (str): The input string
        
    Returns:
        str: String in uppercase
    """
    return s.upper()


def to_lowercase(s):
    """
    Convert string to lowercase.
    
    Args:
        s (str): The input string
        
    Returns:
        str: String in lowercase
    """
    return s.lower()


def to_uppercase_manual(s):
    """
    Convert to uppercase without using upper() method.
    
    Args:
        s (str): The input string
        
    Returns:
        str: String in uppercase
    """
    result = ""
    for char in s:
        if 'a' <= char <= 'z':
            result += chr(ord(char) - 32)
        else:
            result += char
    return result


def to_lowercase_manual(s):
    """
    Convert to lowercase without using lower() method.
    
    Args:
        s (str): The input string
        
    Returns:
        str: String in lowercase
    """
    result = ""
    for char in s:
        if 'A' <= char <= 'Z':
            result += chr(ord(char) + 32)
        else:
            result += char
    return result


if __name__ == "__main__":
    # Test cases
    test_string = "Hello World"
    
    print(f"Original: '{test_string}'")
    print(f"Uppercase (upper()): '{to_uppercase(test_string)}'")
    print(f"Lowercase (lower()): '{to_lowercase(test_string)}'")
    print(f"Uppercase (manual): '{to_uppercase_manual(test_string)}'")
    print(f"Lowercase (manual): '{to_lowercase_manual(test_string)}'")
