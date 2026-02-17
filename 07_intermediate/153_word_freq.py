"""
Program 153: Count word frequency in text
This program counts how many times each word appears in a given text.
"""

def word_frequency(text):
    """Count word frequency"""
    words = text.lower().split()
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    return freq


# Main program
if __name__ == "__main__":
    test_cases = [
        "hello world hello python",
        "the quick brown fox jumps over the lazy dog",
    ]
    
    print("Word Frequency Counter")
    print("-" * 40)
    for text in test_cases:
        freq = word_frequency(text)
        print(f"Text: {text}")
        print(f"Frequency: {freq}\n")

"""
OUTPUT:
Word Frequency Counter
----------------------------------------
Text: hello world hello python
Frequency: {'hello': 2, 'world': 1, 'python': 1}

Text: the quick brown fox jumps over the lazy dog
Frequency: {'the': 2, 'quick': 1, 'brown': 1, 'fox': 1, 'jumps': 1, 'over': 1, 'lazy': 1, 'dog': 1}
"""
