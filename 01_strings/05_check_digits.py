"""
Program 5: Check if a string contains only digits
Author: Python Programs Collection
Description: Verifies if a string contains only numeric digits
"""

def contains_only_digits(s):
    """
    Check if a string contains only digits.
    
    Args:
        s (str): The input string
        
    Returns:
        bool: True if string contains only digits, False otherwise
    """
    if not s:
        return False
    return s.isdigit()


def contains_only_digits_manual(s):
    """
    Check if string contains only digits without using isdigit().
    
    Args:
        s (str): The input string
        
    Returns:
        bool: True if string contains only digits, False otherwise
    """
    if not s:
        return False
    
    for char in s:
        if char < '0' or char > '9':
            return False
    return True


if __name__ == "__main__":
    # Test cases
    test_strings = ["12345", "123.45", "abc123", "000", "123 456", ""]
    
    for test in test_strings:
        result1 = contains_only_digits(test)
        result2 = contains_only_digits_manual(test)
        print(f"'{test}' - isdigit: {result1}, manual: {result2}")
