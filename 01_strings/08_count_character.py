"""
Program 8: Count occurrences of a character in a string
Author: Python Programs Collection
Description: Counts how many times a specific character appears in a string
"""

def count_character(s, char):
    """
    Count occurrences of a character in a string using count method.
    
    Args:
        s (str): The input string
        char (str): The character to count
        
    Returns:
        int: Number of occurrences
    """
    return s.count(char)


def count_character_manual(s, char):
    """
    Count character occurrences without using count method.
    
    Args:
        s (str): The input string
        char (str): The character to count
        
    Returns:
        int: Number of occurrences
    """
    count = 0
    for c in s:
        if c == char:
            count += 1
    return count


if __name__ == "__main__":
    # Test cases
    test_string = "hello world"
    test_chars = ['l', 'o', 'h', 'x']
    
    print(f"String: '{test_string}'")
    for char in test_chars:
        count1 = count_character(test_string, char)
        count2 = count_character_manual(test_string, char)
        print(f"Character '{char}' - count method: {count1}, manual: {count2}")
