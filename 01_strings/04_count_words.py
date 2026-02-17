"""
Program 4: Count the number of words in a string
Author: Python Programs Collection
Description: Counts the number of words in a given string
"""

def count_words(s):
    """
    Count the number of words in a string.
    
    Args:
        s (str): The input string
        
    Returns:
        int: The number of words
    """
    # Split by spaces and filter empty strings
    words = [word for word in s.split() if word]
    return len(words)


def count_words_manual(s):
    """
    Count words without using split method.
    
    Args:
        s (str): The input string
        
    Returns:
        int: The number of words
    """
    word_count = 0
    in_word = False
    
    for char in s:
        if char != ' ':
            if not in_word:
                word_count += 1
                in_word = True
        else:
            in_word = False
    
    return word_count


if __name__ == "__main__":
    # Test cases
    test_strings = ["hello world", "python programming language", "a b c d e", "   spaced   words   "]
    
    for test in test_strings:
        print(f"String: '{test}'")
        print(f"  Words (split): {count_words(test)}")
        print(f"  Words (manual): {count_words_manual(test)}\n")
