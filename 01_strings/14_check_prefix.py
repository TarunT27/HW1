"""
Program 14: Check if a string starts with a specific prefix
Author: Python Programs Collection
Description: Verifies if a string begins with a given prefix
"""

def starts_with_prefix(s, prefix):
    """
    Check if string starts with prefix using startswith method.
    
    Args:
        s (str): The input string
        prefix (str): The prefix to check
        
    Returns:
        bool: True if starts with prefix, False otherwise
    """
    return s.startswith(prefix)


def starts_with_prefix_manual(s, prefix):
    """
    Check prefix without using startswith() method.
    
    Args:
        s (str): The input string
        prefix (str): The prefix to check
        
    Returns:
        bool: True if starts with prefix, False otherwise
    """
    if len(prefix) > len(s):
        return False
    
    return s[:len(prefix)] == prefix


if __name__ == "__main__":
    # Test cases
    test_cases = [
        ("hello world", "hello"),
        ("python", "py"),
        ("test string", "xyz"),
        ("abc", ""),
        ("start", "start")
    ]
    
    for s, prefix in test_cases:
        result1 = starts_with_prefix(s, prefix)
        result2 = starts_with_prefix_manual(s, prefix)
        print(f"String: '{s}', prefix: '{prefix}'")
        print(f"  startswith(): {result1}, manual: {result2}")
