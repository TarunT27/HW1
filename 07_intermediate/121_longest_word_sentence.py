"""
Program 121: Find the longest word in a sentence
This program identifies the word with maximum length.
"""

def longest_word_in_sentence(s):
    """Find longest word in sentence"""
    words = s.split()
    if not words:
        return ""
    return max(words, key=len)


# Main program
if __name__ == "__main__":
    test_sentences = [
        "The quick brown fox",
        "hello world python programming",
        "a"
    ]
    
    print("Longest Word Finder (Sentence)")
    print("-" * 40)
    for s in test_sentences:
        result = longest_word_in_sentence(s)
        print(f"'{s}' -> '{result}'")

"""
OUTPUT:
Longest Word Finder (Sentence)
----------------------------------------
'The quick brown fox' -> 'quick'
'hello world python programming' -> 'programming'
'a' -> 'a'
"""
