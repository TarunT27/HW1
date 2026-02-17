"""
Program 16: Check if two strings are rotations of each other
Author: Python Programs Collection
Description: Verifies if one string is a rotation of another
"""

def are_rotations(s1, s2):
    """
    Check if s2 is a rotation of s1.
    
    Args:
        s1 (str): First string
        s2 (str): Second string
        
    Returns:
        bool: True if s2 is rotation of s1, False otherwise
    """
    if len(s1) != len(s2):
        return False
    
    # If s2 is rotation of s1, it will be substring of s1+s1
    return s2 in s1 + s1


def are_rotations_manual(s1, s2):
    """
    Check rotation without using 'in' operator.
    
    Args:
        s1 (str): First string
        s2 (str): Second string
        
    Returns:
        bool: True if s2 is rotation of s1, False otherwise
    """
    if len(s1) != len(s2):
        return False
    
    # Try all rotations
    for i in range(len(s1)):
        if s1[i:] + s1[:i] == s2:
            return True
    
    return False


if __name__ == "__main__":
    # Test cases
    test_cases = [
        ("abcd", "cdab"),
        ("abcd", "acbd"),
        ("hello", "llohe"),
        ("test", "stte"),
        ("a", "a")
    ]
    
    for s1, s2 in test_cases:
        result1 = are_rotations(s1, s2)
        result2 = are_rotations_manual(s1, s2)
        print(f"'{s1}' and '{s2}' - using 'in': {result1}, manual: {result2}")
