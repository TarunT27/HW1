"""
Program 158: Count unique words in text
This program counts how many unique (distinct) words appear in text.
"""

def unique_word_count(text):
    """Count unique words"""
    words = text.lower().split()
    return len(set(words))


# Main program
if __name__ == "__main__":
    test_cases = [
        "hello world hello python",
        "the quick brown fox",
        "a a a a a",
    ]
    
    print("Unique Words Counter")
    print("-" * 40)
    for text in test_cases:
        count = unique_word_count(text)
        words = set(text.lower().split())
        print(f"Text: {text}")
        print(f"Unique words: {words}")
        print(f"Count: {count}\n")

"""
OUTPUT:
Unique Words Counter
----------------------------------------
Text: hello world hello python
Unique words: {'hello', 'world', 'python'}
Count: 3

Text: the quick brown fox
Unique words: {'the', 'quick', 'brown', 'fox'}
Count: 4

Text: a a a a a
Unique words: {'a'}
Count: 1
"""
