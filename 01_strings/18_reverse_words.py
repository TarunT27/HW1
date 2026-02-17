"""
Program 18: Reverse the order of words in a string
Author: Python Programs Collection
Description: Reverses the order of words in a sentence
"""

def reverse_words(s):
    """
    Reverse word order using split and join.
    
    Args:
        s (str): The input string
        
    Returns:
        str: String with reversed word order
    """
    return " ".join(s.split()[::-1])


def reverse_words_loops(s):
    """
    Reverse words using loops.
    
    Args:
        s (str): The input string
        
    Returns:
        str: String with reversed word order
    """
    words = s.split()
    reversed_words = []
    
    for i in range(len(words) - 1, -1, -1):
        reversed_words.append(words[i])
    
    return " ".join(reversed_words)


if __name__ == "__main__":
    # Test cases
    test_strings = [
        "hello world",
        "python programming language",
        "the quick brown fox",
        "a",
        "one two three four"
    ]
    
    for test in test_strings:
        result1 = reverse_words(test)
        result2 = reverse_words_loops(test)
        print(f"Original: '{test}'")
        print(f"  Reversed: '{result1}'\n")
