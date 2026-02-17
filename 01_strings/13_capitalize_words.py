"""
Program 13: Capitalize the first letter of each word in a string
Author: Python Programs Collection
Description: Converts the first letter of each word to uppercase
"""

def capitalize_words(s):
    """
    Capitalize first letter of each word using title method.
    
    Args:
        s (str): The input string
        
    Returns:
        str: String with capitalized words
    """
    return s.title()


def capitalize_words_manual(s):
    """
    Capitalize words without using title() method.
    
    Args:
        s (str): The input string
        
    Returns:
        str: String with capitalized words
    """
    words = s.split()
    capitalized_words = []
    
    for word in words:
        if word:
            capitalized_word = word[0].upper() + word[1:]
            capitalized_words.append(capitalized_word)
    
    return " ".join(capitalized_words)


if __name__ == "__main__":
    # Test cases
    test_strings = ["hello world", "python programming", "a b c", "hELLO wORLD"]
    
    for test in test_strings:
        result1 = capitalize_words(test)
        result2 = capitalize_words_manual(test)
        print(f"Original: '{test}'")
        print(f"  title(): '{result1}'")
        print(f"  manual: '{result2}'\n")
