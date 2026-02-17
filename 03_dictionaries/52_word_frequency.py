"""
Program 52: Count the frequency of each word in a string using a dictionary
This program creates a frequency map of words.
"""

def word_frequency(s):
    """Count frequency of each word in a string"""
    words = s.lower().split()
    freq = {}
    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1
    return freq


# Main program
if __name__ == "__main__":
    test_strings = [
        "hello world hello",
        "the quick brown fox jumps over the lazy dog",
        "python python python",
        "a b c a b a",
    ]
    
    print("Word Frequency Counter")
    print("-" * 40)
    for s in test_strings:
        freq = word_frequency(s)
        print(f"'{s}'")
        print(f"  -> {freq}\n")

"""
OUTPUT:
Word Frequency Counter
----------------------------------------
'hello world hello'
  -> {'hello': 2, 'world': 1}

'the quick brown fox jumps over the lazy dog'
  -> {'the': 2, 'quick': 1, 'brown': 1, 'fox': 1, 'jumps': 1, 'over': 1, 'lazy': 1, 'dog': 1}

'python python python'
  -> {'python': 3}

'a b c a b a'
  -> {'a': 3, 'b': 2, 'c': 1}
"""
